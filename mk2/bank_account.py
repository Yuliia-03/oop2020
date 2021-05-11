class MyAccount:
    
    def __init__(self, first_name, second_name, status = 0):
        
        self.first_name = first_name
        self.second_name = second_name
        
        self.status = status
        
        self.amound_of_money = 0
        self.deposit_money = 0
        
        
    def my_open_account(self):
        
        self.status = str(self.first_name + " " + self.second_name)
        self.status += str("\nБаланс рахунку: " + str(self.amound_of_money))
        self.status += str("\nБаланс депозитних коштів: " + str(self.deposit_money) + "\n")
        return self.status
    
    def put_account(self, money):
        
        self.amound_of_money += money
        return self.amound_of_money
       
    def get_accaunt(self, money):
        self.amound_of_money -= money
        return self.amound_of_money
    
    
    def send_deposit(self, amound_of_money, deposit_rate, deposit_time):
        
        self.deposit_money = (amound_of_money * (deposit_rate/100) / 12) * deposit_time
        self.tax = self.deposit_money * 0.18
        self.deposit_money -= self.tax
        self.deposit_money += amound_of_money
        return self.deposit_money