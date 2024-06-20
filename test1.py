from services.sms_services.fivesim_sms_service import FiveSim








fivesim=FiveSim()

fivesim

google_prices=fivesim.get_product_prices_by_service(service_name="google")

list_price_json = google_prices.json()

filtered_prices=fivesim.filtered_sorted_country_prices(list_price_json)

print(filtered_prices)





# balance=fivesim.get_balance()

# code=fivesim.get_code('google')

# print(code)











# driver = webdriver.Chrome()
# gmail.createAccount(driver=driver,first_name="ergun",last_name="huseyn",month=3,day=25,year=1998,GenderEnum=GenderEnum.ERKEK,password="asdsa23214")
