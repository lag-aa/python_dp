class Creature:
    pass

class EarthCreature(Creature):
    pass

class Troll(EarthCreature):
    health_points: int = 100

class Elf(EarthCreature):
    health_points: int = 80

class SeaCreature(Creature):
    pass

class Mermaid(SeaCreature):
    health_points: int = 60

class Siren(SeaCreature):
    health_points: int = 75
    
class AirCreature(Creature):
    pass

class Dragon(AirCreature):
    health_points: int = 120

class Pegasus(AirCreature):
    health_points: int = 85
    
# x = Elf()
# print(isinstance(x, EarthCreature))
# print(isinstance(x, Creature))
# print(x.health_points)