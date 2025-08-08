class Category:
    def __init__(self, label):
        self.label = label
        self.ledger = []
    
    def __str__(self):
        outp = f'{self.label:*^30}\n'
        ledg_item = ''
        for item in self.ledger:
            p1 = item['description']
            mon = str(item['amount'])
            if (mon.find('.') < 0):
                mon+= '.00'
            if (len(p1) > 23):
                real1 = p1[:23]
                numspace = 7 - len(str(mon))
                for i in range(numspace):
                    real1 += ' '
                real1 += str(mon)
                ledg_item+= real1 + '\n'
            else:
                numspace = 30 - len(str(item['description'])) - len(str(mon))
                for i in range(numspace):
                    p1 += ' '
                p1 += str(mon)
                ledg_item += p1 + '\n'
        outp += ledg_item + 'Total: ' + str(self.get_balance())
        return outp
    
    def deposit(self, amount, description = 'NULL'):
        des = ''
        if description != 'NULL':
            des = description
        self.ledger.append({'amount': amount, 'description': des})

    
    def withdraw(self, amount, description = 'NULL'):
        dec = ''
        if description != 'NULL':
            dec = description
        if self.get_balance() - amount >= 0:
            self.ledger.append({'amount': -1*amount, 'description': dec})
            return True
        return False
        

    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, categ):
        if self.get_balance() - amount >= 0:
            self.ledger.append({'amount': -1*amount, 'description': f'Transfer to {categ.label}'})
            categ.ledger.append({'amount': amount, 'description': f'Transfer from {self.label}'})
            return True
        return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

def create_spend_chart(categories):
    all_at = ''
    top_l = 'Percentage spent by category\n'
    all_at += top_l

    spent = []
    tot_spent = 0
    for category in categories:
        currsum = 0
        for entry in category.ledger:
            if (entry['amount'] < 0):
                currsum += (-1*entry['amount'])
        spent.append(currsum)
        tot_spent+=currsum

    percent = []
    for val in spent:
        r_down = (val * 100 / tot_spent) // 10 * 10
        percent.append(r_down)


    for i in range(100, -1, -10):
        if i == 100:
            all_at+= f'{i}| '
            for ob in percent:
                if (i <= ob):
                    all_at+='o  '
                else:
                    all_at+='   '

        elif i > 0:
            all_at+=f' {i}| '
            for ob in percent:
                if (i <= ob):
                    all_at+='o  '
                else:
                    all_at+='   '

        else:
            all_at+=f'  {i}| '
            for ob in percent:
                if(i <= ob):
                    all_at+='o  '
                else:
                    all_at+='   '

        all_at+= '\n'
        
    all_at+= '    -'
    for category in categories:
        all_at+= '---'
    
    all_at+='\n'
    

    #Now work on labelling each x axis item
    lengths = []
    for i in categories:
        lengths.append(len(i.label))
    for dig in range(max(lengths)):
        all_at+='     '
        for ts in range(len(categories)):
            if dig < len(categories[ts].label):
                all_at+=f'{categories[ts].label[dig:dig+1]}  '
            else:
                all_at+='   '
        if dig < max(lengths) - 1:
            all_at+='\n'   
    return all_at


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.deposit(500, 'sold da supreme hoodie')
clothing.withdraw(238, 'gucci shoes')
print(food)
print(clothing)

print(create_spend_chart([clothing, food]))

** end of main.py **

