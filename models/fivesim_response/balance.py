
class DefaultCountry:
    def __init__(self,name:str,iso:str,prefix:str):
            self.name=name
            self.iso=iso
            self.prefix=prefix



class DefaultOperator:
    def __init__(self,name:str):
            self.name=name


class Balance:   
    def __init__(self,id:int,email: str, vendor: str, default_forwarding_number: str, balance: float, rating: float,default_country: DefaultCountry,default_operator:DefaultOperator,frozen_balance:float):
        self.id = id
        self.email = email
        self.vendor = vendor
        self.default_forwarding_number = default_forwarding_number
        self.balance = balance
        self.rating = rating
        self.default_country = default_country
        self.default_operator=default_operator
        self.frozen_balance=frozen_balance




