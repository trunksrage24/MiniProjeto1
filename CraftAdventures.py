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
    #3 shields
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
SuccessRating=5

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
        options = [1, 2, 3, 4, 5]
        answer = input()
        if answer not in options:
            print("Select Sword(1), Shield(2), Armor(3), Bow(4) or Leave(5)")
        else:
            if answer == "1":
                Option = [InventoryToSell[0], InventoryToSell[1], InventoryToSell[2]]
                
                craftingattempt=Player.Player.level*Option
                if craftingattempt >= SuccessRating:
                    print("Done and Done!!! "+str(craftingattempt))
                    #remover os items do inventario
                    #dar exp ao jogador

                elif craftingattempt < SuccessRating:  
                    print("Not Done! "+str(craftingattempt)) 
                    #remover os items do inventario
            
            elif answer == "2":
                Option = [InventoryToSell[3], InventoryToSell[4], InventoryToSell[5]]
                craftingattempt=Player.level*Option
                if craftingattempt >= SuccessRating:
                    print("Done and Done!!! "+str(craftingattempt))
                    #remover os items do inventario
                    #dar exp ao jogador

                elif craftingattempt < SuccessRating:  
                    print("Not Done! "+str(craftingattempt)) 
                    #remover os items do inventario

            elif answer == "3":
                print("Please choose the type of armor")
                print("Select Helmet(1), Chestplate(2), Leggins(3) or Shoes(4) or Leave(5)")
                options2 = [1, 2, 3, 4, 5]
                answer2 = input()
                if answer2 not in options2:
                    print("Select Helmet(1), Chestplate(2), Leggins(3) or Shoes(4) or Leave(5)")
                else:
                    if answer2 == "1":
                        Option = [InventoryToSell[6], InventoryToSell[7], InventoryToSell[8]]
                        craftingattempt=Player.level*Option
                        if craftingattempt >= SuccessRating:
                            print("Done and Done!!! "+str(craftingattempt))
                            #remover os items do inventario
                            #dar exp ao jogador

                        elif craftingattempt < SuccessRating:  
                            print("Not Done! "+str(craftingattempt)) 
                            #remover os items do inventario

                    elif answer2 == "2":
                        Option = [InventoryToSell[9], InventoryToSell[10], InventoryToSell[11]]
                        craftingattempt=Player.level*Option
                        if craftingattempt >= SuccessRating:
                            print("Done and Done!!! "+str(craftingattempt))
                            #remover os items do inventario
                            #dar exp ao jogador

                        elif craftingattempt < SuccessRating:  
                            print("Not Done! "+str(craftingattempt)) 
                            #remover os items do inventario  

                    elif answer2 == "3":
                        Option = [InventoryToSell[12], InventoryToSell[13], InventoryToSell[14]]
                        craftingattempt=Player.level*Option
                        if craftingattempt >= SuccessRating:
                            print("Done and Done!!! "+str(craftingattempt))
                            #remover os items do inventario
                            #dar exp ao jogador

                        elif craftingattempt < SuccessRating:  
                            print("Not Done! "+str(craftingattempt)) 
                            #remover os items do inventario        

                    elif answer2 == "4":
                        Option = [InventoryToSell[15], InventoryToSell[16], InventoryToSell[17]]
                        craftingattempt=Player.level*Option
                        if craftingattempt >= SuccessRating:
                            print("Done and Done!!! "+str(craftingattempt))
                            #remover os items do inventario
                            #dar exp ao jogador

                        elif craftingattempt < SuccessRating:  
                            print("Not Done! "+str(craftingattempt)) 
                            #remover os items do inventario   

                    elif answer2 == "5":
                        aux = False

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