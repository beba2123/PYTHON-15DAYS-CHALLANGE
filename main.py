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
mylist1= ["Anteneh", 4323, "selam", ];
my_Sets = set(mylist1);
print(my_Sets)
my_Sets1 = {"alem", 22323, "woldegebriel", "Anteneh"};
setUnion = my_Sets.union(my_Sets1);
print(setUnion);
setInters = my_Sets.intersection(my_Sets1);
print(setInters);