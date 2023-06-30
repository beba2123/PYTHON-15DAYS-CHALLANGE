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

