#projeto realizado por Vitor Daniel e João Carvalho
  #import colorama
  #from colorama import Fore
import random  
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



Resources = {
    "wood" : 5,
    "leather" : 5,
    "iron" : 5,
    "gold" : 0  
}

ResourcesPrice = {
    "wood" : 25,
    "leather" : 35,
    "iron" : 90,
    "gold" : 180

}

Recipes= {
    #Em comentario estão os preços totais do item em questão(ex:1wood->25$ + 1 leather->35$=60$)
    "SwordIni" : "You need: 1 wood and 1 leather.", #60
    "SwordInter" : "You need: 1 wood, 2 leathers and 3 irons.", #365 
    "SwordAdva" : "You need: 4 irons and 2 golds,", #720

    "ShieldIni" : "You need: 1 wood and 1 leather.", #60
    "ShieldInter" : "You need: 1 wood, 2 leathers and 2 irons.", #275
    "ShieldAdva" : "You need: 2 leather, 3 irons and 1 gold.", #520

    "HelmetIni" : "You need: 1 leather and 1 iron.", #125
    "HelmetInter" : "You need: 2 leathers and 3 irons.", #340
    "HelmetAdva" : "You need: 3 leathers, 3 irons and 2 golds.", #1 095

    "ChestplatelIni" : "You need: 2 leather and 1 iron.", #160
    "ChestplateInter" : "You need: 3 leathers and 2 irons.", #285
    "ChestplateAdva" : "You need: 4 leathers, 3 irons and 4 golds.", #1 130
    
    "LegginsIni" : "You need: 2 leather and 1 iron.", #190
    "LegginsInter" : "You need: 3 leathers and 3 irons.", #375
    "LegginsAdva" : "You need: 4 leathers, 2 irons and 3 golds.", #860

    "ShoesIni" : "You need: 1 leather and 1 iron.", #125
    "ShoesInter" : "You need: 2 leathers and 2 irons.", #250
    "ShoesAdva" : "You need: 3 leathers, 3 irons and 1 gold.", #555

    "BowIni" : "You need: 1 wood and 1 leather.", #60
    "BowInter" : "You need: 2 wood,1 leather and 2 iron.", #265
    "BowAdva" : "You need: 1 leather and 3 irons and 2 golds.", #665
    
    "Arrows" : "You need: 3 wood and 1 iron" # 165


}

TotalReceitas=0        
Level=1
money=1500
day=1
SuccessRating=5
print("Day "+str(day))
print("Level "+str(Level))
print("Money: "+str(money))
print("Total Recipes: "+str(TotalReceitas))
print("Wood: "+str(Resources["wood"]))
print("Leather: "+str(Resources["leather"]))
print("Iron: "+str(Resources["iron"]))
print("gold: "+str(Resources["gold"]))

def buyresourcesAndRecipes():
    
    print("Buy Resources/Recipes")
    aux=True
    while aux:
        n1=input("Do you wish to buy Wood(1) for "+str(ResourcesPrice["wood"])+"$,Leather(2)"+str(ResourcesPrice["leather"])+"$, Iron(3)"+str(ResourcesPrice["iron"])+"$, Gold(4)"+str(ResourcesPrice["gold"])+"$,Recipes(5) or leave(6)? ")
        if n1=="1":
            n2=int(input("How much Wood do you wish to buy for "+str(ResourcesPrice["wood"])+"$? "))
            n2=n2*int(ResourcesPrice["wood"])
            print("Total paid: "+str(n2))

        elif n1=="2":
            n2=int(input("How much Leather do you wish to buy for "+str(ResourcesPrice["leather"])+"$? "))
            n2=n2*int(ResourcesPrice["leather"])
            print("Total paid: "+str(n2))
            
        elif n1=="3":   
            n2=int(input("How much Iron do you wish to buy for "+str(ResourcesPrice["iron"])+"$? "))
            n2=n2*ResourcesPrice["iron"]
            print("Total paid: "+str(n2))
        elif n1=="4":   
            n2=int(input("How much Gold do you wish to buy for "+str(ResourcesPrice["gold"])+"$? "))
            n2=n2*ResourcesPrice["gold"]
            print("Total paid: "+str(n2))
        elif n1=="5":
            print("Here recipes") 
            #puxar recipes aqui   
        elif n1=="6":
            aux=False
buyresourcesAndRecipes()

def crafting():
    print("Crafting Time!!")
    randnum=random.randint(1,10)
    craftingattempt=Level*randnum
    if craftingattempt >= SuccessRating:
        print("Done and Done!!! "+str(craftingattempt))
        #remover os items do inventario
        #dar exp ao jogador
    elif craftingattempt < SuccessRating:  
        print("Not Done! "+str(craftingattempt)) 
        #remover os items do inventario

crafting()
