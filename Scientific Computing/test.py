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

def create_spend_chart(budget_list):
    # Declaracion de variables
    withdraws_list = []
    withdraw , deposit, test_two, contador, a, b, testing = 0, 0, 0, 0, 0, 0, 0
    string_porcentage = 100
    porcentage = int
    ticket, generator, category_generator, test = '', '', '', ''
    # Creacion de Gasto total
    for i in budget_list:
        for x in i.ledger:
            if x['amount'] < 0:
                withdraw += x['amount']
            else:
                deposit += x['amount']
        # Redondeado a 0 10 20 30 etc       
        porcentage = (round((withdraw * 100 / deposit)/10)*10) * -1
        # Lista con nombre y % de lo gastado
        withdraws_list.append({
            'category' : i.category_name,
            'porcentage' : porcentage,
        })
        # Reset the variables
        withdraw, deposit = 0, 0
    # Generando el ticket final
    while string_porcentage >= 0:
        for i in withdraws_list:
            # Columna de %
            if string_porcentage <= i['porcentage']:
                generator += ' o '
            else:
                generator += '   '
        ticket += f'{string_porcentage}|{generator}\n'
        string_porcentage -= 10
        
        if string_porcentage == 0:
            test_two = len(generator)
            test = test.rjust(test_two, '-') + '\n'
                # Which string is larger 
            for i in range(0, len(withdraws_list)):
                if i == 0:
                    testing = len(withdraws_list[i]['category'])
                if testing < len(withdraws_list[i]['category']):
                    testing = len(withdraws_list[i]['category'])
                else:
                    testing = testing
        generator = ''
    while testing:
        for i in withdraws_list:
            try:
                category_generator += f" {i['category'][contador]} "
            except:
                category_generator += '   '   
        category_generator += '\n'    
        contador += 1        
        testing-= 1           
         
        
    
    ticket += test
    ticket += category_generator
    

    
    print(ticket)
    return 'Spend Chart'

objeto_uno = Category('Food')
objeto_dos = Category('Transport')
objeto_tres = Category('Entertainment')

objeto_uno.deposit(1005, 'Food')

objeto_uno.withdraw(100, 'Food')


objeto_dos.deposit(1500, 'Food')
objeto_dos.withdraw(1000, 'Food')

objeto_tres.deposit(2000, 'Food')
objeto_tres.withdraw(400, 'Food')

create_spend_chart([objeto_uno, objeto_dos, objeto_tres])

# Falta organizar el codigo mas limpio.
# Ademas de que el codigo sea mas legible.
# Y que quede bien el spend chart