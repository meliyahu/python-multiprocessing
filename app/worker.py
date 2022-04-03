import time
class Customer:
    def __init__(self, customer):
        self.customer = customer
    def execute(self):
        time.sleep(2)
        print(f'The customer is {self.customer["last_name"]}')
        return f'The customer {self.customer["first_name"]} was dealt with!'