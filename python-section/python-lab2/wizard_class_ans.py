##Homework:
## 
## Create a sub class, Wizard that inherits the super class Character
## Use super() to bring in all the data/methods from Character
## Add a max_hp value that is set to the original value of the wizard hp
## Add 2 methods to wizard
## (1) heal - that makes hp = max_hp
## (2) fireball - It is like the Attack method, but subtracts a random
##     integer between 100 and 500 to other. 
import random


class Character:
    
    def __init__(self, name='', hp=0, attack=0, **kwargs):
        self.name = name
        self.hp = hp
        self._attack = attack

    #Change operator overloader to print the attack value.    
    def __str__(self):
        return "Name: " + self.name + "\nHP:" + str(self.hp) + "\nAttack: " + str(self._attack)

    def attack(self):
        return self._attack

    def Attack(self, other):
        other.hp-=self._attack
        print(other.hp)


class Wizard(Character):
    
    def __init__(self, name, hp, attack):
        super().__init__(name,hp,attack)
        self.max_hp=self.hp

    def heal(self):
        self.hp=self.max_hp

    def fireball(self,other):
        damage=random.randint(100,500)
        other.hp-=damage
        print(other.hp)
    
##TEST with the following code###

if __name__=="__main__":
    weezle=Wizard('Weezle',20,5)
    grognak=Character('Grognak',250,300)
    print(weezle)
    print(grognak)
    grognak.Attack(weezle)
    print(weezle)
    weezle.Attack(grognak)
    print(grognak)
    weezle.heal()
    weezle.fireball(grognak)
    print(weezle)
    print(grognak)
    print(str(weezle.attack()))

    
