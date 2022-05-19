class Category:
    # Init instance
    def __init__(self, category_name):
        self.category_name = category_name.capitalize()
        self.ledger = []
    # Print custom instance
    def __str__(self):
        x, y, info, ticket, description = '', '', '', '', ''
        amount = 0
        center = (30 - len(self.category_name)) / 2
        x = x.ljust(int(center), '*')
        y = y.ljust(int(center), '*')
        
        title = x + self.category_name + y
        for i in self.ledger:
            if len(i['description']) >= 23:
                description = i['description'][0:22]
            else:
                description = i['description']
            if len(str(i['amount'])) >= 7:
                amount = format(i['amount'], '.2f')
                amount = amount[0:7]
            else:
                amount = format(i['amount'], '.2f')
            text = description + str(amount).rjust(30 - len(description), ' ')
            info += text + '\n' 
               
        balance = 'Total: ' + format(self.get_balance(), '.2f')        
        ticket = f'{title}\n{info}{balance}'   
        return ticket
    # deposit method with amount and description
    def deposit(self, amount, description = ''):
        deposit_info = {
            'amount' : amount,
            'description' : description,
            }
        return self.ledger.append(deposit_info)
    # Withdraw method , verify if you have enough money for withdraw
    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False
        else:
            amount = amount * -1
            withdraw_info = {
                'amount' : amount,
                'description' : description,
            }
            self.ledger.append(withdraw_info) 
            return True
    # Get balance method
    def get_balance(self):
        self.balance = 0
        for i in self.ledger:
            self.balance += i['amount']
            
        return self.balance
    # Transfer with verification of funds in object
    def transfer(self, amount, budget_category):
        x = 'Transfer to ' + budget_category.category_name
        y = 'Transfer from ' + self.category_name
        
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, x)
            budget_category.deposit(amount, y)
            return True
    # Check funds method
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
# Category Full OKEY       
        
def create_spend_chart(budget_list):
    # Stating the variables
    withdraws_list = []
    withdraw , deposit, contador, names = 0, 0, 0, 0
    string_porcentage = 100
    porcentage = int
    ticket, column_numbers, columns_names, line, final_name  = '', '', '', '', ''
    
    for i in budget_list:
        # Dinero total de cada categoria
        for x in i.ledger:
            if x['amount'] < 0:
                withdraw += x['amount']
            else:
                deposit += x['amount']
        # Redondeando
        porcentage = (round((withdraw * 100 / deposit) / 10 ) * 10) * -1
        # Lista con nombre y % de lo gastado
        withdraws_list.append({
            'category' : i.category_name,
            'porcentage' : porcentage,
        })    
        
        # Reset the values
        withdraw, deposit = 0, 0
    
    # Generando Ticket
    while string_porcentage >= 0:
        if len(str(string_porcentage)) == 3:
            space = ''
        elif len(str(string_porcentage)) == 2:
            space = ' '
        else:
            space = '  '
        
        # Recorriendo withdraws_list
        for i in withdraws_list:
            # Columna numerica
            if string_porcentage <= i['porcentage']:
                column_numbers += ' o '
            else:
                column_numbers += '   '
        # Formateando el ticket
        ticket += f'{space}{string_porcentage}|{column_numbers}\n'
        string_porcentage -= 10
        # Generando la linea de -
        if string_porcentage == 0:
            line_space = len(column_numbers)
            line = '    ' + line.rjust(line_space, '-') + '\n'
            
            # Which string is larger
            for i in range(0, len(withdraws_list)):
                if i == 0:
                    names = len(withdraws_list[i]['category'])
                if names < len(withdraws_list[i]['category']):
                    names = len(withdraws_list[i]['category'])
                else:
                    names = names
                    
        column_numbers = ''
    # Creando los nombres en vertical
    while names:
        if contador == 0:
            columns_names += '    '
        for i in withdraws_list:
            try:
                columns_names += f" {i['category'][contador]} "
            except:
                columns_names += '   '
        if names == 1:
            columns_names += ' '
        else:
            columns_names += '\n    '
        contador += 1
        names -= 1
        
    ticket += line
    ticket += columns_names
    return print(ticket)
    
    
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


# Me falta 1 espacio