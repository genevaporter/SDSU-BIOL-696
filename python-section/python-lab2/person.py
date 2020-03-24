class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    ##Add operator overload for print that prints
    ##First Name: firstname
    ##Last  Name: lastname
        
    def __str__(self):
        return "First Name: " + self.firstname + "\nLast Name: " + self.lastname + "\n"

#Make Super class "Empolyee" that inherits Person
#In the constructor, grab all the Person methods using the super() method
#Add a new variable to the __init__ -> staffnum
#Overload __str__ with super and add "Staff Number: staffnum"

bob=Person('bob','zeller')
print(bob)
