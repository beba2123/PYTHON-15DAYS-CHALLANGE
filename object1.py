#in this python file ww gonna see object oriented programming.
# class Beba():

    #define init method..
#     def __init__(self, name, age): 
#         self.name = name;
#         self.age = age;

#     def univer(self, UniName):
#         self.UniName = UniName;


# PersPro = Beba('Anteneh', 34);
# PersPro.univer('AASTU')
# print(' My name is {} and i am {} years old and i graduated from {} . '.format(PersPro.name, PersPro.age, PersPro.UniName));

# class Circle():
#     #first lets instance variable.
#     pi = 3.14;

#     def __init__(self, radius):
#         self.radius =radius;
#         self.area = Circle.pi * radius * radius;
#     #lets calculate perimeter
#     def perimeter(self):
#         return 2 * self.pi * self.radius 
#     def area1(self):
#         return self.pi * self.radius * self.radius;

# circle = Circle(30);
# print(circle.area)
# print("the perimeter of the circle {} and the area of the string is gonna be {}" .format(circle.perimeter() , circle.area1()))

# class Cat():

#     def __init__(self, name):
#         self.name = name;
#     def Sound(self):
#         return (self.name + ' says Meow..')

# class Dog():

#     def __init__(self, name):
#         self.name = name;
#     def Sound(self):
#         return (self.name + ' says wooof....')
    
# dog = Dog('biku')
# cat = Cat('shershta');

# print(cat.Sound())
# print(dog.Sound())

# def Speak(Animal):
#     return (Animal.Sound())

# print(Speak(dog)) 

from abc import ABC, abstractmethod

class AbstractClass():

    def __init__(self, name):
        self.name = name
    
    @abstractmethod  
    def Abstract_Speak(self):
        return self.name + " this is abstract speak, "

class ConcreteClass(AbstractClass):

    def Abstract_Speak(self):
        return super().Abstract_Speak() + " BY Concerete Class. "   

concerte = ConcreteClass('hi');

print(concerte.Abstract_Speak())