#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

class Category:

    def __init__(self, name):
        self.name=name
        self.ledger = list()
        
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in self.ledger:
            x = i["amount"]
            y = i["description"]
            items += f"{y[0:23]:23}"+ f"{x:>7.2f}" + '\n'
            total = total + x
        output = title + items + "Total:" + str(f"{total:>7.2f}")
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
            return False
            
    def get_withdrawls(self):
        sum = 0
        
        for record in self.ledger:  
            x = record["amount"]
            x = float(x)
            x = (f"{x:>7.2f}")
            if float(x) < 0 :
                sum = float(sum) + float(x)
        return sum

def create_spend_chart(categories):

    total = 0
    subtotal = 0
    percent = dict()
    names = []

    for categ in categories:
        subtotal = categ.get_withdrawls()
        total = total + subtotal

    for categ in categories:
        subtotal = categ.get_withdrawls()
        percent[categ] = int(((subtotal / total) * 100)-10)


    rows = 10
    outp = "Percentage spent by category\n" 
    while rows >= 0:
        x = str(rows * 10)  + "|"
        outp = outp + f"{x:>4}"
        rows -= 1
        for category in categories:
            if percent[category] >= rows * 10:
                outp = outp + " o "
            else:
                outp = outp + "   "
        outp = outp + " \n"
    a = ""

    x = 0
    for category in categories:
        names.append(category.name)
        x += 1

    res = max(len(ele) for ele in names) 
        
    outp += '    -' + '---'*x + '\n'
        
    for x in range(res):
        outp = outp + "     "
        for name in names:
            try:
                outp = outp + (name[x])+"  "
            except:
                outp = outp + "   "
        outp = outp + "\n"

    outp = outp.rstrip()
    outp = outp + "  "

    return (outp)


food = Category("Food")
business = Category("business")
business.deposit(1000, "initial deposit")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.90, "restaurant and more food for dessert")
food.withdraw(10.15, "groceries")
food.withdraw(15.90, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
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
auto.withdraw(950)
auto.deposit(1000, "initial deposit")
auto.withdraw(950)

print(food)
print(clothing)
print(create_spend_chart([food,  auto]))
print(food.get_withdrawls())
print(clothing.get_withdrawls())
print(auto.get_withdrawls())
print(create_spend_chart([food, clothing, auto]))
