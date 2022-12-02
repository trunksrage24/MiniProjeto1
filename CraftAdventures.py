#projeto realizado por Vitor Daniel e João Carvalho
from collections import defaultdict
#objetivo alcançar 100k em lucros

#classes para cada item:
    #4 espadas
    #3 escudos
    #2 capacetes
    #3 armaduras
    #gems
    #1manto
#cada item pode ser encantado com gems, cada cor gera um efeito em cada item: red attack, green defense e blue speed/invisibility.

class Item:
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
    
    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
class Swords(Item):
    #pelo menos 4 espadas diferentes, 1 iniciante, 1 intermédia e 2 avançadas
    def __init__(self):
        super().__init__("Sword", 0)
    
    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

#espada avançada
class SwordAdva(Swords):
    def __init__(self):
        super().__init__("SwordAdva", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#espada intermédia
class SwordInter(Swords):
    def __init__(self):
        super().__init__("SwordInter", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#espada iniciante
class SwordIni(Swords):
    def __init__(self):
        super().__init__("SwordIni", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

class Shields(Item):
    #pelo menos 3 shields, begginer, intermediate e advanced
    def __init__(self):
        super().__init__("Shield", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
#escudo iniciante
class ShieldIni(Shields):
    def __init__(self):
        super().__init__("ShieldIni", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#escudo intermedio
class ShieldInter(Shields):
    def __init__(self):
        super().__init__("ShieldInter", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#escudo avançado
class ShieldAdva(Shields):
    def __init__(self):
        super().__init__("ShieldAdva", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

class Armors(Item):
    # 3 helmets, 3 chestplates, 3 leggings e 3 shoes
    def __init__(self):
        super().__init__("Armors", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
class Helmet(Armors):
    def __init__(self):
        super().__init__("Helmet", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
#helmet iniciante
class HelmetIni(Helmet):
    def __init__(self):
        super().__init__("HelmetIni", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#helmet intermédio
class HelmetInter(Helmet):
    def __init__(self):
        super().__init__("HelmetInter", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#helmet avançado
class HelmetAdva(Helmet):
    def __init__(self):
        super().__init__("HelmetAdva", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

class BodyArmor(Armors):
    def __init__(self):
        super().__init__("BodyArmor", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
#armadura corpo iniciante
class ChestplatelIni(BodyArmor):
    def __init__(self):
        super().__init__("ChestplatelIni", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#armadura corpo intermédia
class ChestplateInter(BodyArmor):
    def __init__(self):
        super().__init__("ChestplateInter", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#armadura corpo avançada
class ChestplateAdva(BodyArmor):
    def __init__(self):
        super().__init__("ChestplateAdva", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

class Leggins(Armors):
    def __init__(self):
        super().__init__("Leggins", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
#leggins iniciante
class LegginsIni(Leggins):
    def __init__(self):
        super().__init__("LegginsIni", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#leggins intermedio
class LegginsInter(Leggins):
    def __init__(self):
        super().__init__("LegginsInter", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#leggins avançado
class LegginsAdva(Leggins):
    def __init__(self):
        super().__init__("LegginsAdva", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

class Shoes(Armors):
    def __init__(self):
        super().__init__("Shoes", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

#shoes iniciante
class ShoesIni(Shoes):
    def __init__(self):
        super().__init__("ShoesIni", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()


#shoes intermedio
class ShoesInter(Shoes):
    def __init__(self):
        super().__init__("ShoesInter", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#shoes avançado
class ShoesAdva(Shoes):
    def __init__(self):
        super().__init__("ShoesAdva", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

class Bow(Item):
    def __init__(self):
        super().__init__("Bow", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

#bow iniciante
class BowIni(Bow):
    def __init__(self):
        super().__init__("BowIni", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#bow intermedio
class BowInter(Bow):
    def __init__(self):
        super().__init__("BowInter", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#bow avançado
class BowAdva(Bow):
    def __init__(self):
        super().__init__("BowAdva", 10000)
        print(self.name + str(self.gold))
    def Display(self):
        return super().Display()

#arrows
class Arrows(Item):
    def __init__(self):
        super().__init__("Bow", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

InventoryToSell = [SwordIni, SwordInter, SwordAdva, ShieldIni, ShieldInter, ShieldAdva, ChestplatelIni, 
                    ChestplateInter, ChestplateAdva, HelmetIni, HelmetInter, HelmetAdva, LegginsIni, LegginsInter, 
                    LegginsAdva, ShoesIni, ShoesInter, ShoesAdva, BowIni, BowInter, BowAdva, Arrows]


TotalReceitas=0
Resources = {
    "wood" : 5,
    "leather" : 5,
    "iron" : 5,
    "gold" : 0  
}

ResourcesPrice = {
    "wood" : 1,
    "leather" : 2,
    "iron" : 4,
    "gold" : 10
}

Recipes= {

    "SwordIni" : "You need: 1 wood",
    "SwordInter" : "You need: 1 wood and 1 leather",
    "SwordAdva" : "You need: 2 wood and 3 iron",

    "ShieldIni" : "You need: 1 wood",
    "ShieldInter" : "You need: 1 wood and 1 leather",
    "ShieldAdva" : "You need: 2 wood and 3 iron",

    "HelmetIni" : "You need: 1 leather",
    "HelmetInter" : "You need: 1 iron and 1 leather",
    "HelmetAdva" : "You need: 3 iron",

    "ChestplatelIni" : "You need: 1 leather",
    "ChestplateInter" : "You need: 2 iron and 2 leather",
    "ChestplateAdva" : "You need: 4 iron and 3 leather",
    
    "LegginsIni" : "You need: 2 leather",
    "LegginsInter" : "You need: 2 iron and 2 leather",
    "LegginsAdva" : "You need: 3 iron and 3 leather",

    "ShoesIni" : "You need: 1 leather",
    "ShoesInter" : "You need: 1 iron and 2 leather",
    "ShoesAdva" : "You need: 3 iron and 2 leather",

    "BowIni" : "You need: 1 wood and 1 leather",
    "BowInter" : "You need: 2 wood and 1 iron and 1 leather",
    "BowAdva" : "You need: 3 iron and 1 leather",
    
    "Arrows" : "You need: 3 wood and 1 iron"


}

        
Level=0
day=1
print("Day "+str(day))
print("Level "+str(Level))
print("Money: "+str(Resources["gold"]))
print("Total Recipes: "+str(TotalReceitas))
print("Wood: "+str(Resources["wood"]))
print("Iron: "+str(Resources["wood"]))
print("Leather: "+str(Resources["leather"]))


def buyresources():
    
    print("Buy Resources")
    aux=True
    while aux:
        n1=input("Do you wish to buy Wood(1),Leather(2), Iron(3) Or leave(4)?")
        if n1=="1":
            n2=input("How much Wood do you wish to buy? ")
            n2=n2*int(ResourcesPrice["wood"])
            print("Total paid: "+str(n2))

        elif n1=="2":
            n2=input("How much Leather do you wish to buy? ")
            ResourcesPrice=defaultdict(int)
           # for value in ResourcesPrice:
            ResourcesPrice["leather"] *= n2
                #n4=n2*ResourcesPrice[value]
            print("Total paid: "+str(ResourcesPrice["leather"]))
            
        elif n1=="3":   
            n2=input("How much Iron do you wish to buy? ")
            n2=n2*ResourcesPrice["iron"]
            print("Total paid: "+str(n2))
        elif n1=="4":
            aux=False
    
buyresources()
     




