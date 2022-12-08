#projeto realizado por Vitor Daniel e João Carvalho

import random  


#objetivo alcançar 100k em lucros

#classes para cada item:
    #3 espadas
    #3 escudos
    #3 capacetes
    #3 armaduras
    #3 leggins
    #3 sapatos

#add amount variable in all class
class Item:
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
    
    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

class Player:
    name=""
    totalgold=5000
    exp=0
    level=1

class Swords(Item):
    #3 espadas
    def __init__(self):
        super().__init__("Sword", 0)
    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

#espada avançada
class SwordAdva(Swords):
    iron=4
    gold=2
    SuccessRating=10
    def __init__(self,iron,gold,SuccessRating):

        super().__init__("SwordAdva", 10000)
        print(self.name + str(self.gold))
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#espada intermédia
class SwordInter(Swords):
    wood=1
    leather=2
    iron=3
    SuccessRating=10
    def __init__(self,wood,leather,iron,SuccessRating):
        super().__init__("SwordInter", 10000)
        print(self.name + str(self.gold))
        self.wood=wood
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#espada iniciante
class SwordIni(Swords):
    wood=1
    leather=1
    SuccessRating=3
    def __init__(self,wood,leather,SuccessRating):
        super().__init__("SwordIni", 10000)
        print(self.name + str(self.gold))
        self.wood=wood
        self.leather=leather
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()
        

class Shields(Item):
    #3 shields
    def __init__(self):
        super().__init__("Shield", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
#escudo iniciante
class ShieldIni(Shields):
    wood=1
    leather=1
    SuccessRating=10
    def __init__(self,wood,leather,SuccessRating):
        super().__init__("ShieldIni", 10000)
        print(self.name + str(self.gold))
        self.wood=wood
        self.leather=leather
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()
        print("wood needed: "+str(self.wood)+" , "+str(self.leather)+" leather")

#escudo intermedio
class ShieldInter(Shields):
    wood=1
    leather=2
    iron=2
    SuccessRating=10
    def __init__(self,wood,leather,iron,SuccessRating):
        super().__init__("ShieldInter", 10000)
        print(self.name + str(self.gold))
        self.wood=wood
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()
        print("wood needed: "+str(self.wood)+" , "+str(self.leather)+" leather"+str(self.iron)+" iron")

#escudo avançado
class ShieldAdva(Shields):
    leather=2
    iron=3
    gold=1
    SuccessRating=15
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("ShieldAdva", 10000)
        print(self.name + str(self.gold))
        self.gold=gold
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()
        print("wood needed"+str(self.leather)+" leather"+str(self.iron)+" iron")

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
    leather=1
    iron=1
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("ShieldInter", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()
        print(str(self.leather)+" leather"+str(self.iron)+" iron")

#helmet intermédio
class HelmetInter(Helmet):
    leather=2
    iron=3
    SuccessRating=10
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("HelmetInter", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#helmet avançado
class HelmetAdva(Helmet):
    leather=3
    iron=3
    gold=2
    SuccessRating=10
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("HelmetAdva", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

class BodyArmor(Armors):
    def __init__(self):
        super().__init__("BodyArmor", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
#armadura corpo iniciante
class ChestplatelIni(BodyArmor):
    leather=2
    iron=1
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("ChestplateIni", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#armadura corpo intermédia
class ChestplateInter(BodyArmor):
    leather=3
    iron=2
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("ChestplateInter", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#armadura corpo avançada
class ChestplateAdva(BodyArmor):
    leather=4
    iron=3
    gold=4
    SuccessRating=10
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("ChestplateAdva", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

class Leggins(Armors):
    def __init__(self):
        super().__init__("Leggins", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
#leggins iniciante
class LegginsIni(Leggins):
    leather=2
    iron=1
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("LegginsIni", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#leggins intermedio
class LegginsInter(Leggins):
    leather=3
    iron=3
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("LegginsInt", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#leggins avançado
class LegginsAdva(Leggins):
    leather=4
    iron=2
    gold=3
    SuccessRating=10
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("HelmetInter", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

class Shoes(Armors):
    def __init__(self):
        super().__init__("Shoes", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

#shoes iniciante
class ShoesIni(Shoes):
    leather=1
    iron=1
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("ShoesIni", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()


#shoes intermedio
class ShoesInter(Shoes):
    leather=2
    iron=2
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("ShoesInter", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#shoes avançado
class ShoesAdva(Shoes):
    leather=3
    iron=3
    gold=1
    SuccessRating=10
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("ShoesAdva", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

class Bow(Item):
    def __init__(self):
        super().__init__("Bow", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

#bow iniciante
class BowIni(Bow):
    leather=1
    wood=1
    SuccessRating=10
    def __init__(self,leather,SuccessRating):
        super().__init__("BowIni", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#bow intermedio
class BowInter(Bow):
    leather=1
    wood=2
    iron=2
    SuccessRating=10
    def __init__(self,leather,iron,SuccessRating):
        super().__init__("BowInt", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#bow avançado
class BowAdva(Bow):
    leather=3
    iron=3
    gold=1
    SuccessRating=10
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("BowAdva", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#arrows
class Arrows(Bow):
    wood=3
    iron=1
    SuccessRating=10
    def __init__(self,wood,iron,SuccessRating):
        super().__init__("HelmetInter", 10000)
        print(self.name + str(self.gold))
        self.wood=wood
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

InventoryToSell = [SwordIni, SwordInter, SwordAdva, ShieldIni, ShieldInter, ShieldAdva, HelmetIni, HelmetInter, HelmetAdva, 
                    ChestplatelIni, ChestplateInter, ChestplateAdva, LegginsIni, LegginsInter, 
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



day=1

print("Day "+str(day))
print("Level "+str(Player.level))
print("EXP "+str(Player.exp))
print("Money: "+str(Player.totalgold))
print("Total Recipes: "+str(TotalReceitas))

def BuyResourceRecipes():
    print("Buy Resources/Recipes")
    aux=True
    while aux:
        print("Wood: "+str(Resources["wood"]))
        print("Leather: "+str(Resources["leather"]))
        print("Iron: "+str(Resources["iron"]))
        print("gold: "+str(Resources["gold"]))
        n1=input("Do you wish to buy Wood(1) for "+str(ResourcesPrice["wood"])+"$,Leather(2)"+str(ResourcesPrice["leather"])+"$, Iron(3)"+str(ResourcesPrice["iron"])+"$, Gold(4)"+str(ResourcesPrice["gold"])+"$,Recipes(5) or leave(6)? ")
        if n1=="1":
            ResourcesAmount=int(input("How much Wood do you wish to buy for "+str(ResourcesPrice["wood"])+"$? "))   
            ResourcesQuantity=ResourcesAmount
            ResourcesAmount=ResourcesAmount*int(ResourcesPrice["wood"])
            if Player.totalgold>=ResourcesAmount:
                    print("Total paid: "+str(ResourcesAmount))
                    Player.totalgold=Player.totalgold-ResourcesAmount
                    print("Current Gold:"+str(Player.totalgold))
                    Resources["wood"]=Resources["wood"]+ResourcesQuantity
            elif Player.totalgold<ResourcesAmount:
                    print("You dont have enought gold to buy this product!")


        elif n1=="2":
            ResourcesAmount=int(input("How much Leather do you wish to buy for "+str(ResourcesPrice["leather"])+"$? "))
            ResourcesQuantity=ResourcesAmount
            ResourcesAmount=ResourcesAmount*int(ResourcesPrice["leather"])
            if Player.totalgold>=ResourcesAmount:
                print("Total paid: "+str(ResourcesAmount))
                Player.totalgold=Player.totalgold-ResourcesAmount
                print("Current Gold:"+str(Player.totalgold))
                Resources["leather"]=Resources["leather"]+ResourcesQuantity
            elif Player.totalgold<ResourcesAmount:
                    print("You dont have enought gold to buy this product!")    
            
        elif n1=="3":   
            ResourcesAmount=int(input("How much Iron do you wish to buy for "+str(ResourcesPrice["iron"])+"$? "))
            ResourcesQuantity=ResourcesAmount
            ResourcesAmount=ResourcesAmount*ResourcesPrice["iron"]
            if Player.totalgold>=ResourcesAmount:
                print("Total paid: "+str(ResourcesAmount))
                Player.totalgold=Player.totalgold-ResourcesAmount
                print("Current Gold:"+str(Player.totalgold))
                Resources["iron"]=Resources["iron"]+ResourcesQuantity
            elif Player.totalgold<ResourcesAmount:
                    print("You dont have enought gold to buy this product!")    

        elif n1=="4":   
            ResourcesAmount=int(input("How much Gold do you wish to buy for "+str(ResourcesPrice["gold"])+"$? "))
            ResourcesQuantity=ResourcesAmount
            ResourcesAmount=ResourcesAmount*ResourcesPrice["gold"]
            if Player.totalgold>=ResourcesAmount:
                print("Total paid: "+str(ResourcesAmount))
                Player.totalgold=Player.totalgold-ResourcesAmount
                print("Current Gold:"+str(Player.totalgold))
                Resources["gold"]=Resources["gold"]+ResourcesQuantity
            elif Player.totalgold<ResourcesAmount:
                    print("You dont have enought gold to buy this product!")    

        elif n1=="5":
            print("Here recipes") 
            #puxar recipes aqui   

        elif n1=="6":
            aux = False

BuyResourceRecipes()

def CraftingItems():
    print("Crafting Time!!")
    aux = True
    while aux:
        print("Choose the type of item you want to craft.")
        print("Select Sword(1), Shield(2), Armor(3), Bow(4) or Leave(5)")
        answer = input()
        if answer == "1":
                Choose=input("Which Sword do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                auxrand=random.randint(1,10)
                craftingattempt=Player.level*auxrand
                if Choose=="1":
                    #SwordIni
                  print(Recipes["SwordIni"])
                 
                  if Resources["wood"]>=SwordIni.wood and Resources["leather"]>=SwordIni.leather:
                    if craftingattempt >= SwordIni.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-SwordIni.wood
                        Resources["leather"]=Resources["leather"]-SwordIni.leather
                        #dar exp ao jogador
                        Player.exp=Player.exp+10
                    elif craftingattempt < SwordIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-SwordIni.wood
                        Resources["leather"]=Resources["leather"]-SwordIni.leather
                  else:
                    print("Not enough materials!")      
                if Choose=="2":
                    #SwordInt
                  print(Recipes["SwordInter"]) 
                  if Resources["wood"]>=SwordInter.wood and Resources["leather"]>=SwordInter.leather and Resources["iron"]>=SwordInter.iron:    
                    if craftingattempt >= SwordIni.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-SwordInter.wood
                        Resources["leather"]=Resources["leather"]-SwordInter.leather
                        Resources["iron"]=Resources["iron"]-SwordInter.iron
                        
                        #dar exp ao jogador
                        Player.exp=Player.exp+15
                    elif craftingattempt < SwordIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario  
                        Resources["wood"]=Resources["wood"]-SwordInter.wood
                        Resources["leather"]=Resources["leather"]-SwordInter.leather
                        Resources["iron"]=Resources["iron"]-SwordInter.iron  
                  else:
                    print("Not enough materials!")      
                if Choose=="3":
                    #SwordAdv
                   print(Recipes["SwordAdva"])   
                   if Resources["gold"]>=SwordAdva.gold and Resources["iron"]>=SwordAdva.iron: 
                    if craftingattempt >= SwordAdva.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["gold"]=Resources["gold"]-SwordAdva.gold
                        Resources["iron"]=Resources["iron"]-SwordAdva.iron
                        #dar exp ao jogador
                        Player.exp=Player.exp+20
                    elif craftingattempt < SwordAdva.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario    
                        Resources["gold"]=Resources["gold"]-SwordAdva.gold
                        Resources["iron"]=Resources["iron"]-SwordAdva.iron    
                   else:
                    print("Not enough materials!") 



        elif answer == "2":
                Choose=input("Which Shield do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                auxrand=random.randint(1,10)
                craftingattempt=Player.level*auxrand
                if Choose=="1":
                    #ShieldInit
                  print(Recipes["ShieldIni"])   
                  if Resources["wood"]>=ShieldIni.wood and Resources["leather"]>=ShieldIni.leather:  
                    if craftingattempt >= ShieldIni.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-ShieldIni.wood
                        Resources["leather"]=Resources["leather"]-ShieldIni.leather
                        #dar exp ao jogador
                        Player.exp=Player.exp+10
                    elif craftingattempt < ShieldIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-ShieldIni.wood
                        Resources["leather"]=Resources["leather"]-ShieldIni.leather
                  else:
                    print("Not enough materials!")        
                if Choose=="2":
                    #ShieldInt
                   print(Recipes["ShieldInter"])  
                   if Resources["wood"]>=ShieldInter.wood and Resources["leather"]>=ShieldInter.leather and Resources["iron"]>=ShieldInter.iron: 
                    if craftingattempt >= ShieldInter.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-ShieldInter.wood
                        Resources["leather"]=Resources["leather"]-ShieldInter.leather
                        Resources["iron"]=Resources["iron"]-ShieldInter.iron
                        #dar exp ao jogador
                        Player.exp=Player.exp+15
                    elif craftingattempt < ShieldInter.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-ShieldInter.wood
                        Resources["leather"]=Resources["leather"]-ShieldInter.leather
                        Resources["iron"]=Resources["iron"]-ShieldInter.iron
                   else:
                    print("Not enough materials!")      
                if Choose=="3":
                    #ShieldAdv
                   print(Recipes["ShieldAdva"])  
                   if Resources["leather"]>=ShieldAdva.leather and Resources["iron"]>=ShieldAdva.iron and Resources["gold"]>=ShieldAdva.gold: 
                    if craftingattempt >= ShieldAdva.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-ShieldAdva.leather
                        Resources["iron"]=Resources["iron"]-ShieldAdva.iron
                        Resources["gold"]=Resources["gold"]-ShieldAdva.gold
                        #dar exp ao jogador
                        Player.exp=Player.exp+20
                    elif craftingattempt < ShieldAdva.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario   
                        Resources["leather"]=Resources["leather"]-ShieldAdva.leather
                        Resources["iron"]=Resources["iron"]-ShieldAdva.iron
                        Resources["gold"]=Resources["gold"]-ShieldAdva.gold
                   else:
                    print("Not enough materials!")          
            #ARMOR            
        elif answer == "3":
                print("Please choose the type of armor")
                answer2=input("Select Helmet(1), Chestplate(2), Leggins(3) or Shoes(4) or Leave(5)")
                if answer2 == "1":
                        Choose=input("Which Helmet do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                        auxrand=random.randint(1,10)
                        craftingattempt=Player.level*auxrand
                        if Choose=="1":
                            #helmetini
                           print(Recipes["HelmetIni"])  
                           if Resources["leather"]>=HelmetIni.leather and Resources["iron"]>=HelmetIni.iron: 
                            if craftingattempt >= HelmetIni.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetIni.leather
                                Resources["iron"]=Resources["iron"]-HelmetIni.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+10

                            elif craftingattempt < HelmetIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetIni.leather
                                Resources["iron"]=Resources["iron"]-HelmetIni.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="2":
                            #helmetint
                           print(Recipes["HelmetInter"])  
                           if Resources["leather"]>=HelmetInter.leather and Resources["iron"]>=HelmetInter.iron: 
                            if craftingattempt >= HelmetInter.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetInter.leather
                                Resources["iron"]=Resources["iron"]-HelmetInter.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+15

                            elif craftingattempt < HelmetInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario 
                                Resources["leather"]=Resources["leather"]-HelmetIni.leather
                                Resources["iron"]=Resources["iron"]-HelmetIni.iron
                           else:
                            print("Not enough materials!")         
                        if Choose=="3":
                            #HelmetAdv
                           print(Recipes["HelmetAdva"])  
                           if Resources["leather"]>=HelmetAdva.leather and Resources["iron"]>=HelmetAdva.iron and Resources["gold"]>=HelmetAdva.gold: 
                            if craftingattempt >= HelmetAdva.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetAdva.leather
                                Resources["iron"]=Resources["iron"]-HelmetAdva.iron
                                Resources["gold"]=Resources["gold"]-HelmetIni.gold
                                #dar exp ao jogador
                                Player.exp=Player.exp+20

                            elif craftingattempt < HelmetAdva.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetAdva.leather
                                Resources["iron"]=Resources["iron"]-HelmetAdva.iron
                                Resources["gold"]=Resources["gold"]-HelmetIni.gold
                           else:
                            print("Not enough materials!")

                elif answer2 == "2":
                        Choose=input("Which Helmet do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                        auxrand=random.randint(1,10)
                        craftingattempt=Player.level*auxrand
                        if Choose=="1":
                            #chestplateini
                           print(Recipes["ChestplateIni"])  
                           if Resources["leather"]>=ChestplatelIni.leather and Resources["iron"]>=ChestplatelIni.iron: 
                            if craftingattempt >= ChestplatelIni.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ChestplatelIni.leather
                                Resources["iron"]=Resources["iron"]-ChestplatelIni.iron

                                #dar exp ao jogador
                                Player.exp=Player.exp+10        
                            elif craftingattempt < ChestplatelIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ChestplatelIni.leather
                                Resources["iron"]=Resources["iron"]-ChestplatelIni.iron
                           else:
                            print("Not enough materials!")  
                        if Choose=="2":
                            #Chestplateint
                           print(Recipes["ChestplateInter"])  
                           if Resources["leather"]>=ChestplateInter.leather and Resources["iron"]>=ChestplateInter.iron: 
                            if craftingattempt >= ChestplateInter.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ChestplateInter.leather
                                Resources["iron"]=Resources["iron"]-ChestplateInter.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+15
                           
                            elif craftingattempt < ChestplateInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario   
                                Resources["leather"]=Resources["leather"]-ChestplateInter.leather
                                Resources["iron"]=Resources["iron"]-ChestplateInter.iron
                           else:
                            print("Not enough materials!") 
                        if Choose=="3":
                            #ChestplateAdv
                           print(Recipes["ChestplateAdva"])  
                           if Resources["leather"]>=ChestplateAdva.leather and Resources["iron"]>=ChestplateAdva.iron and Resources["gold"]>=ChestplateAdva.gold: 
                            if craftingattempt >= ChestplateAdva.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ChestplateAdva.leather
                                Resources["iron"]=Resources["iron"]-ChestplateAdva.iron
                                Resources["gold"]=Resources["gold"]-ChestplateAdva.gold
                                #dar exp ao jogador
                                Player.exp=Player.exp+20

                            elif craftingattempt < ChestplateAdva.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ChestplateAdva.leather
                                Resources["iron"]=Resources["iron"]-ChestplateAdva.iron
                                Resources["gold"]=Resources["gold"]-ChestplateAdva.gold
                           else:
                            print("Not enough materials!")     
                elif answer2 == "3":
                        Choose=input("Which Leggins do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                        auxrand=random.randint(1,10)
                        craftingattempt=Player.level*auxrand
                        if Choose=="1":
                            #legginsini
                           print(Recipes["LegginsIni"])  
                           if Resources["leather"]>=LegginsIni.leather and Resources["iron"]>=LegginsIni.iron: 
                            if craftingattempt >= LegginsIni.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-LegginsIni.leather
                                Resources["iron"]=Resources["iron"]-LegginsIni.iron

                                #dar exp ao jogador
                                Player.exp=Player.exp+10

                            elif craftingattempt < LegginsIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-LegginsIni.leather
                                Resources["iron"]=Resources["iron"]-LegginsIni.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="2":
                            #legginsinter
                           print(Recipes["LegginsInter"])  
                           if Resources["leather"]>=LegginsInter.leather and Resources["iron"]>=LegginsInter.iron: 
                            if craftingattempt >= LegginsInter.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-LegginsInter.leather
                                Resources["iron"]=Resources["iron"]-LegginsInter.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+15
                            elif craftingattempt < LegginsInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario    
                                Resources["leather"]=Resources["leather"]-LegginsInter.leather
                                Resources["iron"]=Resources["iron"]-LegginsInter.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="3":
                            #legginsAdv
                           print(Recipes["LegginsAdva"])  
                           if Resources["leather"]>=LegginsAdva.leather and Resources["iron"]>=LegginsAdva.iron and Resources["gold"]>=LegginsAdva.gold: 
                            if craftingattempt >= LegginsAdva.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-LegginsAdva.leather
                                Resources["iron"]=Resources["iron"]-LegginsAdva.iron
                                Resources["gold"]=Resources["gold"]-LegginsAdva.gold
                                #dar exp ao jogador
                                Player.exp=Player.exp+20

                            elif craftingattempt < LegginsAdva.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario        
                                Resources["leather"]=Resources["leather"]-LegginsAdva.leather
                                Resources["iron"]=Resources["iron"]-LegginsAdva.iron
                                Resources["gold"]=Resources["gold"]-LegginsAdva.gold
                           else:
                            print("Not enough materials!")
                elif answer2 == "4":
                        Choose=input("Which Helmet do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                        auxrand=random.randint(1,10)
                        craftingattempt=Player.level*auxrand
                        if Choose=="1":
                            #shoesini
                           print(Recipes["ShoesIni"])  
                           if Resources["leather"]>=ShoesIni.leather and Resources["iron"]>=ShoesIni.iron: 
                            if craftingattempt >= ShoesIni.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ShoesIni.leather
                                Resources["iron"]=Resources["iron"]-ShoesIni.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+10
                            elif craftingattempt < ShoesIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ShoesIni.leather
                                Resources["iron"]=Resources["iron"]-ShoesIni.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="2":
                            #shoesint
                           print(Recipes["ShoesInter"])  
                           if Resources["leather"]>=ShoesInter.leather and Resources["iron"]>=ShoesInter.iron: 
                            if craftingattempt >= ShoesInter.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ShoesInter.leather
                                Resources["iron"]=Resources["iron"]-ShoesInter.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+15

                            elif craftingattempt < ShoesInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario  
                                Resources["leather"]=Resources["leather"]-ShoesInter.leather
                                Resources["iron"]=Resources["iron"]-ShoesInter.iron
                           else:
                            print("Not enough materials!")  
                        if Choose=="3":
                            #shoesAdv
                           print(Recipes["ShoesAdva"])  
                           if Resources["leather"]>=ShoesAdva.leather and Resources["iron"]>=ShoesAdva.iron and Resources["gold"]>=ShoesAdva.gold: 
                            if craftingattempt >= ShoesAdva.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ShoesAdva.leather
                                Resources["iron"]=Resources["iron"]-ShoesAdva.iron
                                Resources["gold"]=Resources["gold"]-ShoesAdva.gold
                                #dar exp ao jogador
                                Player.exp=Player.exp+20

                            elif craftingattempt < ShoesAdva.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario   
                                Resources["leather"]=Resources["leather"]-ShoesAdva.leather
                                Resources["iron"]=Resources["iron"]-ShoesAdva.iron
                                Resources["gold"]=Resources["gold"]-ShoesAdva.gold
                           else:
                            print("Not enough materials!")     
        elif answer == "4":
                Choose=input("Which Bow do you wish to create Beginner(1),Intermediate(2),Advanced(3) or Arrows(4)?")
                auxrand=random.randint(1,10)
                craftingattempt=Player.level*auxrand
                if Choose=="1":
                    #BowIni
                   print(Recipes["BowIni"])  
                   if Resources["wood"]>=BowIni.wood and Resources["leather"]>=BowIni.leather: 
                    if craftingattempt >= BowIni.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-BowIni.leather
                        Resources["wood"]=Resources["wood"]-BowIni.wood
                        #dar exp ao jogador
                        Player.exp=Player.exp+10
                    elif craftingattempt < BowIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-BowIni.leather
                        Resources["wood"]=Resources["wood"]-BowIni.wood
                   else:
                    print("not enough materials!")      
                if Choose=="2":
                    #BowInt
                   print(Recipes["BowInter"])  
                   if Resources["wood"]>=BowInter.wood and Resources["leather"]>=BowInter.leather and Resources["iron"]>=BowInter.iron: 
                    if craftingattempt >= BowInter.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-BowInter.leather
                        Resources["wood"]=Resources["wood"]-BowInter.wood
                        Resources["iron"]=Resources["iron"]-BowInter.iron
                        #dar exp ao jogador
                        Player.exp=Player.exp+15
                    elif craftingattempt < BowInter.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario   
                        Resources["leather"]=Resources["leather"]-BowInter.leather
                        Resources["wood"]=Resources["wood"]-BowInter.wood
                        Resources["iron"]=Resources["iron"]-BowInter.iron
                   else:
                    print("Not enough materials!")       
                if Choose=="3":
                    #BowAdv
                   print(Recipes["BowAdva"])  
                   if Resources["leather"]>=BowAdva.leather and Resources["iron"]>=BowAdva.iron and Resources["gold"]>=BowAdva.gold: 
                    if craftingattempt >= BowAdva.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-BowAdva.leather
                        Resources["gold"]=Resources["gold"]-BowAdva.gold
                        Resources["iron"]=Resources["iron"]-BowAdva.iron
                        #dar exp ao jogador
                        Player.exp=Player.exp+20
                    elif craftingattempt < BowAdva.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-BowAdva.leather
                        Resources["gold"]=Resources["gold"]-BowAdva.gold
                        Resources["iron"]=Resources["iron"]-BowAdva.iron
                   else:
                    print("Not enough materials")     
                if Choose=="4":
                    #Arrows
                   print(Recipes["Arrows"])  
                   if Resources["wood"]>=Arrows.wood and Resources["iron"]>=Arrows.iron: 
                    if craftingattempt >= Arrows.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["iron"]=Resources["iron"]-Arrows.iron
                        Resources["wood"]=Resources["wood"]-Arrows.wood
                    
                        #dar exp ao jogador
                        Player.exp=Player.exp+15
                    elif craftingattempt < Arrows.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario    
                        Resources["iron"]=Resources["iron"]-Arrows.iron
                        Resources["wood"]=Resources["wood"]-Arrows.wood   
                   else:
                    print("Not enough materials!")       
        elif answer2 == "5":
                        aux = False
        else:
            print("Not found!")                

CraftingItems()

def SellingItems():
    #alterar para ter uma funcao para cada npc, provavelmente dentro de uma classe NPC 
    print("Its time to sell your awesome items")
    npcRange = (1,2,3,4,5,6,7,8)
    npcNumber=random.choice(npcRange)
    if npcNumber == 1:
        print("Your loyal customer Bill showed up to your store to purchase some items! \n")
        print("Since he's a regular you usually give him a 20(%) discount... \n")
        print("Will you keep giving him his regular discount or sell an item for full price? Select (y) or (n) \n")
        answerNPC = input()
        OptionNPC = ["y", "n"]
        if answerNPC not in OptionNPC:
            print("Will you keep giving him his regular discount or sell an item for full price? Select (y) or (n) \n")
        
        elif answerNPC == "y":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your loyal customer will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                #aplicar 20% desconto na compra e remover o item do inventario
                #Player.totalgold += InventoryToSell[] - (ItemPrice * 0.20)
                aux = False

        elif answerNPC == "n":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #definir x para numero total de items no inventario to sell
                x=1
                randAmount = random.randint(1, x)
                print("Although Bill is very angry with you he will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("Bill left the shop yelling at you : MotherF*!%#+@ !!!")
                #remover o item do inventario
                #Player.totalgold += ItemPrice
                aux = False

    elif npcNumber == 2:
        print("Your crush from the flower shop next to you has entered your shop in hopes of buying something nice for her niece \n")
        print("Since you like her so much you could risk loosing profit AND make her happy with a 50(%) discount on her purchase \n")
        print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        answerNPC = input()
        OptionNPC = ["y", "n"]
        if answerNPC not in OptionNPC:
            print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        
        elif answerNPC == "y":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("You have failed all man today, you let a mere woman buy you item(s) for next to nothing... SIMP!!! \n")
                #aplicar 50% desconto na compra e remover o item do inventario
                #Player.totalgold += InventoryToSell[] - (ItemPrice * 0.50)
                aux = False

        elif answerNPC == "n":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("Congratulations Private! You passed the SIMP test and sold " + str(randAmount) + " item(s) at full price! \n")
                #remover o item do inventario
                #Player.totalgold += ItemPrice
                aux = False

    elif npcNumber == 3:
        print("A new client showed up at your shop. \n")
        print("He seems to understand very easily the high quality of yout craftsmanship. \n")
        aux = True
        while aux:    
            randSelect = random.choice(InventoryToSell)
            #randAmount = random.randint(1, InventoryToSell.amount)
            print("New client will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
            print("You have sold" + str(randAmount) + randSelect + "from you at full price. \n")
            #Player.totalgold += ItemPrice
            aux = False

    elif npcNumber == 4:

        print("Your crush from the flower shop next to you has entered your shop in hopes of buying something nice for her niece \n")
        print("Since you like her so much you could risk loosing profit AND make her happy with a 50(%) discount on her purchase \n")
        print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        answerNPC = input()
        OptionNPC = ["y", "n"]
        if answerNPC not in OptionNPC:
            print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        
        elif answerNPC == "y":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("You have failed all man today, you let a mere woman buy you item(s) for next to nothing... SIMP!!! \n")
                #aplicar 50% desconto na compra e remover o item do inventario
                #Player.totalgold += InventoryToSell[] - (ItemPrice * 0.50)
                aux = False

        elif answerNPC == "n":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("Congratulations Private! You passed the SIMP test and sold " + str(randAmount) + " item(s) at full price! \n")
                #remover o item do inventario
                #Player.totalgold += ItemPrice
                aux = False
                print(randSelect)

    elif npcNumber == 5:

        print("Your crush from the flower shop next to you has entered your shop in hopes of buying something nice for her niece \n")
        print("Since you like her so much you could risk loosing profit AND make her happy with a 50(%) discount on her purchase \n")
        print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        answerNPC = input()
        OptionNPC = ["y", "n"]
        if answerNPC not in OptionNPC:
            print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        
        elif answerNPC == "y":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("You have failed all man today, you let a mere woman buy you item(s) for next to nothing... SIMP!!! \n")
                #aplicar 50% desconto na compra e remover o item do inventario
                #Player.totalgold += InventoryToSell[] - (ItemPrice * 0.50)
                aux = False

        elif answerNPC == "n":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("Congratulations Private! You passed the SIMP test and sold " + str(randAmount) + " item(s) at full price! \n")
                #remover o item do inventario
                #Player.totalgold += ItemPrice
                aux = False
                print(randSelect)
        
    elif npcNumber == 6:

        print("Your crush from the flower shop next to you has entered your shop in hopes of buying something nice for her niece \n")
        print("Since you like her so much you could risk loosing profit AND make her happy with a 50(%) discount on her purchase \n")
        print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        answerNPC = input()
        OptionNPC = ["y", "n"]
        if answerNPC not in OptionNPC:
            print("Will you once again be her simp and possibly loose money with this customer? Select (y) or (n) \n")
        
        elif answerNPC == "y":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("You have failed all man today, you let a mere woman buy you item(s) for next to nothing... SIMP!!! \n")
                #aplicar 50% desconto na compra e remover o item do inventario
                #Player.totalgold += InventoryToSell[] - (ItemPrice * 0.50)
                aux = False

        elif answerNPC == "n":
            aux = True
            while aux:    
                randSelect = random.choice(InventoryToSell)
                #randAmount = random.randint(1, InventoryToSell.amount)
                print("Your crush will be purchasing : " + str(randAmount) + randSelect + "from you. \n")
                print("Congratulations Private! You passed the SIMP test and sold " + str(randAmount) + " item(s) at full price! \n")
                #remover o item do inventario
                #Player.totalgold += ItemPrice
                aux = False
                print(randSelect)

    else:
        pass

SellingItems()