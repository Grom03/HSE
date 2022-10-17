from datetime import datetime

class Account:
    def __init__(self):
        self.balance = 0
        self.all_operations = []
    
    def put_money(self, amount):
        self.balance += amount
        self.all_operations.append(
            {
                "Time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"), 
                "Amount": f"+{amount}", 
                "Balance": self.balance
            }
        )
        return self.balance
    
    def take_money(self, amount):
        if self.balance < amount:
            return ("You don't have that sum", self.balance)
        self.balance -= amount
        self.all_operations.append(
            {
                "Time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"), 
                "Amount": f"-{amount}", 
                "Balance": self.balance
            }
        )
        return (None, self.balance)
    
    def get_operations(self):
        return self.all_operations
