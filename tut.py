#Python Print Syntax
"""
Python Syntax to output data 
"""
print("Hello World")

#python Indentation
'''sometimes python requires indentation 
eg if statement'''
if 5 > 2:
    print("YES")

#Python Variables 
"""assign a valriable 
using variablename = 'variable' variables can be different data types - string, number etc"""
carname ='volvo'
x = 50

'''can display the sum of 2 variables'''
x = 5
y =10
(print(x+y))

'''can create a new variable using data from 2 variables '''
x = 5
y = 10
z = x + y
print(z)

'''can assign values to multiple vairables in one line'''
x, y, z = "orange", 'banana', 'cherry'
print(x,y,z)
 
'''can assign the same value to multiple variables'''
x = y = z = 'orange'
print (x, y, z)

'''define  a global variable - 
created outside a function and can be used in and out of a function'''
x = 'awesome' #global variable
def myfunc():
    print('python is ' + x)

myfunc() 

'''local variable is created inside function 
and can only be used inside function even  if global function with same key present'''
x = 'awesome' #global variable
def myfunc2():
    x ='fantastic' #local variable
    print('python is ' + x) #the x here would be local (fantastic)

myfunc2()
print('python is ' + x) #the x here would be global (awesome) since print syntax is outside the function

'''can make a local variable global
using global function'''
def myfunc3():
    global x
    x = 'amazing'

myfunc3()
print('pyhon is ' + x) #the x here would be local turned global (amazing) even though print syntax outside function

#Data Types
'''to find the data type of your variable
use type()function'''
x = 2  #an integer
print(type(x)) 

x = "Hello World" #a atring
print(type(x))

x = 20.5 #a float
print(type(x))

x = ["apple", "banana", "cherry"] #a list
print(type(x))

x = ("apple", "banana", "cherry") #a tuple
print(type(x))

x = {"name" : "John", "age" : 36} #a dictionary
print(type(x))

x = True #a boolean
print(type(x))

#Python Numbers
'''3 python number types'''
x = 1    # integer (whole number +/-)
y = 2.8  # float (decimals, or 2e4 +/-)
z = 1j   # complex (number+letter (j- imaginary part -check google))

'''can convert numbers from one type to another except complex 
- cannot convert complex to a different type
'''
x = 1   
a = float(x) #convert from int to float
print(a)
print(type(a))

#Random Function
'''use random function 
to randomly display a number between 1 and 9'''

import random #need this on the script before u can use the random function
print(random.randrange(1, 10)) #random number displayed


#Python Casting
'''to specify variable type 
- use int(), float() and string()'''
x = float(1)   # x will be float 1.0 although denoted as an integer
y = str(2.8) # y will be string '2' although denoted as a float
z = int("3") #z will be interger 3 although denoted as a string with ""

print(x, y, z)


#Python Strings
'''strings are always in single or double quotation marks use triple marks for a multiline string
and when you print the multiline string it will be on a the same lines you typed'''
x = 'bottle'
y = "car"
z = '''i am progressing
in python''' # this is still the z variable

'''strings can also be an array 
so can use [] to access elements in the string'''
a = 'Hello'
print(a[1]) #prints the 2nd letter in the string (e) - python starts counting from index 0

'''can loop through a string
using for loop''' 
for x in 'Hello':
    print(x) #loops through each letter in Hello and prints them

'''can search for a character in string
using 'in'  and/or if statement'''
a = 'i am a car'
print ('am' in a) #searches for am inisde the string and outputs true or false if present
print ('am' not in a) #searches and outputs true/false if not present
if 'am' in a: #if statement
    print('yes', 'am ' 'is present')

if 'me' not in a: #if not statement
    print('no', 'me ' 'is not present')

'''slicling strings
returns a range of characters inside the string'''
a = 'Computer'
print(a[1:6]) #loops through string and prints characters at index 1 to 5 (6 not included)
print(a[1:]) #prints everything from index 1 till end
print(a[:6]) #prints everything from start till index 5
print(a[-4:-1]) #prints from index 3 to 1 reading backwards

'''remove space in strings
use strip() function before/after text'''
a = ' Hello, World! ' #space before H and after the !
print(a.strip()) #removes the spaces before H and after !
'''replace strings
using replace() function'''
print(a.replace('H', 'J')) #replaces H with J in Hello World!
'''split strings 
using split() to specify what the separator is 
and charcaters before and after this will be split into different strings '''
print(a.split(',')) #splits Hello and World!

'''To combine a string and a number
-can't do this with +, use .format() function'''
age = 36
name = 'kenny'
txt = 'my name is {} and i am {} years old'
print(txt.format(name, age)) #write in order of variable that should be filled
country = 'England'
txt = 'my name is {1} and i am {0} years old and i live in {2}' #or can use index of txt.format(variable0, variable1 etc) to specify the order
print(txt.format(age, name, country))

'''To insert illegal charcaters into string
eg quotation marks(''), backslash(\), tab(t), new line(n) use the escape character -backslash (\) before the character'''
txt = 'i am \'kenny\' and i am 3' # \ before each quote so that kenny can be 'kenny'


#Boolean
'''to evalutae any value and give true/false 
use bool() function'''
print(bool('hello')) #most values will be true if it has some contents -string, number, list,dict,tuple etc 
print(bool(0)) #value None, number zero, empty list,dict,tuple,string etc are false

'''an object made from a class with a _len_ function that returns 0 or False is False'''
class myclass(): 
    def _len_(self):
        return 0
myobj = myclass()
print(bool(myobj))

'''can execute code based on boolean answer of a function'''
def myfunction():
    return True
if myfunction(): #if myfunction() returns true, print yes
    print('yes')
else:
    print('no')

''' some built in functions can return boolean values 
eg isinstance() function - this determines if an object is of a certain data type'''
x = 200
print(isinstance(x,int)) #checks if x is an interger and returns true or false

#Python Operators
'''to perform operations on variables & values'''
x + 3 #arithmetic operators- +, -, = etc

x += 3  #Assignment operators - assign values to variables - =, >>=, etc
x = x + 3 

x == 3 # comparisom operators - compare values - !=, >, >= etc

x < 5 and x > 10 # logical operators - to combine conditional statements - not, or etc

x = 'apple'
y = 'apple'
z = x
print(x is z) #identity operators - eg is, is not (returns boolean)- compare objects not if they are equal (use == for this) but if they are the same

x = ['apple', 'banana']
print('banana' in x) #membership operators- eg in, not in (returns boolean) - check if a sequence is presented in an object

print(6 & 3) #bitewise operators eg &, |, ~, ^ - compare binary numbers (check google)

'''operator precedence
order in which operators are performed
(), **(exponention), +x -X ~x, * / // %, + -, << >>, &, ^, |,
== != etc, not, and, or (comparison, identity & membership operators),
2 operators with same precedence will be executed left to right'''

#Python Lists
''''ordered, changeable, allow duplicates, index'''
a = list((1, 2, 3)) #use list() function to create new list
print(a)
print(a[0:2]) #use slice syntax to print range of itens in list
if 2 in a: #use in to search for item in list
    print('yes, 2 is in a') 

a[1] = 5 #change value of an item in list
print(a)

a[0:2] = [6,5] #change range of item in list
print(a)

a[0:2] = [3,8,7] #insert items in list - can insert more items than ranged
print(a) 

a[0:2] = [6] #replace multiple items in list with one value
print(a)

'''insert item without replacing values
using .insert() function'''
a.insert(2,6) #.insert(potion index, new value)
print(a)

'''insert item at end of list
using .append() function'''
a.append(6) #.append(new value)
print(a)

'''insert elements from a different iterable object eg list, tuple, dict, sets etc
using .extend() function'''
b = [23,45,56]
a.extend(b) #.extend(list to insert)
print(a)

'''removing items using the actual value
using .remove() function'''
a.remove(3) #if multiple 3 in list, will remove first occurence.
print(a)

'''removing items using the index position
using .pop() function'''
a.pop(3) #will remove value in 4th position (remeber to count form 0), if no index indicated, last item will be removed
print(a)

del a[4] #will calue in 5th position
print(a)

c = [45,46,245,244]
print(c)
del c #to remove whole list #print(c) - will bring error, c is not defined

g = ['boy', 'girl']
print(g)
g.clear() #to clear content in list
print(g)


''' Looping through List'''
'''for loop'''
for x in a: #iterates over each item in list, assign to x and print
    print(x)

'''for loop using index'''
for i in range(len(a)): #loop through the length of the list, assign i to each item and print
    print(a[i]) 

'''while loop using index'''
i = 0
while i < len(a): #loop through length of list, assign i to each item, print and add 1 to i,
    print(a[i])
    i = i + 1 #once i is grater than the length of list, stop loop

'''use for statement and in operator to search inside a list'''

k = ['Egg', 'butter', 'bag', 'cup']
f = []
for x in k: #iterate through all items in k and assign to x
    if 'u' in x: #each item assigned to x searched letter u
        f.append(x) #adding any x item assigned from k list containing letter u into the f list
print(f) 

'''loop using list comprehension
offers shorter syntax for looping through list 
syntax - [expression for item in iterable if condition is true]
-expression -current item/outcome you can manipulate eg print(x)
-condition- not a filter but a way to manipulate the outcome eg for and if statement etc
-iterable -list, dict etc'''

[print(x) for x in a]  #shortend version of for loop


f = [x for x in k if 'u' in x] #shortened version of using for statement and in operator to search inside a list'
print(f)  

f = [x.upper() for x in f] #changes all items in f list to upper case
print(f)  

f = ['wow' for x in f] #sets all items in f list to 'wow'
print(f)  

f = [x if x != 'cup' else 'orange' for x in k] #replaces one item if present
print(f) 

'''sorting lists
using sort() function'''
k.sort() #sorts alphanumerically in acsending order -capital letters first
print(k)

k.sort(reverse = True) #sorts alphanumerically in descending order
print(k)

k.reverse() #reverse order the list not sorting - last item becomes first item

'''can customise sort function
using keyword argument -key = function'''
def myfunc4(n):  #function that will return a no to be used to sort the list
    return abs(n - 50) #sort the list based on how close the item is to 50
number = [100,34,45,3675]
number.sort(key = myfunc4) #the keyword argument
print(number)

'''sort() is case sensitive-
sorts capitals first 
use inbuilt keyword function - .sort(key = str.lower) '''
k.sort(key = str.lower) #sorts alphanumerically in ascending order regardless of case
print(k)

'''copying lists
use .copy() or list()'''
n = k.copy() #copys the lists into a new list n
print(n)

p = list(k)
print(p)

n = k #this can also copy but will be a reference and any changes made to k list will also be made to n

'''joining lists
use +, .append() or .extend()'''
k = ['Egg', 'butter', 'bag', 'cup']
g = ['boy', 'girl']
l = [100,34,45,3675]

w = k + g #add both k and g lists into a new list w
print(w)

for x in k:
    g.append(x) #for each item in k list, add it to g list
print(g)

l.extend(k) #extend l list by adding k list to it
print(l)

#Tuples
'''ordered, unchangeable (can't add/remove items), in (), allow duplicates''',
k = ('dog',) #needs comma even if its just one item otherwise the tuple will be classed as a string'''
animal = tuple(('dog', 'cat', 'pig')) #can use tuple() function to make a tuple too

'''can access tuple like list using index, search (in), for loop, while loop etc'''

'''can add tuple to a tuple'''
human = ('man', 'woman', 'boy', 'girl') #new tuple
animal += human #use += to add human tuple to animal tuple
print(animal)

t = (1,3,5,7)
animalno = animal + t #use + to join 2 tuples and make a new tuple
print(animalno)

multiple = human * 2 #multiplies content of tuple and prints twice
print(multiple)

'''can delete tuple'''
t = (1,3,5,7)
print(t)
del t
#print(t)

'''Tuple unchangeable but theres a way change it, 
need to convert to a list, change then convert back to tuple'''
animal2 = list(animal) #turn tuple into a list
animal2[1] = 'lion' #change item using index
animal2.append('goat') #use .append() to add new item to end of list
animal2.remove('pig') #use .remove to remove an item
animal = tuple(animal2) #turn the list back into tuple
print(animal)

'''Packing a tuple -assigning values
-Unpacking -extract values in tuple back into separate variables'''
t = (1,3,5,7) #packing
(h, g, d, w) = t #unpacking - assigns each item in t tuple into variables corresponding to index of each other
print(h) #assigned to first value
print(g) #assigned to 2nd value etc

(h, *g) = t #use * to assign the rest of the values into a list
print(h) 
print(g) #rest of values in t tuple will be listed as list

(h, *g, d) = t #assigns values between first and last as a list
print(h) 
print(g)
print(d) 

#Python Sets
'''stores multiple items in a single variable
unordered (can't be accessed by index and printed in random order), 
unchangeable - but can add/remove items, 
unindexed, {}, no duplicates- True and 1, False and 0 are also seen as duplicates'''

t = {1,3,1,7, True, False, 0} #duplicate values will be ignored -only one won't be printed
print(t)

g = set((3,5,6,5)) #can use set() to create a set 
print(g)

'''uses same functions as list except when indexing as can't access items in set using index
use for loop and in to search for a value'''
for x in g:
    print(x)

print(3 in g) #remember in returns true/ false if value present

'''add items to set using .add() function'''
g.add(20) #to add items to set

'''add set to another iterable/set
will exclude duplicates'''
b = [5,7,8]
g.update(b) #to add set to another iterable
print(g)

c = {5,7,4,20,19}
g.union(c) #joins two sets
print(g)

g.intersection_update(c) #will only print duplicates present in both sets
print(g) 

d = g.intersection(c) #create a new set with the duplicate values
print(d)

g.symmetric_difference_update(c) #will only print items not present in both sets- so only present in 1
print(g) 

d = g.symmetric_difference(c) #create a new set items not present in both sets- so only present in 1
print(d)


'''using .pop() to delete item will delete random item since sets are unindexed'''
g.pop() #can't add index will give error
print(g)


#Dictionaries
'''ordered(only in python >3.6), chnageable, no duplicates, stores data values in {key:value} pairs'''

d = dict(a = 'b', goat = False, e = ['f', 'g', 3], o = 2345) #dict constructor. can have different data types in dict
print(d)
'''accessing dict values'''
names = {'dog': 'bobby','cat': 'tommy', 'goat': 'robby', 'cat': 'tabby' }
print(names['dog']) #Access values using key



x = names['dog'] #access and store value as a new variable using dict['key']
q = d.get('a') #Access and store value as a nevalues using .get('key')
print(x)
print(q)

print(names['cat']) #value in duplicated key will replace earlier value

print(len(names)) #duplicated keys will be counted as one

x = names.keys() #to return list of all keys 
v = names.values() #to return list of all values
print(x) #x variable will be updated if dict is edited
print(v) #v variable will be updated if dict is edited

'''to edit key/values dictionary'''
names['lion'] = 'milly' #to add new key value pair
names['goat'] = 'cooly' #to change value of a key
names.update({'dog': 'penny'}) #to change key value
print(x) #prints updated keys
print(v) #prints updated values


'''to return each key value pair in dict as a tuple
use .items()'''
x = names.items() #changes made to dict will also be updated in x
print(x)

'''use in to search for key in dict'''
if 'dog' in names:
    print('yes')

'''removing items in dict
use del and .clear() as normal'''
names.pop('dog') #removes key
names.popitem() #removes last key/value pair (item)
del names['cat'] #removes key
print(names)

'''for loop in a dictionary returns the keys not the values'''
names = {'dog': 'bobby','cat': 'tommy', 'goat': 'robby', 'cat': 'tabby' }
for x in names: #assign all keys to x and print
    print(x)

for x in names.keys(): #or use .keys() to access keys
    print(x) 

for x in names: 
    print(names[x]) #use x as index to print all values

for x in names.values(): #or .values() this to access values
    print(x) 

for x,y in names.items(): #or use .items to access key value pairs
    print(x,y) 

'''to copy dictionary
use .copy() or dict(dictname)'''
x = names.copy()
print(x)

x = dict(names)
print(x)

'''Nested dictionaries - dictionary containing a dictionary
create at once or make multiple dicts and combine'''

specienames = {'animal' :{'dog': 'bobby','cat': 'tommy', 'goat': 'robby', 'cat': 'tabby' }, #dictionary within a dictionary
               'human' :{'man': 'robert','boy': 'thomas', 'woman': 'roberta', 'girl': 'tabitha' }}

animalnames = {'dog': 'bobby','cat': 'tommy', 'goat': 'robby', 'cat': 'tabby' }
humannames = {'man': 'robert','boy': 'thomas', 'woman': 'roberta', 'girl': 'tabitha'}

specienames2 = {'animal': animalnames, 'human': humannames} #assign a key to each dictionary (which is the value)
print(specienames2)

print(specienames['animal']['dog'])















































