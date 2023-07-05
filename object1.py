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

class Circle():
    #first lets instance variable.
    pi = 3.14;

    def __init__(self, radius):
        self.radius =radius;
    #lets calculate perimeter
    def perimeter(self):
        return 2 * pi * self.radius 