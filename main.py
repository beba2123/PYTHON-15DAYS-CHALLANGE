# a = "beba is a good guy";
# print(len(a));
# print(a[0]);
# print(type(a))
# print(a[2: ]); #start from the index 2 and go untill the last index.
# print(a[ :10]);

# mylist1= ["Anteneh", 4323, "selam"];
# mylist2 = ['abeba', 4793, 'alem'];
# print(type(mylist1));
# total_list = mylist1 + mylist2;
# print(total_list);

#dictionary

# my_dic = {'name': 'Anteneh', 'age': 23}; #it is used to store key and value pair.
# print(my_dic['name']);

# my_dict1 = {'key1': [1,2,12,'anteneh'], 'key2': {'name': 'alem'}};
# print(my_dict1['key2']['name'].upper()) 

#set
# mylist1= ["Anteneh", 4323, "selam", ];
# my_Sets = set(mylist1);
# print(my_Sets)
# my_Sets1 = {"alem", 22323, "woldegebriel", "Anteneh"};
# setUnion = my_Sets.union(my_Sets1);
# print(setUnion);
# setInters = my_Sets.intersection(my_Sets1);
# print(setInters);


#
# myfile = ("E:\\Python-30days\\PYTHON-15DAYS-CHALLANGE\\main.txt")

# file = open(myfile);

# print(file.readline())
# # print(file.seek(0))
# # print(file.read())
# with open(myfile,'r') as file:
#     content = file.read;
#     print(content);
# # print(file.close)
# with open('file', mode='a') as file1:
#     file1.write('\n  anteneh is gangstar');
# with open('file', mode='r') as file1:
#     print(file1.read())
# file1.close()

#loop(for, if)
# my_iterable = [1,2,3,4,5,6,7,8,9,10];
# sum =0;
# for num in my_iterable:
#     # if(num %2 == 0):
#     #     print(f' even number: {num}');
#     # else:
#     #     print(f' odd number: {num}');
#     sum += num
#     print(sum)
# print(f'sum of the num :=> {sum}')

# mylist = [(1,2), (3,4)]; 
# for (a,b) in mylist: #this is called tuple unpacking
#     print(a);
#     print(b);

# my_dict = {'value1': 'Anteneh', 'value2': 4543};
# for ket,value in my_dict.items():
#     print(value)
# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# age = input("Enter your age: ")
# print("You are " + age + " years old.")
# int(age)
# print(type(age));

# list comprehension
# my_string = [2,3,4,5,6];
# my_stringList = [str**2 for str in my_string];
# print(my_stringList);

# my_list = [num for num in range(1,10)  if(num % 2 != 0)];
# print(my_list)

# my_list = [num for num in range(1,50) if(num%3==0)];
# print(my_list)

# for num in range(1,50):
#     if(num % 3 == 0):
#         my_list.append(num);
# # print(my_list);
  
# def check_even(mylist):
#     for list in mylist:
#         if(list % 2 == 0):
#           return ('one of the numbers are even!!');
#         else:
#            pass
#     return ('this is odd')

# mylist = [1,2,3,4,5,6];
# print(check_even([1,2,5,7,9]))

# mylist  = [1,2,3,4,5,6,7,8,9];

# def check_even(mylist):

#     #creating placeholder
#     new_even_list = [];
#     new_odd_list = [];
#     #then iterate through the given list
#     for list in mylist:
#         #if he find an even number it is going to  append in the placeholder 
#         if list % 2 == 0:
#             new_even_list.append(list)
#         else:
#             new_odd_list.append(list)
#     return (new_even_list, new_odd_list)
# print(check_even([1,2,3,4,5,6,7,8,9]))

# working_hours = [('anteneh', 200), ('beleta', 5000), ('seleshi', 700)];

# def employer_check(working_hours):
#     check_hour = 0;
#     employer_month = '';
#     for keys, value in working_hours:
#         if value > check_hour:
#             check_hour = value;
#             employer_month = keys;
#     return (employer_month, check_hour);

# print(employer_check(working_hours))
# from pickletools import pylist
# from random import shuffle

# my_list = ['', '0', ''];

# def shuffle_list(mylist):  #this function is for shuffle the given list
#     shuffle(mylist)
#     return mylist
# def player_guess():  #then make the player guess.
#     guess = ['']
#     while guess not in ['0','1','2']:
#         guess = input("please pick a number between: 0,1 and 2 ?")

    
#     return int(guess)
# guess = player_guess()
# print(guess)
# def check_guess(my_list, guess):
#     shuffle_list(my_list)
#     if my_list[guess] == '0':
#         print('your guess is correct..')
#         print(my_list)
#     else:
#         print('you are wrong...')
#         print(my_list)

# print(check_guess(my_list, guess))

# def myfunction(*args):
#  sum = 0;
#  for item in args:
#        sum += item;
#  return sum;   

# print(myfunction(1,2,3,4));

# def myfunc(**kwargs):
#     print(kwargs);
#     if 'fruit' in  kwargs:
#         print('my favourite fruit is {}'.format(kwargs['fruit']))
#     else:
#        print('there is no favourite fruit ')
# print(myfunc(fruit= 'apple', name= 'anteneh'))

    #map
# def square(num):
#      return num**2;
# my_Nums = [1,2,3,4,5]
# onemap = map(square, my_Nums);
# print(list(onemap))
# def splic(myString):
#      if len(myString)%2 == 0:
#           return('EVEN');
#      else:
#           return(myString[0]);

# mylist = ['anteneh', 'alem', 'abeba'];

# print(list(map(splic, mylist)));

   #filter
# def check_even(num):
#    return num % 2 == 0;
# my_num = [1,3,4,6,4,2,1];
# my_filter = list(filter(check_even, my_num));
# print(my_filter);