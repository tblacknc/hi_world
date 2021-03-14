
class Category:

    def __init__(self, name):
        self.name=name
        self.ledger = list()
        #self.ledger = {}
        
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in self.ledger:
            x = i["amount"]
            y = i["description"]
            items += f"{y[0:23]:23}"+ f"{x:>7.2f}" + '\n'
            total = total + x
        output = title + items + "Total: " + str(f"{total:>7.2f}")
        return output

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": round(float(amount),2), "description": description})
        return True
        
    def withdraw(self, withd, text=''):
        if self.get_balance() > withd:
            self.ledger.append({"amount": -round(float(withd),2), "description": text})
            return True
        else:
            return False
        
    def get_balance(self):
        sum = 0
        for record in self.ledger:  
            x = record["amount"]
            x = float(x)
            x = (f"{x:>7.2f}")
            sum = float(sum) + float(x)
        return sum
       
    def transfer(self, amount, bucket):
        if self.check_funds(amount):
            txt = 'Transfer to {}'
            string = txt.format(bucket.name)
            self.deposit("-"+str(amount), string) 

            txt = 'Transfer from {}'
            string = txt.format(self.name)
            bucket.deposit(str(amount), string)
            
            return True
        else:
            return False
        
    def check_funds (self, amount):

        if self.get_balance() >= amount:
            return True
        else:
            #print("self.get_balance = ",self.get_balance())
            return False
            
    def get_withdrawls(self):
        sum = 0
        
        for record in self.ledger:  
            x = record["amount"]
            x = float(x)
            x = (f"{x:>7.2f}")
            #print("x = " + x)
            if float(x) < 0 :
                sum = float(sum) + float(x)
        return sum
        

def create_spend_chart(categories):
    res = "Percentage spent by category\n"

    
    dashes = "-" + "---"*len(categories)

    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = '     '
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        nameStr += '\n'
        x_axis += nameStr

    res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res
    
    
business = Category("Business")      
business.deposit(900, "deposit")

entertainment = Category("entertainment")
entertainment.deposit(900, "deposit")


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.90, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food.get_balance())
print(food.withdraw(855.00))
print(food.get_balance())
print(food.transfer(22,business))
print(food.get_balance())

print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))

print(create_spend_chart([business, food, entertainment]))
#clothing.create_spend_chart([self.business, self.food, self.entertainment])
#create_spend_chart(["food", "clothing", "auto"])
#create_spend_chart("auto", "food")
#print(clothing.get_balance())
#print(food.get_balance())

#print(food.get_withd())
#{'amount': 45.56, 'description': ''}
#{'amount': 45.56, 'description': ''}
""" 
food = Category("food")
entertainment = Category("Entertainment")
business = Category("Business")    
  
business.deposit(900, "deposit")
  
food.deposit(900, "deposit")
food.deposit(45.56)
#food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#food.withdraw(45.67)
print(food.get_balance())
print(food.withdraw(855.00))
print(food.get_balance())
print(food.transfer(22,business))
print(food.get_balance())
print(business.get_balance())

print(food)
"""
