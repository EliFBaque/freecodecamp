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
    all_objects_withdraws = []
    string_porcentage = 100
    final_porcentage = int
    object_withdraw = 0
    object_deposit = 0
    category_generator = ''
    contador = 0
    # recorrer la lista de objectos y luego sacar los amounts
    for i in budget_list:
        # cada objecto de la lista
        for x in i.ledger:
            # Entrando a los datos del ledger
            if x['amount'] < 0:
                object_withdraw += x['amount']
            else:
                object_deposit += x['amount']
        
            
        final_porcentage = (round((object_withdraw * 100 / object_deposit)/10)*10) * -1 # porcentaje de gastos.
        all_objects_withdraws.append({
            'category' : i.category_name,
            'porcentage' : final_porcentage,
        })
        object_withdraw = 0
        object_deposit = 0
    ticket = ''
    string_yes = ''
    while string_porcentage >= 0:
        for i in all_objects_withdraws:
            if string_porcentage <= i['porcentage']:
                string_yes += ' o '
            else:
                string_yes += '   '
            print(string_yes)
            
        for i in all_objects_withdraws:
            for x in i['category']:
                category_generator += x + '\n'
            print(category_generator)
        ticket += f'{string_porcentage}| {string_yes}\n'
        print(ticket)
        string_porcentage -= 10 
        if string_porcentage == 0:
            # Hacer la linea
            # Un for para los nombres de cada categoria  
            return
        string_yes = ''
        
    
            
    # crear el grafico 
    

    return print(all_objects_withdraws)
    # hacer un for y verificar que el primer digito sea un -
    # rounded = round(number/10)*10 rondea a numero mas cerca del 0 osea 10 20 30 etc
    # usar get balance y sumarle lo del withdraw para sacar el % de gastos
    
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


