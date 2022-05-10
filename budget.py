class Category:
    
    def __init__(self, category_name):
        self.category_name = category_name.capitalize()
        self.ledger = []
        
    def __str__(self):
        l, r, final_format = '', '', ''
        center = (30 - len(self.category_name)) / 2
        
        l = l.ljust(int(center), '*')
        r = r.rjust(int(center), '*')
        
        title = l + self.category_name + r
        
        final_format += title + '\n'
        
        for i in self.ledger:
            if len(i['description']) >= 23:
                description = i['description'][0:23]
            else:
                description = i['description'] 
            
            if len(str(i['amount'])) >= 7:
                amount = str(i['amount'])
                amount = amount[0:7]
            else:
                amount = (str(i['amount']))
                
            ticket = description + str(amount).rjust(30 - len(description), ' ')

            final_format += ticket + '\n'
            
        final_format += 'Total: ' + str(self.get_balance())

        return final_format
    
    def deposit(self, amount, description = ""):
        deposit_info = {
            'amount' : round(amount,2),
            'description' : description,
        }
        
        return self.ledger.append(deposit_info)
    
    def withdraw(self, amount, description = ""):
        withdraw_info = amount
        if not self.check_founds(amount):
            return False
        else:
            amount = float('-' + str(withdraw_info))
            withdraw_info = {
                'amount' : round(amount,2),
                'description' : description,
            }
            self.ledger.append(withdraw_info)
            return True
    
    def get_balance(self):
        self.balance = 0
        for i in self.ledger:
            self.balance += i['amount']
        
        return round(self.balance, 2)
    
    def transfer(self, amount, budget_category):
        a = 'Transfer to ' + budget_category.category_name
        b = 'Transfer from ' + self.category_name
        
        if not self.check_founds(amount) or not budget_category.check_founds(amount):
            return False
        else:
            self.withdraw(amount, a)
            budget_category.deposit(amount, b)
            return True

    def check_founds(self, amount):
       if amount > self.get_balance():
           return False
       else:
           return True

