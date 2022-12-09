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
    #3 bow
    #1 arrow

#classe "pai"
class Item:
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
    
    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)

#classe para dados do jogador
class Player:
    name=""
    totalgold=7000
    exp=0
    level=1 
    day=1
    auxvar=False

#classe dados espadas
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
    qt=0
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
    qt=0
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
    qt=0
    def __init__(self,wood,leather,SuccessRating):
        super().__init__("SwordIni", 10000)
        print(self.name + str(self.gold))
        self.wood=wood
        self.leather=leather
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()
        

#classe dados escudos
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
    qt=0
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
    qt=0
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
    qt=0
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

#classe dados armaduras
class Armors(Item):
    # 3 helmets, 3 chestplates, 3 leggings e 3 shoes
    def __init__(self):
        super().__init__("Armors", 0)

    def Display(self):
        print("Name" + self.name)
        print("Sell Value" + self.gold)
        
##classe dados capacete
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
    qt=0
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
    qt=0
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
    qt=0
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("HelmetAdva", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#classe dados armaduras corpo
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
    qt=0
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
    qt=0
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
    qt=0
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("ChestplateAdva", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#classe dados calças
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
    qt=0
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
    qt=0
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
    qt=0
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("HelmetInter", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#classe dados sapatos
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
    qt=0
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
    qt=0
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
    qt=0
    def __init__(self,leather,iron,gold,SuccessRating):
        super().__init__("ShoesAdva", 10000)
        print(self.name + str(self.gold))
        self.leather=leather
        self.iron=iron
        self.gold=gold
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()

#classe dados arcos
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
    qt=0
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
    qt=0
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
    qt=0
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
    qt=0
    def __init__(self,wood,iron,SuccessRating):
        super().__init__("HelmetInter", 10000)
        print(self.name + str(self.gold))
        self.wood=wood
        self.iron=iron
        self.SuccessRating=SuccessRating
    def Display(self):
        super().Display()
#Recursos com que o jogador começa
Resources = {
    "wood" : 5,
    "leather" : 5,
    "iron" : 5,
    "gold" : 0  
}

#Preço dos recursos
ResourcesPrice = {
    "wood" : 25,
    "leather" : 35,
    "iron" : 90,
    "gold" : 180
}

#Oque cada item precisa para ser "craftado"
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

#Dict para guardar recipes que ainda não foram comprados pelo jogador(sofre alterações ao longo do codigo)
Recipestobuy= {
    #Beginner(1),Intermediate(2) or Advanced(3)?
        "1":["Sword Begginer",150],
        "2":["Sword Intermediate",1000],
        "3":["Sword Advanced",3000],

        "4":["Shield Beginner",150],
        "5":["Shield Intermediate",1000],
        "6":["Shield Advanced",3000],

        "7":["Helmet Beginner",150],
        "8":["Helmet Intermediate",1000],
        "9":["Helmet Advanced",3000],

        "10":["Chestplate Beginner",150],
        "11":["Chestplate Intermediate",1000],
        "12":["Chestplate Advanced",3000],

        "13":["Leggins Beginner",150],
        "14":["Leggins Intermediate",1000],
        "15":["Leggins Advanced",3000],

        "16":["Shoes Beginner",150],
        "17":["Shoes Intermediate",1000],
        "18":["Shoes Advanced",3000],

        "19":["Bow Beginner",150],
        "20":["Bow Intermediate",1000],
        "21":["Bow Advanced",3000],

        "22":["Arrows",150]
}

#Receitas compradas pelo jogador são postas aqui para verificar quais dos recipes o jogador pode fazer
Recipesbought={
}
def VerifyWin():
    #verifica se o dinheiro do jogador chegou aos 100k,se sim então mostra que venceu
    if Player.totalgold==100000:
        print("You Win!!"+str(Player.totalgold))
def BuyResourceRecipes(bought):
    print("Buy Resources/Recipes")
    aux = True
    while aux:
        #mostra recursos que o jogador tem
        print("Wood: "+str(Resources["wood"]))
        print("Leather: "+str(Resources["leather"]))
        print("Iron: "+str(Resources["iron"]))
        print("gold: "+str(Resources["gold"]))
        n1=input("Do you wish to buy Wood(1) for "+str(ResourcesPrice["wood"])+"$,Leather(2)"+str(ResourcesPrice["leather"])+"$, Iron(3)"+str(ResourcesPrice["iron"])+"$, Gold(4)"+str(ResourcesPrice["gold"])+"$,Recipes(5) or leave(6)? ")
        if n1=="1":
            #Pede a quantidade ao jogador e multiplica pelo preço, subtraindo ao dinheiro do jogador
            #caso não tenho a quantidade suficiente então apenas mostra que o jogador não tem dinheiro (o mesmo para os restantes recursos)
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

        elif n1 == "2":
            ResourcesAmount = int(input("How much Leather do you wish to buy for " + str(ResourcesPrice["leather"]) + "$? "))
            ResourcesQuantity = ResourcesAmount
            ResourcesAmount *= int(ResourcesPrice["leather"])
            
            if Player.totalgold >= ResourcesAmount:
                print("Total paid: " + str(ResourcesAmount))
                Player.totalgold -= ResourcesAmount
                print("Current Gold:" + str(Player.totalgold))
                Resources["leather"] += ResourcesQuantity
            
            elif Player.totalgold < ResourcesAmount:
                    print("You dont have enought gold to buy this product!")    
            
        elif n1 == "3":   
            ResourcesAmount = int(input("How much Iron do you wish to buy for " + str(ResourcesPrice["iron"]) + "$? "))
            ResourcesQuantity = ResourcesAmount
            ResourcesAmount *= ResourcesPrice["iron"]
            
            if Player.totalgold >= ResourcesAmount:
                print("Total paid: " + str(ResourcesAmount))
                Player.totalgold -= ResourcesAmount
                print("Current Gold:" + str(Player.totalgold))
                Resources["iron"] += ResourcesQuantity
            
            elif Player.totalgold<ResourcesAmount:
                    print("You dont have enought gold to buy this product!")    

        elif n1 == "4":   
            ResourcesAmount = int(input("How much Gold do you wish to buy for " + str(ResourcesPrice["gold"]) + "$? "))
            ResourcesQuantity = ResourcesAmount
            ResourcesAmount *= ResourcesPrice["gold"]
            
            if Player.totalgold >= ResourcesAmount:
                print("Total paid: " + str(ResourcesAmount))
                Player.totalgold -= ResourcesAmount
                print("Current Gold:" + str(Player.totalgold))
                Resources["gold"] += ResourcesQuantity
            
            elif Player.totalgold < ResourcesAmount:
                print("You dont have enought gold to buy this product!")    
        
        elif bought == False: 
            
            if n1 == "5":
                print("Here recipes") 
                print("Begginer for 150$, Intermediate for 1000$ and Advanced for 3000$!! WE DONT GIVE DISCOUNTS!")  
                #escolhe 3 items random do dict que guardar as receitas que ainda não foram compradas.
                if Player.auxvar == False:
                    item1 = random.choice(list(Recipestobuy.items()))
                    item2 = random.choice(list(Recipestobuy.items()))
                    item3 = random.choice(list(Recipestobuy.items()))
                print("Recipes to buy: " + str(item1[1][0]) + "(1)," + str(item2[1][0]) + "(2)," + str(item3[1][0]) + "(3) or leave(4)")
                choice = input("Which do you wish to buy?")
                #var global para não deixar o jogador comprar varias receitas
                Player.auxvar = True
                
                if choice == "1":
                    #retira a receita comprada do dict "Recipestobuy" e mete no dict "Recipesbought", retira dinheiro do jogador e mostra repetivas ações
                    #o mesmo acontece para os restantes
                    Recipesbought[item1[0]] = item1[1]
                    Player.totalgold -= item1[1][1]
                    print("Bought: " + str(item1[1][0]))
                    print("Current Wealth: " + str(Player.totalgold))
                    Recipestobuy.pop(item1[0])
                    bought = True
                    
                elif choice == "2":
                    Recipesbought[item2[0]] = item2[1]
                    Player.totalgold -= item2[1][1]
                    print("Bought: " + str(item2[1][0]))
                    print("Current Wealth: " + str(Player.totalgold))
                    Recipestobuy.pop(item2[0]) 
                    bought = True
                    
                elif choice == "3":
                    Recipesbought[item3[0]] = item3[1]
                    Player.totalgold -= item3[1][1]
                    print("Bought: " + str(item3[1][0]))
                    print("Current Wealth: " + str(Player.totalgold))
                    Recipestobuy.pop(item3[0])           
                    bought = True 
                   
        #baseado numa variavel global verifica se o jogador já comprou um item, se sim diz que já comprou o limite receitas para aquele dia
        elif bought == True:
                print("Already bought a recipe! Therefore you cant buy anymore today!")   
        
        #para o while                
        if n1 == "6":
            aux = False

def levelup():
    #função para aumentar o nivel se o exp for maior que o respetivo valor
    if Player.exp % 50 == 0:
        Player.level += 1
        print("Level up!")
    
        Player.level += 1      
        print("Level up!")  

def verifyrecipes(choose):
    #verifica se o item que o jogador escolheu fazer está ou não nas receitas compradas, se sim procede com o craft, se não diz que
    #não tem o recipe comprado
    if choose in Recipesbought:
        print("Crafting!!")
        choose=True
        return choose
    
    else:
        print("Dont have the recipe for this item!!")    

def CraftingItems():
    #funcao pega os resources do inventário e gasta os que precisa paracraft deitem selecionado
    print("Crafting Time!!")
    aux = True
    while aux:
        print("Choose the type of item you want to craft.")
        print("Select Sword(1), Shield(2), Armor(3), Bow(4) or Leave(5)")
        answer = input()
        #escolhe o item que o jogador escolheu
        
        #SWORD
        if answer == "1":
                Choose = input("Which Sword do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                #random de 1 a 10 ,multiplica isso pelo lv do jogador, verifica se o jogador tem o recipe, se sim continua
                #mostra oque é necessario para o craft
                auxrand=random.randint(1,10)
                craftingattempt=Player.level*auxrand
                if Choose=="1":
                 if verifyrecipes(Choose)==True:  #AQUI
                    #SwordIni
                  print(Recipes["SwordIni"])
             #verifica se o jogador tem os materiais necessarios para o craft, se sim remove os recursos do jogador, adiciona exp 
             #e chama função levelup para verificar se o jogador passou de nivel
                  if Resources["wood"]>=SwordIni.wood and Resources["leather"]>=SwordIni.leather:
                    if craftingattempt >= SwordIni.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-SwordIni.wood
                        Resources["leather"]=Resources["leather"]-SwordIni.leather
                        #dar exp ao jogador
                        Player.exp=Player.exp+10
                        levelup()
               #se não tiver conseguido fazer o craft então apenas remove os recursos         
                    elif craftingattempt < SwordIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-SwordIni.wood
                        Resources["leather"]=Resources["leather"]-SwordIni.leather
                #caso não tenha os recursos mostra que não tem os materiais necessarios      
                  else:
                    print("Not enough materials!")      
                #MESMO SISTEMA PARA O RESTANTE CODIGO               
                if Choose=="2":
                 if verifyrecipes(Choose)==True:  
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
                        levelup()
                    elif craftingattempt < SwordIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario  
                        Resources["wood"]=Resources["wood"]-SwordInter.wood
                        Resources["leather"]=Resources["leather"]-SwordInter.leather
                        Resources["iron"]=Resources["iron"]-SwordInter.iron  
                  else:
                    print("Not enough materials!")      
                
                if Choose=="3": 
                 if verifyrecipes(Choose)==True:      
                    #SwordAdv
                   print(Recipes["SwordAdva"])   
                   if Resources["gold"]>=SwordAdva.gold and Resources["iron"]>=SwordAdva.iron: 
                    if craftingattempt >= SwordAdva.SuccessRating:
                        print("Done and Done!!! "+str(craftingattempt))
                        #remover os items do inventario
                        Resources["gold"]=Resources["gold"]-SwordAdva.gold
                        Resources["iron"]=Resources["iron"]-SwordAdva.iron
                        #dar exp ao jogador
                        Player.exp=Player.exp+30
                        levelup()
                    elif craftingattempt < SwordAdva.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario    
                        Resources["gold"]=Resources["gold"]-SwordAdva.gold
                        Resources["iron"]=Resources["iron"]-SwordAdva.iron    
                   else:
                    print("Not enough materials!")

        #SHIELD
        elif answer == "2":
                Choose=input("Which Shield do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                auxrand=random.randint(1,10)
                craftingattempt=Player.level*auxrand
                if Choose=="1":
                 Choose="4"  
                 if verifyrecipes(Choose)==True:   
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
                        levelup()
                    elif craftingattempt < ShieldIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-ShieldIni.wood
                        Resources["leather"]=Resources["leather"]-ShieldIni.leather
                  else:
                    print("Not enough materials!")        
                if Choose=="2":
                 Choose="5"  
                 if verifyrecipes(Choose)==True:    
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
                        levelup()
                    elif craftingattempt < ShieldInter.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["wood"]=Resources["wood"]-ShieldInter.wood
                        Resources["leather"]=Resources["leather"]-ShieldInter.leather
                        Resources["iron"]=Resources["iron"]-ShieldInter.iron
                   else:
                    print("Not enough materials!")      
                if Choose=="3":
                 Choose="6"  
                 if verifyrecipes(Choose)==True:   
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
                        levelup()
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
                        Choose = input("Which Helmet do you wish to create, Beginner(1),Intermediate(2) or Advanced(3)?")
                        auxrand = random.randint(1,10)
                        craftingattempt = Player.level * auxrand
                        
                        if Choose == "1":
                            #helmetini
                         Choose="7"  
                         if verifyrecipes(Choose)==True:   
                           print(Recipes["HelmetIni"])  
                           if Resources["leather"]>=HelmetIni.leather and Resources["iron"]>=HelmetIni.iron: 
                            if craftingattempt >= HelmetIni.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetIni.leather
                                Resources["iron"]=Resources["iron"]-HelmetIni.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+10
                                levelup()
                            elif craftingattempt < HelmetIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetIni.leather
                                Resources["iron"]=Resources["iron"]-HelmetIni.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="2":
                            #helmetint
                         Choose="8"  
                         if verifyrecipes(Choose)==True:    
                           print(Recipes["HelmetInter"])  
                           if Resources["leather"]>=HelmetInter.leather and Resources["iron"]>=HelmetInter.iron: 
                            if craftingattempt >= HelmetInter.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-HelmetInter.leather
                                Resources["iron"]=Resources["iron"]-HelmetInter.iron
                                #dar exp ao jogador
                                Player.exp=Player.exp+15
                                levelup()
                            elif craftingattempt < HelmetInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario 
                                Resources["leather"]=Resources["leather"]-HelmetIni.leather
                                Resources["iron"]=Resources["iron"]-HelmetIni.iron
                           else:
                            print("Not enough materials!")         
                        if Choose=="3":
                            #HelmetAdv
                         Choose="9"  
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
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
                         Choose="10"  
                         if verifyrecipes(Choose)==True:   
                            #chestplateini
                           print(Recipes["ChestplatelIni"])  
                           if Resources["leather"]>=ChestplatelIni.leather and Resources["iron"]>=ChestplatelIni.iron: 
                            if craftingattempt >= ChestplatelIni.SuccessRating:
                                print("Done and Done!!! "+str(craftingattempt))
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ChestplatelIni.leather
                                Resources["iron"]=Resources["iron"]-ChestplatelIni.iron

                                #dar exp ao jogador
                                Player.exp=Player.exp+10
                                levelup()       
                            elif craftingattempt < ChestplatelIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ChestplatelIni.leather
                                Resources["iron"]=Resources["iron"]-ChestplatelIni.iron
                           else:
                            print("Not enough materials!")  
                        if Choose=="2":
                         Choose="11"  
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
                            elif craftingattempt < ChestplateInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario   
                                Resources["leather"]=Resources["leather"]-ChestplateInter.leather
                                Resources["iron"]=Resources["iron"]-ChestplateInter.iron
                           else:
                            print("Not enough materials!") 
                        if Choose=="3":
                         Choose="12"  
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
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
                         Choose="13"  
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
                            elif craftingattempt < LegginsIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-LegginsIni.leather
                                Resources["iron"]=Resources["iron"]-LegginsIni.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="2":
                         Choose="14"  
                         if verifyrecipes(Choose)==True:  
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
                                levelup()
                            elif craftingattempt < LegginsInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario    
                                Resources["leather"]=Resources["leather"]-LegginsInter.leather
                                Resources["iron"]=Resources["iron"]-LegginsInter.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="3":
                         Choose="15"  
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
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
                         Choose="16"  
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
                            elif craftingattempt < ShoesIni.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario
                                Resources["leather"]=Resources["leather"]-ShoesIni.leather
                                Resources["iron"]=Resources["iron"]-ShoesIni.iron
                           else:
                            print("Not enough materials!")     
                        if Choose=="2":
                         Choose="17"  
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
                            elif craftingattempt < ShoesInter.SuccessRating:  
                                print("Not Done! "+str(craftingattempt)) 
                                #remover os items do inventario  
                                Resources["leather"]=Resources["leather"]-ShoesInter.leather
                                Resources["iron"]=Resources["iron"]-ShoesInter.iron
                           else:
                            print("Not enough materials!")  
                    
                        if Choose=="3":
                         Choose="18"  
                        
                         if verifyrecipes(Choose)==True:   
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
                                levelup()
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
                 Choose="19"  
                 if verifyrecipes(Choose)==True:   
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
                        levelup()
                    elif craftingattempt < BowIni.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-BowIni.leather
                        Resources["wood"]=Resources["wood"]-BowIni.wood
                   else:
                    print("not enough materials!")      
                if Choose=="2":
                 Choose="20"  
                 if verifyrecipes(Choose)==True:   
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
                        levelup()
                    elif craftingattempt < BowInter.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario   
                        Resources["leather"]=Resources["leather"]-BowInter.leather
                        Resources["wood"]=Resources["wood"]-BowInter.wood
                        Resources["iron"]=Resources["iron"]-BowInter.iron
                   else:
                    print("Not enough materials!")       
                if Choose=="3":
                 Choose="21"  
                 if verifyrecipes(Choose)==True:   
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
                        levelup()
                    elif craftingattempt < BowAdva.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario
                        Resources["leather"]=Resources["leather"]-BowAdva.leather
                        Resources["gold"]=Resources["gold"]-BowAdva.gold
                        Resources["iron"]=Resources["iron"]-BowAdva.iron
                   else:
                    print("Not enough materials")     
                if Choose=="4":
                 Choose="22"  
                 if verifyrecipes(Choose)==True:   
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
                        levelup()
                    elif craftingattempt < Arrows.SuccessRating:  
                        print("Not Done! "+str(craftingattempt)) 
                        #remover os items do inventario    
                        Resources["iron"]=Resources["iron"]-Arrows.iron
                        Resources["wood"]=Resources["wood"]-Arrows.wood   
                   else:
                    print("Not enough materials!") 
        #parar o While                  
        elif answer == "5":
                        aux = False
       
        #caso o jogador escreva um numero que não seja um dos pedidos
        else:
            print("Command not found!")                

def SellingItems():
        #alterar para ter uma funcao para cada npc, provavelmente dentro de uma classe NPC 
    print("Its time to sell your awesome items")
    npcRange = (1,2,3,4)
    npcNumber=random.choice(npcRange)
    
    if npcNumber == 1:
        print("Your loyal customer Bill showed up to your store to purchase a " + str(SwordIni.name) + "\n")
        print("Since he's a regular you usually give him a 20(%) discount... \n")
        print("Will you keep giving him his regular discount or sell an item for full price? Select (y) or (n) \n")
        answerNPC = input()
        OptionNPC = ["y", "n"]
       
        if answerNPC not in OptionNPC:
            print("Will you keep giving him his regular discount or sell an item for full price? Select (y) or (n) \n")
         
        elif answerNPC == "y":
            if SwordIni.qt >= 1:    
                SwordIni.qt -= 1
                #aplicar 20% desconto na compra e remover o item do inventario
                Player.totalgold += (SwordIni.gold - (SwordIni.gold * 0.2)) 
                print("Bill has bought a " + str(SwordIni.name) + " from you. \n")

        elif answerNPC == "n":
            if SwordIni.qt >= 1:    
                SwordIni.qt -= 1
                Player.totalgold += SwordIni.gold
                print("Although Bill is very angry with you he will be buying the " + str(SwordIni.name) + " from you. \n")
                print("Bill left the shop yelling at you : MotherF*!%#+@ !!!")
 

    elif npcNumber == 2:
        print("Your neighbour Anna went by your shop to buy a " + str(BowInter.name) + " as gift to her son \n")
        if BowInter.qt >= 1:
            BowInter.qt -= 1
            Player.totalgold += BowInter.gold
        else:
            print("Client left without buying.")

    elif npcNumber == 3:
        print("2 men enter the shop and introduce themselfs as Rodd and Todd. They are looking for a " +  str(HelmetIni.name) + " and " +  
               str(ChestplatelIni.name) + " to train in the fields. \n")
        if HelmetIni.qt >= 1 and ChestplatelIni.qt >= 1:
            HelmetIni.qt -= 1
            ChestplatelIni.qt -= 1
            Player.totalgold += HelmetIni.gold + ChestplatelIni.gold
        else:
            print("Client left without buying.")
    
    elif npcNumber == 4:
        print("Heinz, the town drunk entered the shop. He wants a " + str(BowIni.name) + " and a " + str(Arrows.name) + ".")
        if BowIni.qt >= 1 and Arrows.qt >= 1:
            BowIni.qt -= 1
            Arrows.qt -= 1
            Player.totalgold += BowIni.gold + Arrows.gold

auxwin=False
while auxwin==False:
    #print de informação
    print("Day " + str(Player.day))
    print("Level " + str(Player.level))
    print("EXP " + str(Player.exp))
    print("Money: " + str(Player.totalgold))
    #var auxiliar 
    bought = False
    BuyResourceRecipes(bought)
    CraftingItems()
    SellingItems()
    Player.day=Player.day+1
    Player.auxvar = False