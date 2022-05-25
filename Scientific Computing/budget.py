class Category:
    '''A Class with diferent methods to make a movement of money'''
    def __init__(self, categoryName):
        '''Inital instance'''
        self.categoryName = categoryName.capitalize()
        self.ledger = []
        
    def __str__(self):
        '''Custom print of each Category class'''
        rightTitle, leftTitle, info, ticket, description = '', '', '', '', ''
        amount = 0
        
        centerOfTitle = (30 - len(self.categoryName)) / 2
        
        rightTitle = rightTitle.ljust(int(centerOfTitle), '*')
        leftTitle = leftTitle.ljust(int(centerOfTitle), '*')
        
        title = rightTitle + self.categoryName + leftTitle
        
        # Loop through each item in the ledger
        for i in self.ledger:
            if len(i['description']) >= 23:
                description = i['description'][0:23]
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
    
    def deposit(self, amount, description=''):
        '''Make a deposit'''
        deposit_info = {
            'amount': amount,
            'description': description,
        }
        return self.ledger.append(deposit_info)
    
    def withdraw(self, amount, description=''):
        '''Make a withdraw and verify if you have enough money for it'''
        if not self.check_funds(amount):
            return False
        else:
            amount = amount * -1
            withdraw_info = {
                'amount': amount,
                'description': description,
            }
            self.ledger.append(withdraw_info)
            return True
    
    def get_balance(self):
        '''Get the total balance of the category'''
        self.balance = 0
        for i in self.ledger:
            self.balance += i['amount']
        
        return self.balance
    
    def transfer(self, amount, budget_category):
        '''Verify and make a transaction if you have enough funds to it'''
        transferTo = 'Transfer to ' + budget_category.categoryName
        transferFrom = 'Transfer from ' + self.categoryName
        
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, transferTo)
            budget_category.deposit(amount, transferFrom)
            return True
        
    def check_funds(self, amount):
        '''Check if you have enough funds to make a transfer or withdraw'''
        if amount > self.get_balance():
            return False
        else:
            return True
        
def create_spend_chart(budget_list):
    '''Make a spend chart with the withdraws of each category'''
    chart = 'Percentage spent by category\n'
    withdraws_list, percentageList, namesList  = [], [], [] 
    withdraw , counter, namesLen, totalWithdraws = 0, 0, 0, 0
    roundedPercentage = int 
    counterPercentage = 100 
    percentageFormat, namesFormat = ' ', ' ' 
    dividerLine, namesFinalFormat, percentageFinalFormat, lineLen = '', '', '', '' 
    namesColumn = '    ' 
    
    for i in budget_list:
        percentageFormat += '{}  '
        namesFormat += '{}  '

        for x in i.ledger:
            if x['amount'] < 0:
                withdraw += x['amount']
        print(withdraw)
        totalWithdraws += withdraw * - 1
        #Reset values
        withdraws_list.append({
            'category': i.categoryName,
            'withdraw': withdraw * - 1,
            'percentage': 0,
        })
        withdraw = 0
    for i in withdraws_list:
        notRound = int(i['withdraw'] * 100 / totalWithdraws)
        roundedPercentage = round(notRound / 10) * 10
        if (roundedPercentage > notRound):
            roundedPercentage -= 10
            
        i.update({'percentage' : roundedPercentage})
        
    percentageFormat += '\n'
    while counterPercentage >= 0:
        
        if len(str(counterPercentage)) == 3:
            percentageSpace = ''
        elif len(str(counterPercentage)) == 2:
            percentageSpace = ' '
        else:
            percentageSpace = '  '
        
        #Matching the percentage of the withdraws with counterPercentage
        for i in withdraws_list:
            if counterPercentage <= i['percentage']:
                percentageList.append('o')
            else:
                percentageList.append(' ')
            
        percentageFinalFormat = percentageFormat.format(*percentageList)
        chart += f'{percentageSpace}{counterPercentage}|{percentageFinalFormat}'
        percentageList = []
        counterPercentage -= 10
        
        if counterPercentage == 0:
           lineLen = len(percentageFinalFormat) - 1
           dividerLine = dividerLine.rjust(lineLen, '-') 
    chart += '    ' + dividerLine + '\n'
    
    for i in range(0, len(withdraws_list)):
        if i == 0:
            namesLen = len(withdraws_list[i]['category'])
        if namesLen < len(withdraws_list[i]['category']):
            namesLen = len(withdraws_list[i]['category'])
        else:
            namesLen = namesLen
    
    while namesLen:
        for i in withdraws_list:
            try:
                namesList.append(i['category'][counter])
            except:
                namesList.append(' ')
            
        if namesLen != 1:
            namesFinalFormat = namesFormat.format(*namesList)
            chart += f'{namesColumn}{namesFinalFormat}\n'
        else:
            namesFinalFormat = namesFormat.format(*namesList)
            chart += f'{namesColumn}{namesFinalFormat}'
        
        namesFinalFormat = ''
        counter += 1
        namesList = []
        namesLen -= 1
        
    return print(chart)
    
food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

create_spend_chart([business, food, entertainment])

# Finalizado Todo Correcto