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
