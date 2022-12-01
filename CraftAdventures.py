#projeto realizado por Vitor Daniel e João Carvalho

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

TotalReceitas=0
Resources = {
    "wood" : 5,
    "iron" : 5,
    "leather" : 5,
    "gold" : 1500
    
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
print("Day "+str(Level))
print("Money: "+str(Resources["gold"]))
print("Total Recipes: "+str(TotalReceitas))
print("Wood: "+str(Resources["wood"]))
print("Iron: "+str(Resources["wood"]))
print("Leather: "+str(Resources["leather"]))


def buyresources():
    aux=True
    print("Buy Resources")
   
        
     





