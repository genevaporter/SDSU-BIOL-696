#Charactes class

class Character:
    def __init__(self, name='', hp=0, attack=0, **kwargs):
        self.name = name
        self.hp = hp
        self._attack = attack

    #Change operator overloader to print the attack value.
    
    def __str__(self):
        return self.name + str(self.hp)
    
    def attack(self):
        return self._attack

    def Attack(self, other):
        other.hp-=self.attack
        print(other.hp)
        
    def inspect(self):
        print('{0.name} HP and {0._attack} Attack.'.format(self))

#Use if __name__=="main": to
#(1) Done: Make an object 'grognak' with name "Grognak" 250 hp and 300 attack
#(2) Make object 'weezle' with "Weezle", 20 and 5 but also magic=100
#(3) print both grognak and weezle
#(4) have grognak Attack weezle
#(5) run weezle.inspect


if __name__=="__main__":
    grognak=Character('Grognak',250,300)
    print(grognak)
    

    
