#Python Print Syntax
"""
Python Syntax to output data 
"""
print("Hello World")

#python Indentation
'''
sometimes python requires indentation eg if statement
'''
if 5 > 2:
    print("YES")

#Python Variables 
"""
assign a valriable using variablename = 'variable' 
variables can be different data types - string, number etc
"""
carname ='volvo'
x = 50

'''
can display the sum of 2 variables
'''
x = 5
y =10
(print(x+y))

'''
can create a new variable using data from 2 variables 
'''
x = 5
y = 10
z = x + y
print(z)

'''
can assign values to multiple vairables in one line'''
x, y, z = "orange", 'banana', 'cherry'
print(x,y,z)
 
'''
can assign the same value to multiple variables'''
x = y = z = 'orange'
print (x, y, z)

'''
define  a global variable - created outside a function and can be used in and out of a function'''
x = 'awesome' #global variable
def myfunc():
    print('python is ' + x)

myfunc() 

'''
local variable is created inside function and can only be used inside function even  if global function with same key present'''
x = 'awesome' #global variable
def myfunc2():
    x ='fantastic' #local variable
    print('python is ' + x) #the x here would be local (fantastic)

myfunc2()
print('python is ' + x) #the x here would be global (awesome) since print syntax is outside the function

'''
can make a local variable global'''
def myfunc3():
    global x
    x = 'amazing'

myfunc3()
print('pyhon is ' + x) #the x here would be local turned global (amazing) even though print syntax outside function

#Data Types
'''
to find the data type of your variable'''
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
'''
3 python number types'''
x = 1    # integer (whole number +/-)
y = 2.8  # float (decimals, or 2e4 +/-)
z = 1j   # complex (number+letter (j- imaginary part -check google))

'''
can convert numbers from one type to another except complex 
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
'''
to specify variable type - int(), float() and string()'''
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
txt = 'my name is {1} and i am {0} years old and i live in {2}'
print(txt.format(age, name, country))













































