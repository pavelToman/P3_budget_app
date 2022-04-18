class Category:
    spentt = [0]
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.tot = 0
        self.spent = 0

    def __repr__(self):
        a = self.name
        a_l = len(a)
        a_l1 = (30-a_l)//2
        n = a_l1
        row1 = ("*"*n)+str(self.name)+("*"*n)
        if len(row1)<30:
            row1 += "*"
        row = f""
        for i in self.ledger:
            b = i["description"]
            if len(b)>23:
                b = b[:23]
            elif len(b)<23:
                p = 23 - len(b)
                b += p*" "
            c = i["amount"]
            c = float(c)
            c = round(c, 2)
            c = format(c,'.2f')
            c1 = len(str(c))
            if c1 < 7:
                c2 = 7-c1
                c3 = str(c2*" ")
                row += f"{b}{c3}{c}\n"
            elif c1 == 7:
                row += f"{b}{c}\n"
            else:
                c = str(c)
                c = c[:7]
                row += f"{b}{c}\n"
        d = self.tot
        d = float(d)
        d = round(d, 2)
        d = format(d, ".2f")
        frow = f"Total: {str(d)}"
        return f"{row1}\n{row}{frow}"
    
    def deposit(self, amount, description=""):
        self.tot += amount
        self.ledger.append({"amount": amount, "description": description})
           
    def withdraw(self, amount, description=""):
        global spentt
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -(amount), "description": description})
            self.tot -= amount
            self.spentt[0] += amount
            self.spent += amount

            return True
        else:
            return False
      
    def get_balance(self):
        return self.tot
    
    def transfer(self, amount, kam):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {kam.name}")
            kam.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    def check_funds(self, amount):
        if amount > self.tot:
            return False
        else:
            return True  

def create_spend_chart(lis):
    listik = list()
    for g in lis:
        listik.append(g.name)
    char = ""
    nad = "Percentage spent by category"
    pd = "    -"
    text_d = dict()
    td = ""
    delka = 0
    for i,j in enumerate(listik):
        pd += "---"
        k = len(j)
        if k>delka:
            delka = k
        text_d[i]=list(j)
    for i in range(delka):
        td += " "*5
        for j,k in enumerate(listik):
            try:
                td += text_d[j][i]+"  "
            except:
                td += "   "
        if i < (delka-1):
            td += "\n"
    tn = ""
    tndict = dict()
    for i,j in enumerate(lis):
        a = j.spent // (j.spentt[0]/10)
        print(a)
        a = int(a)
        print(a)
        tndict[i]=[]
        for k in range(a+1):
            tndict[i].append(k)
    tn += "100| "
    for i, j in enumerate(lis):
        if 10 in tndict[i]:
            tn += "o  "
        else:
            tn += "   "
    tn += "\n"
    for i in reversed(range(10,100,10)):
        tn += f" {i}| "
        for x,y in enumerate(lis):
            if (i/10) in tndict[x]:
                tn+="o  "
            else:
                tn+="   "
        tn+="\n"
    tn += "  0| "
    for i in lis:
        tn+="o  "
    char = f"{nad}\n{tn}\n{pd}\n{td}"
    return char
        
food = Category("Food")
food.deposit(900, "cash")
food.withdraw(105.55, "chocolate, late, coffe, pan, flowers, cheese")
food.get_balance
print(food.tot)
print(food.ledger)