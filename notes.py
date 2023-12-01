a = True
print(type(a)) #type gives type basically
b = complex(124, 43) #complex number in a+bj form
print(b, type(b))
print(5**2) #5 ki power 2
print(5//2) # will return integer, removing decimal part

#typecasting

a1 = "1"
a2 = "2"
print(a1 + a2) #it will give "12" bcz a1 and a1 are strings not a number
b1 = 1
b2 = 2
print(b1 + b2) #it will give 3 bcz b1 and b2 are numbers

print(int(a1)+int(a2)) #it will give 3 bcz a1 and a2 are now converting into a number from string using "int" keyword(this is known as explicit typecasting)

c1 = 2
c2 = 2.2
print(c1 + c2) #will print 4.2  and float variable takes more memory than integer value so it will typecast it into float (this is known as implicit typecasting)
float_number = 1.096
print(f"{float_number:.2f}") #will print upto 2 decimal places (will round off the number also)[if 0.00-0.05 then it will give 0.0 else if 0.06-0.09 it will give 0.1 assuming number will be printed upto 1 decimal place]
#input() will take input in string

multi_line_string = '''hey,
my name is Akshat.
And today i'm learning python''' 
# with triple ' or triple " we can make a multiline string.
print(multi_line_string)

string_example = "Hello_World"
print(string_example[0]) #will print "H", string is LIKE an array of characters not exactly an array.

print(string_example[0:5]) #will print "Hello" (from 0th position to 4th position)
print(len(string_example)) #will give length of the string
print(string_example[0:-5]) #will give "Hello_" (-5 means:- length of string-5 automatically in py)
print(string_example[0:len(string_example) -5]) # same thing as above
print(string_example[-11:-5])  #will give "Hello_" (-5 means:- length of string-5 automatically in py)
print(string_example[len(string_example)-11:len(string_example)-5]) # same thing as above

#strings are immutable
Example  = "Hello_hi_BYE____"
# .upper() will convert string to uppercase
print(Example.upper())
# .lower() will convert string to lowercase
print(Example.lower())
# rstrip("character") will remove the character inserted from the END of the string
print(Example.rstrip("_")) # it will remove "_" from the END of the string
# .replace() will replace all occurances
print(Example.replace("_","!"))

Example1 = "hey! my name is Akshat"
print(Example1.split(" ")) #it will make a list of every element in the variable splitting [spaces (" ")]
print(Example1.capitalize()) #it will capitalize first letter of the sentence and also lowercase following elements
print(Example1.center(50,"-")) #centers the element using spaces
print(len(Example1.center(50)))
print(len(Example1))
Example2 = "Hello, hihlo, Hi, hey"
print(Example2.count("h")) #returns the number of occurances in the string, it is case sensitive also\
print(Example2.endswith("ey")) #returns true 
print(Example2.endswith("lo",2,5)) #returns true starts from index number 2 and 5
print(Example2.startswith("H")) #returns true if first character of string is present otherwise false(index method also works in this)
print(Example2.find("hi")) #returns index number of first occurance (if there is no occurence than it will return -1)
# .index() will do the same thing as .find() but .index() will throw an error is no occurence is found
Example3 = "HelloWorld123"
print(Example3.isalnum()) #if string contains A-Z,a-z,0-9 numbers ONLY then it will return true otherwise false
print(Example3.isalpha()) #if string contains A-Z,a-z letters ONLY then it will return true otherwise false
print(Example3.islower()) #if string contains all lowercase letters than it will return true otherwise false

Example4 = "HeyEveryone!\n"
print(Example4.isprintable()) #if all characters are printable then it will return true otherwise false
Example5 = "        "
print(Example5.isspace()) #returns true if string contains ONLY space otherwise false

Example6 = "Hey! My Name Is Akshat" 
print(Example6.istitle()) #returns true if first character of every word is capital otherwise false
print(Example6.swapcase()) #converts lower to uppercase and upper to lowercase

Example7 = "this is a title"
print(Example7.title()) #converts every first letter of every word to capital

import time
timestamp1 = int(time.strftime('%H'))
timestamp2 = int(time.strftime('%M'))
if(timestamp1 >= 21):
    print("Good Night")
elif(timestamp1 >= 12):
    print('Good evening')
elif(timestamp1 >= 5):
    print("Good Morning") 
print("{}:{}".format(timestamp1,timestamp2))           


#match case in python (like switch cases in c & c++)

day = int(input("Enter number from 1 to 7 for getting a day:- "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print('Thursday')
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input!!")  #default case if any case isn't executed  


 # Loops in python
 # for x in (stringname,listname , range(starting number,ending number + 1, increment value) , etc)
for variable in range(0, 20000, 2):
   print(variable) 
# while loop same syntax as c 
   
def average(a=2,b=11): # 2 , 11 will be default values if any values are NOT passed during function call
  return (a+b)/2

print(average(4,6)) # 4 and 6 will be executed as values in function call has more priority

def sum(*x):   #you can pass multiple values using * in a function and access them by a loop
    sum = 0    # *x will be a tuple of all the values passes in the function
    for i in x:
        sum = sum + i
    return sum

print(sum(1,2,3,4,5,6))  #you can pass multiple values using * in a function and access them by a loop      

# lists methods
example_list = [1,2,3,4,5,True,False,"Hello"]
print(example_list[0:6])
print(example_list[0:9:2])

l = [7,6,2,4,5,3,1,0,0,0,0]
l.append(8) #will add element in the last of the list
print(l)
l.sort()
print(l) #will sort the list, list must contain either only strings values OR ONLY number values
# l.sort(reverse=True) will sort in descending order
# "".join() will join the list elements and convert it into a string and will join with the given input between ""(all list elements should be a string)
print(l.index(4)) #it will print the index position of number 4 in the list.
print(l.count(0)) #it will count number of occurances of the given element in the list.


m = l
m[0] = 22
print(l) #22 will reflect back in original "l" list
m = l.copy()
m[0] = 44
print(l) # now any changes wont be reflected back in l

new_list = [1,4,5,7,2,4,1,67,9,4]
new_list.sort()
new_list.insert(2,"inserted element") #inserts element on given index in a list.
print(new_list)
new_list2 = ["elem1","elem2","elem3"]
new_list.extend(new_list2) #appends a list in the end (can also append itself)
print(new_list)

list1 = [1,3,5,6]
list2 = [3,5,6,8,9]
k = list1 + list2 #changes won't be reflected in original list and two list can be concatinated and assigned it to a new variable(no need to use .copy())
print(k)

# Tuples
# tuples are immutable
example_tuple = (1,2,4,5,6,"hello","hi") #values in tuples can't be updated 
print(example_tuple[5])

if "hi" in example_tuple:  # can be done with list too

    print("Yes")

example_tuple2 = example_tuple[2:6] #example_tuple is sliced and stored into example_tuple2
print(example_tuple2)

ex_tuple1 = (1,2,4,5)
ex_tuple2 = ("hello","hi","bye")

concat_tuple = ex_tuple1 + ex_tuple2 # you can concat two tuples 
print(concat_tuple)
tuple_one_elem = (1,) #tuple with one element is has a coma after the element


tuple1 = (100,101,102,103,104,105)
converted_list = list(tuple1) # converts tuple into list and assigns it to a variable BUT doesn't convert the original tuple into list.
converted_list.pop(0)
converted_tuple = tuple(converted_list)
print(converted_tuple) 
# .count() works 
# .index(element, starting index, ending index) works
# len() works

#f-strings

letter = "My name is {} and my age is {}"
name = "Akshat"
age  = 18
print(letter.format(name,age)) #method 1

letter1 = f"hey {name}! Your age is {age} so you can drive." #method 2
print(letter1)
print(f"hello {{name}}") #to print f-string (might be useful in the future somewhere)
def power(a,b):
    """take 2 numbers and returns there power a^b 
    """                                              #doc-string should be right below the function name or right above the function body
    print(a**b)
power(4,2) 
print(power.__doc__)

#Recursive Functions

def recursive_function1(n):
    
    if(n >0):
     recursive_function1(n-1)
    print(n)
recursive_function1(10) 



def recursive_function2_factorail(x):
    if(x == 1 or x==0):
        return 1
    else:
       return (x * recursive_function2_factorail(x-1))
    

print(recursive_function2_factorail(5))    

# Sets
s = {1,2,3,2,1,3,4}  #sets won't repeat values and are unordered (no idea how the elements might be ordered)
print(s)
empty_set = set() # This is how empty set is declared

# Set methods
s1 = {2,3,4,5}
s2 = {2,4,5,6,7,100,9}
print(s1.union(s2)) #will print union (all elements in both the sets[common one's will be printed only 1 time]) won't reflect back in s1 or s2

s1.update(s2) # basically adding two sets s1 = s1 + s2 (union)
print(s1) # it will give both elemnts of itself as well as s2

q1 = {1,2,3,4,5,6}
q2 = {2,4,6,8,10}
print(q1.intersection(q2)) #intersection of two sets (elements that are same in both sets)

q1.intersection_update(q2) #intersection of two sets (elements that are same in both sets) (reflects back in q1)
print(q1) # (reflects back in q1)

w1 = {2,3,4,5}
w2 = {3,4,6,7,8}
print(w1.symmetric_difference(w2)) #will print all elements in both sets EXCEPT the common ones in both

w1.symmetric_difference_update(w2) #will print all elements in both sets EXCEPT the common ones in both(updates w1)

print(w1) # (reflects back in w1)
e1 = {1,2,3,4}
e2 = {2,3}
print(e1.difference(e2)) # e1 - e2 

e1.difference_update(e2) # e1 - e2 (reflects back in e1)

print(e1)

z1 = {1,2,3,4}
z2 = {5,6,7,8}
print(z1.isdisjoint(z2)) # will print True bcs no intersection b/w the two sets z1 & z2

print(z1.issuperset(z2)) # will print False bcz z1 is not superset of z2
x1 = {1,2,3,4}
x2 = {2,4}

print(x1.issubset(x2)) # will print False bcz x1 is not subset of x2

x2.add(3) # adds element in a set
x2.remove(2) # removes element from set
x2.discard(2) # difference b/w remove and discard is that if element is not present in the set then remove will give error whereas discard won't
# .pop() will remove last element from the set but as sets are unordered any element can be the last element and any element might get removed
# .pop() can beused for accessing a random element in the set and removing it also
# del set_name will delete the entire set
# .clear() will remove all items in the set


# Dictionarys in python
empty_dic = {}

dic = {
    "Name":"Akshat",
    "Age": 18,
    "Lname": 'Jain'
} # dictionarys are ordered

print(dic) # will print dictionary


print(dic["Age"]) # will print value of the key given in dictionary
print(dic.get('Age')) # will print value of corresponding key but won't give error IF key doesn't exist and will print 'None'

print(dic.keys()) # will print all the keys in the dictionary
print(dic.values()) # will print all the values in the dictionary

for key in dic.keys():
    print(f"{key} : {dic[key]}")


dic1  = {
    "Name":"Akshat",
    "Age": 18,
    "Lname": 'Jain'
}

print(dic1.items()) # will print key : value pairs

ep1 = {
    1:99,
    2:32,
    3:67,
    4:89,
    5:69
}
ep2 = {
    6:67,
       7:89,
       8:88
       }
ep1.update(ep2) # ep1 = ep1 + ep2

print(ep1)
ep2.clear() # clears all key:value pairs in the dictionary
print(ep2)
ep1.pop(1) # it will remove the particular key:value pair in the dictionary
print(ep1)
ep1.popitem() # will remove the last key:value pair in the dictionary
print(ep1)

# del dictionary_name will delete the whole dictionary
# you can also del using a key (del dic_name['key_name']) will delete the key:value pair

# else keyword can be used with for and while loops
# else block will execute when the WHOLE loop is executed (all iterations are executed AND loop isn't breaked out using "break" keyword.)
for i in range(6):
    print(i)
    if i == 5:
        break
else:
    print("loop is fully executed") # it will not execute bcz loop is breaked using break keyword despite executing all iterations


x =  input()
try:
    for i in range(11):
        print(f"{int(x)} X {i} = {int(x)*i}")  #it will try to execute the code inside the try block and if any error occurs the transfers control to the except block.
except Exception as any_name: #you can print the error message customly or also print the error the compiler is giving using "Exception" keyword using variable_name and printing it.
    print(any_name)
    print("this is custom message when error is occuring")
print("these are lines after the try-except blocks of codes are executed")   
# except ValueError: will execute when value entered is giving the error
# except IndexError: will execute when index is out of range in and array

try:
    abc =  int(input('enter a number:- '))
except:
    print("error")
finally: # this block is always executed no matter what! (used in functions when you want to do something even after returning a value)
    print("this satements will be executed always!!")        

h =  int(input("enter number(if value is b/w 5 to 10 then custom error will be raised!!):- "))
if(h>5 and h<10):
    raise ValueError("This is a custom error ( no lines below it will be executed!!)")

h1 =  input("enter string \'quit\':- ")
if(h1 != "quit"):
    raise ValueError("value should be \'quit\' string!!")
    

g1 = int(input("Enter number:- "))
g2 = int(input("Enter number:- "))
print(f"{g1} is greater than {g2}") if g1>g2 else print(f"{g1} is less than {g2}") if g2>g1 else print(f"{g1} is equal to {g2}") #short hand if else statments
# for using short hand if statement using (else "" )is a compulsion otherwise syntax error will occur.

i1 = 10 if g1>g2 else 20 #short hand if else statements can also be used like this!!
print(i1)

marks = [10,20,22,43,21,54,88,32,45,67,77,38,91,21]
for x,y in enumerate(marks): # this will use 'x' as index number and 'y' as value in the list
    print(f"Index:{x}, value:{y}") 

marks1 = [10,20,22,43,21,54,88,32,45,67,77,38,91,21]
for i,j in enumerate(marks1, start=2): #start will start the iteration from the given value!
    print(f"Index:{i}, value:{j}") 
        
# you can import functions from other files of python using "import file_name"
# IMP--->  using if __name__="__main__": will avoid executing the function calss if any in thee other module/file when imported


# xyz = open('text_filename.txt','r') [r for reading, w for writing, a for appending in the last of the file]
f = open('text_file.txt','r') # for jpg,pdf etc files use 'rb'
text = f.read()
print(text)
f.close()
o = open('text_file.txt','w') # write will change the whole file and newly write it
text1 = o.write('hello!!')
o.close()

d = open('text_file.txt','a') # append will add the text in the last of the original file
text2 = d.write('HELLO!!')
d.close()

# close is important
with open('text_file.txt','a') as any: # this will automatically close
    any.write('27')


line = open('text_file.txt','r')
for i in range(0,3):
    line1 = line.readline() # the number of times readline is called it iterates toh the next line in the file
    print(line1)
line.close()    


# map,filter and reduce

def cube(x):
    return (x**3)

num_list = [1,2,3,4,5,4,3,2,1]
num_list_cubed = list(map(cube,num_list))  # map uses the function on every item in a list,tuple and you will have to typecast it from object to list or the desired data type
print(num_list_cubed)
def filter_fun(x):
    return x%2==0
num_list_filtered = list(filter( filter_fun,num_list)) # iterates over the list, if base condition is flase then element is deleted
print(num_list_filtered)

from functools import reduce
# 'reduce' reduces the list.tuple to one element