Python 15-days challange..

python is dynamic typing which means that we can use built in function like int,Str,..when we assing value  
 we can write it b=4, ant="Anteneh",--> this means like dynamicly typing.
String is a sequence of character, using a syntax of single quote or double quote..
eg. "beba", 'beba'
-->> so due to it ordered sequence we can use slice or index the character inside the string.
Eg. a = "beba";
inorder to know the length of the string len(a);
a[0]==> output -> b using the index method.
a[start:stop:step], start the index that the slice start, stop the index you will go upto but not include, step is the size of the jump you take..
==>> there is a thing called reverse indexing which says it start from the last and start the count from -1;  
==>> also to reverse the string you can use the slicing method a[::-1];
==>> String are immutable which means that we cannot change them .
Eg. a = 'abera'
if we say a[0] = b ==> it create an error becouse due to immutable behavior.
==>> but we can change it like using concatenation method using(+ sign)
Eg. a = 'baba';
b = [1: ]
print(b); the output will be 'aba'
pring(b + 'ba') out-put => ababa
==>>there are diffrent method which uses to change the string property like 'varible name'.upper(), 'variable name'.lower(), 'variable name'.split().
===>> Formating with the .format() method
it one of the way to format object into your string for printing the statements is with the string method.
=> the syntax is print('String here {}'.format('it is'))
->the output is going to be ( String here it is.)
=> we can also insert more than one string inside our formating string.
-> Eg. print('The {f} {b} {q}'.format(f='fox', b='jump', q='quick'));
the out-put will be -> The fox jump quick.
=> but F-Strings or formatted string literals in a new python releases there it change the previous method to
Eg. name = 'Anteneh';
pring(f'My name is {name}');
-> so the output will be My name is Anteneh.
==>> so you can use one of the two method that we like.

                ==>> Lists

they are ordered sequences that can holds a variety of object types.They uses brackets and commas to separate objects in the list.
[1,2,3,4....]. they also support indexing and slicing.
Eg. my_list = ["Anteneh", 1234, 4543];
print(len(my_list)); output 3
my_list(1:); out put ->1234, 4543;
==>> in List you can mutate or change a value it isnot like string.
Eg. my_list = ["Anteneh", 'selam'];
my_list[0] = "Abera"; so we can chage it is easily .
so if we say like print(my_list);
["Abera", 'selam']
==>> there are method that we used in list like 'list name'.append(), 'list name'.pop(), 'list name'.reverse(), 'list name'.sort()

            ==>> Dictionaries

-> they are unordered mapping for storing objects they diffrent than list becouse of this but they use key-value pair which helps the users to quickly grabs objects without needing to know an index location.  
-> they uses a curly braces and : for separte the key and value.
Eg. my_dict = {'value1': 'Anteneh', 'value2': 4543,....};
my_dict['value1'] -->> the output will be Anteneh.
-> dictionaries can hold another dictionaries or lists inside of it.
Eg. my_dict1 = {'value1': [1,2,2,'anteneh'], 'value2': {'name': 'alem'}};
so for accessing it my_dict1[value1][3]
-> inorder to add an elment inside the dictionary.
my_dict1['addAnother'] = 'beba'--->so it will add this to the dictionary.
-> also to override one value we can do like my_dict['value1'] = 'Abera';
-> if we want to know the keys my_dict.keys(); out-put [value1, value2] and also we can do it for the value my_dict.value();

            ===>> Tuples

-> they are like a list however they have one key diffrence this is their immutablity. and they use parenthesis();
my_tuple = (1, 2, 3, 'a', 'b', 'c')
-> they can contains multiple types like integer,string....and you can access them using indexing.
print(my_tuple[3]) --> the output ->a --> also for knowing the index my_tuple.index('a');
-> it also support slicing like
print(my_tuple[2:5]) --> output (3, 'a', 'b', 'c');
-> inorder to know how many times the value is repeating inside the tuple we can do
print(my_tuple.count('a')); -->>out-put 1 ;
->Even if tuple are immutable one but we can concatenate several tuple together
Example
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple) # Output: (1, 2, 3, 'a', 'b', 'c')

Note: Tuples are commonly used when you want to store a collection of items that should not be modified, such as coordinates, database records, or any other situation where immutability is desired.

             ===>> Sets

===>>>set is an unorderd collection of unique elements.unlike lists or tuples,they don't maintain specific order for their element.
Example -> my_set = {1, 2, 3, 4, 5}
==>> set can also be created from another iterable objects like list or tuples ...
Example -> my_set = set(tuple1);
print(my_set); ==>> {1, 2, 3};
==>> they perform some mathimatical operation like union(for joining with other set.), intersect(for finding a value between two sets) and diffrence  
 mylist1= ["Anteneh", 4323, "selam", ];
my_Sets = set(mylist1);
print(my_Sets)
my_Sets1 = {"alem", 22323, "woldegebriel", "Anteneh"};
setUnion = my_Sets.union(my_Sets1);
print(setUnion);
setInters = my_Sets.intersection(my_Sets1);
print(setInters);

===>>> File I/O (file input and output)
->in order to open file.txt first we have to give the directory and then
->1st myfile = ("E:\\Python-30days\\PYTHON-15DAYS-CHALLANGE\\main.txt")
-> then the second step is ->file = open(myfile);
-> so after this we can write or read a file.

->tuples unpacking -> which to unpack tuples that are inside list.
mylist = [(1,2), (3,4)];
for (a,b) in mylist:
print(a);
print(b);
->when we want to iterate using for loop for a dictionary
my_dict = {'value1': 'Anteneh', 'value2': 4543};
for key,value in my_dict.items:
print(value) or print(key);
NOTE-->>the main point is using .items becouse it changes it to a tuple one and we access it using tuple unpacking.

-->> also the note in a while loop ..we  can use it with an else
while condtion:
   print();
else:
   print();

===>> there are some statment in our loops to add additional funtionalty for various cases
  like continue, pass, break.
==>> addition useful oprator
 we use (range operator) in for loop for determinre the index of the loop.
 for num in range(1, 10,2--> for increase the output by 2..):
  print(num)-->it will print out till it reaches 9. it doesnot include 10.

===>>> enumerate is built-in function that allows you to iterate over a sequence(such as list, tuple, or string) while keeping track of the index of each elemeent. 
it return tuples where each tuple contain the index and the corrsponding element from the orginal sequence.
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
the out-put will be like
0 apple
1 banana
2 cherry

===>>> zip operator it is a built in function that allows to combine  multiple  iterable into single iterable tuples.
Example->
fruits = ['apple', 'banana', 'cherry']
prices = [1.0, 0.5, 0.8]
quantities = [5, 10, 3]

zipped = zip(fruits, prices, quantities)

for item in zipped:
    print(item)
==> the output is going to be  
      ('apple', 1.0, 5)
      ('banana', 0.5, 10)
      ('cherry', 0.8, 3)
==> you can convert zip into list function like 
zipped_list = list(zipped);
print(zipped_list);

the out-put
[('apple', 1.0, 5), ('banana', 0.5, 10), ('cherry', 0.8, 3)]

===>>>list comprehension 
->is a concise way to create lists in python.it provides a compact and readable syntax for generating new lists based  on existing iterable, applying condition, and perform transformations.
new_list = [element for element in iterable_name];

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

==> we can use .append in list comprehension
Example  celcius =  [0,10,20,30];
farnheit = [];
   for temp in celcius:
     farnheit.append(((9/5)*temp + 32))
and also we can use it
farnheit = [((9/5)*temp + 32) for temp in celcius]


===>>>*args and **kwargs
->*args  is also known as args or star args that allows you to pass an arbitrary number of arguments to a function.it pass  the format as a tuple argument.

def myfunction(*args):
   return sum((args));

print(myfunction(1,2,3,4)) 

===>>> **kwargs
-> it is called key argument which accept arbitrary number of argument and  return dictionary type to who ever access it.
->def myfunc(**kwargs):
    print(kwargs);
    if 'fruit' in  kwargs:
        print('my favourite fruit is {}'.format(kwargs['fruit']))
   else:
       print('there is no favourite fruit ')
 print(myfunc())

===>>> map
-> map is a built in function that applies to a given function to each item of an iterable like string, tuple, list and returns an iterator that yields the results. map takes two argument the function to be applied and the iterable containing  the elements to be processed.

Example  -> def square(num):
               return num**2;
            my_Nums = [1,2,3,4,5]
            onemap = list(map(square, my_Nums));
            for items in onemap:
                print(items);
               
===>>> filter 
-> it is used to filter out a value inside a list  or any iterable object based on the function  requirment.
Example -> def check_even(num):
               return if num % 2 == 0;
            my_num = [1,3,4,6,4,2,1];
            my_filter = list(filter(check_even, my_num));
            print(my_filter)