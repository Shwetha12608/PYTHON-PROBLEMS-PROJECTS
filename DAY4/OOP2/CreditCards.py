class VISACard:
    def __init__(self,name,Cnumber):
        self.name=name
        self.Cnumber=Cnumber
    
    def display_details(self):
        print(self.name)
        print(self.Cnumber)
    # DESCOUNT METHOD
    def compute_discount(self,amount):
        discount=amount*0.01
        print(float(discount))

# LETS CREATE THE CHILD CLASS

class HPVISACard(VISACard):
    def compute_discount(self,amount,purchase_type):
        discount=amount*0.01
        if purchase_type=="Fuel":
            discount+=10
        print(float(discount))

# //MAIN()
card_type=input("Enter the card type (Regular/HP): ")
name=input("Enter the card holder name: ")
Cnumber=input("Enter the card number: ")
amount=float(input("Enter the purchase amount: "))

if card_type=="VISA":
    card=VISACard(name,Cnumber)
    card.display_details()
    card.compute_discount(amount)

elif card_type=="HP":
    purchase_type=input("Enter the purchase type (Fuel/Other): ")
    card=HPVISACard(name,Cnumber)
    card.display_details()
    card.compute_discount(amount,purchase_type)
        




