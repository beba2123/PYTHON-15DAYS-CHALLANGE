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
==>> Lists they are ordered sequences that can holds a variety of object types.They uses brackets and commas to separate objects in the list.
[1,2,3,4....]. they also support indexing and slicing.
Eg. my_list = ["Anteneh", 1234, 4543];
print(len(my_list)); output 3;
my_list(1:); out put ->1234, 4543;
==>> in List you can mutate or change a value it isnot like string.
Eg. my_list = ["Anteneh", 'selam'];
my_list[0] = "Abera"; so we can chage it is easily .
so if we say like print(my_list);
["Abera", 'selam']

