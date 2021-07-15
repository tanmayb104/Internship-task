'''
Write a Python Program to Access the Parent Class attributes (instance variable) in the Child Class.
1. Parent Class Name-Vehicle
Instance Variable-The constructor for Vehicle must take three arguments: Color, Price, Maximum_Speed
2. Child Class Name-Car
Instance Variable- The constructor for Car must take a single argument: Number of Tires
Instance Method-Prints a string based on the arguments of parent class and child class. The output would be:
A red-colored car with a maximum speed of 200 km/h is priced at 500000 with 4 tires
3. The constructor of a both classes are invoked when we create an object of the class Car.
4. The variables defined within constructor are called as the instance variables. Hence, Color, Price, Max_Speed
are the instance variables of the class Vehicle. Similarly, Number of Tires are the instance variable of the class
Car. Since the class Car inherits from class Vehicle, you have to initialize both class instance variable.
5. Call an instance method of the class Car using its object.
'''

# Parent Class
class Vehicle():
    def __init__(self, Color, Price, Maximum_Speed):
        self.Color = Color
        self.Price = Price
        self.Maximum_Speed = Maximum_Speed

# Child Class
class Car(Vehicle):
    def __init__(self, Color, Price, Maximum_Speed, Number_of_Tires):

        # Invoking the parent constructor
        super().__init__(Color, Price, Maximum_Speed)

        self.Number_of_Tires = Number_of_Tires
    
    # Instance method to show the desired output
    def  display(self):
        print(f"A {self.Color}-colored car with a maximum speed of {self.Maximum_Speed} km/h is priced at {self.Price} with {self.Number_of_Tires} tires")

# Creating a Car object
a = Car("red","500000","200","4")

# Calling instance method through class object
a.display()