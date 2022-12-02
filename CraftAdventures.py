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
    pass

class Swords(Item):
    #pelo menos 4 espadas diferentes, 1 iniciante, 1 intermédia e 2 avançadas
    pass

class Shields(Item):
    #pelo menos 3 shields, begginer, intermediate e advanced
    pass

class Armors(Item):
    # 2 tipos de helmet e 3 tipos body armor
    pass

class Gem(Item):
    #valores random por gem ou diferenciadas por classes de cor (red, green and blue)
    pass

class Cloaks(Item):
    #um manto com habilidades mágicas, fazer uso das gems para cada efeito
    #red - boost attack for swords
    #green - boost defense for shields
    #blue - become invisible
    pass

#espada avançada
class LightSaber(Swords):
    pass

#espada avançada
class DualHandedSword(Swords):
    pass

#espada intermédia
class Katana(Swords):
    pass

#espada iniciante
class WoodenSword(Swords):
    pass

#escudo iniciante
class RoundShield(Shields):
    pass

#escudo intermedio
class HeavyShield(Shields):
    pass

#escudo avançado
class EnergyShield(Shields):
    pass

class BodyArmor(Armors):
    pass

#armadura corpo iniciante
class LightArmor(BodyArmor):
    pass

#armadura corpo intermédia
class HeavyArmor(BodyArmor):
    pass

#armadura corpo avançada
class FullBodyArmor(BodyArmor):
    pass

class Helmet(Armors):
    pass

#helmet iniciante
class LeatherHelmet(Helmet):
    pass

#helmet intermédio
class HeavyHelmet(Helmet):
    pass


Resources = {
    "wood" : 5,
    "iron" : 5,
    "leather" : 5,
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

def buyresourcesAndRecipies():
    
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
buyresourcesAndRecipies()

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