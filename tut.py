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
can convert numbers from one type to another but complex - cannot convert complex to a different type
'''
x = 1   
a = float(x) #convert from int to float
print(a)
print(type(a))

#Random Function
'''
use random function to randomly display a number between 1 and 9'''

import random #need this on the script before u can use the random function
print(random.randrange(1, 10)) #random number displayed


#Python Casting
'''
to specify variable type - int(), float() and string()'''
x = float(1)   # x will be float 1.0 although denoted as an integer
y = str(2.8) # y will be string '2' although denoted as a float
z = int("3") #z will be interger 3 although denoted as a string with ""

print(x, y, z)





