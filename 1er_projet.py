class Utilisateur():
    def __init__(self,name,age,portfolio):
        self.name=name
        self.age=age
        self.portfolio=portfolio
        self.inventary=[]

    def depot(self):

        depot=int(input("entrez le montant a deposer : "))
        self.portfolio+= depot 
        print(f"votre nouveau solde est {self.portfolio}")

        
    def retrait(self):
        retrait= int(input("entrez le montant a retirer"))
        self.portfolio-= retrait 
        print("votre nouveau solde est " +self.portfolio)
        

    
class Products:
    def __init__(self,name,price):
        self.name=name
        self.price=price


productName=["telephone","habits","ordinateur"]
product=[Products(productName[0],800),
         Products(productName[1],50),
         Products(productName[2],2000)
         ]

def userlogin(Utilisateur):
    while True :
        try:
            name=input("entrez votre nom : ")
            age=int(input("entrez votre age : "))
            portfolio=int(input("entrez la somme a deposer : "))
            return Utilisateur(name, age, portfolio)
            break
        except ValueError:
            print("entrez un nombre pour l'age et pour le solde")
        

def buy(user,product):
     b = True 
     while b:
        try:
            name=input("quel est le nom de l'article que vous desirez obtenir ? :")
            for items in product:
                if items.name ==name and user.portfolio>=items.price:
                    user.portfolio=user.portfolio -items.price
                    user.inventary.append(name)
                    print(f"votre nouveau solde est de {user.portfolio}")
                    print(user.inventary)
                    a=input("voulez vous continuer ou arretez le programme ? entrez non pour continuer et oui pour arreter. ")
                    if a == "oui":
                        b=False
                elif items.name ==name and user.portfolio<items.price:
                    print("votre solde est inssufisant.")
                    user.depot()
                    
        except:
            print("")





user=userlogin(Utilisateur)
buy(user,product)

