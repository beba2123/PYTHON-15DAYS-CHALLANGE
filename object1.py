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

# from abc import ABC, abstractmethod

# class AbstractClass():

#     def __init__(self, name):
#         self.name = name
    
#     @abstractmethod  
#     def Abstract_Speak(self):
#         return self.name + " this is abstract speak, "

# class ConcreteClass(AbstractClass):

#     def Abstract_Speak(self):
#         return super().Abstract_Speak() + " BY Concerete Class. "   

# concerte = ConcreteClass('hi');

# print(concerte.Abstract_Speak())

# class Book():

#     def __init__(self, name, author, page):
#         self.name = name;
#         self.author = author;
#         self.page = page;

#     def __str__(self): # writing the string representation of the class
#         return f"{self.name} by {self.author}";
    
#     def __len__(self):
#         return " The Length of the book is {} ".format(self.page)
    
# book = Book(' python ', ' beba ', 900);
# print(str(book));
# print((len(book)))


# def add(num1, num2):
#     return num1 + num2;

# num1 = 10;
# num2 = int(input('please enter any number: '));

# try:
#     add(num1, num2)
# except:
#     print(' we cannot add integer and string together..!!')
# else:
#     print('oww it seems that you are adding two numbers together..')
#     print(add(num1, num2))

# def ask_for_integer():

#     while True:
#         try:
#             result = int(input('please enter any number..: '))
#         except:
#             print(' it is a word, not a number.. ')
#             continue
#         else:
#             print('oww it is a number ')
#             break;
#         finally:
#             print('end of try/except and also finally.. ')

# print(ask_for_integer())

# import unittest

# def text_cap(text):
#     # return text.capitalize() // captalize only make the first letter on the string.
#     return text.title() #

# class TestClass(unittest.TestCase):

#     def test_one_word(self):
#         text = 'python'
#         result = text_cap(text);
#         self.assertEqual(result, 'Python')

#     def test_multi_word(self):
#        text = 'anteneh alem'
#        result = text_cap(text)
#        self.assertEqual(result, 'Anteneh Alem')
    
# if __name__ == '__main__':
#     unittest.main()  

# import time

# def execution_time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         excution_time = end_time - start_time;
#         print(f" Function {func.__name__} took {excution_time} seconds to excute ")
#         return result
#     return wrapper

# @execution_time_decorator
# def my_function(a, b, c, d):
#     return a + b + c + d;

# print(my_function(334355342135, 513455131340, 32444454, 23425452))


def authorization_decorator(func):
    def wrapper(user):
        if user.is_authenticated:
            return func(user)
        else:
            raise Exception(" User is nott authenticated ")
    return wrapper;

class User:

    def __init__(self, name, is_authenicated):
        self.name = name
        self.is_authenticated = is_authenicated

@authorization_decorator
def delete_user(user):
    print(f"Deleting data for user: {user.name}")

user1  = User('antenh', True)
user2  = User('beba', False)

# delete_user(user1)
delete_user(user2)