from abc import ABC, abstractmethod



class GameCharacter(ABC):
    
    @abstractmethod
    
    def attack(self):
        
	pass


class Warrior(GameCharacter):
    
    def attack(self):
       
	print("Warrior: Swings sword!")

class Mage(GameCharacter):
    
    def attack(self):
        
	print("Mage: Casts a fireball!")
class Archer(GameCharacter):
    def attack(self):
	print("Archer: Shoots an arrow!")
class Healer(GameCharacter):
    def attack(self):
	print("Healer: Casts healing spell on ally!")
warrior = Warrior()
mage = Mage()
archer = Archer()
healer = Healer()
warrior.attack()  
mage.attack()    
archer.attack()  
healer.attack()   