import time
import requests
import os
from dotenv import load_dotenv
from models.fivesim_response.balance import Balance


class FiveSim:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('FIVESIM_API_KEY')
        self.api_url = os.getenv('FIVESIM_BASE_API_URL')
        self.headers= {
                        'Authorization': 'Bearer ' + self.token,
                        'Accept': 'application/json',
                      }
        self.headers_without_token={
             'Accept': 'application/json'
        }
        self.banned_country=os.getenv('BANNED_COUNTRY')


    # def get_balance(self) -> Balance:
    #     endpoint=f"{self.api_url}/user/profile"              
    #     response = requests.get(endpoint,headers=self.headers)
    #     response.raise_for_status()  # Hata durumunda exception fırlatır        
    #     return response.json()  
    
    def get_balance(self):
        endpoint=f"{self.api_url}/user/profile"              
        response = requests.get(endpoint,headers=self.headers)
        response.raise_for_status()  # Hata durumunda exception fırlatır        
        return response.json()  



    def get_product_prices_by_service(self,service_name):
        endpoint=f"{self.api_url}/guest/prices?product={service_name}"   
        response=requests.get(endpoint,headers=self.headers_without_token)
        response.raise_for_status()  
        return response.json() 
    
    def buy_phone(self,product,country="any",operator="any"):
        endpoint=f"{self.api_url}/user/buy/activation/{country}/{operator}/{product}"
        print(endpoint)
        response = requests.get(endpoint,headers=self.headers)
        response.raise_for_status()  
        return response.json()
    
    def check_order(self,order_id):
        endpoint=f"{self.api_url}/user/check/{order_id}"
        response=requests.get(endpoint,headers=self.headers)
        response.raise_for_status()  
        return response.json()
    
    def cancel_order(self,order_id):
        endpoint=f"{self.api_url}/user/cancel/{order_id}"
        response = requests.get(endpoint,headers=self.headers)  
        response.raise_for_status()   
        return response.json() 


    def get_code(self,service_name):

        list_price=self.get_product_prices_by_service(service_name)

        sorted_list_price=self.filtered_sorted_country_prices(list_price)

        country=sorted_list_price[0].get('country')

        print(country)

        operator=sorted_list_price[0].get('operator_name')

        order=self.buy_phone(service_name,country=country,operator=operator)

        order_id=order.get('id')

        count=0

        while(True):
           
           if count>60:    
               self.cancel_order(order_id)   
               break     
            

           message=self.check_order(order_id)
           if message.get('status')=='RECEIVED':
               sms_list = message.get("sms", [])
               if sms_list:                    
                    for sms in sms_list:
                        text = sms.get("code")
                        if text:
                            return text
            
           count+=1
           time.sleep(1)








    def filtered_sorted_country_prices(self,service_prices):
            
        new_list_price_models=[]

        firs_key=next(iter(service_prices))

        for country,operators in service_prices[firs_key].items():
            
            if country in self.banned_country:
                continue

            for operator_name,details in operators.items():
                count=details.get('count')
                rate=details.get('rate')
                cost=details.get('cost')
                
                
                if count is not None and count > 0  and rate is not None and rate > 50:
                    net_cost=cost*((200-rate)/100)
                    list_price_model = {   
                                            'country':country,
                                            'operator_name': operator_name,
                                            'cost': cost,
                                            'count': count,
                                            'rate': rate,  
                                            'net_cost': net_cost    
                                        }

                    new_list_price_models.append(list_price_model)

            

        sorted_data = sorted(new_list_price_models, key=lambda x: x['net_cost'], reverse=False)    

        return sorted_data





    