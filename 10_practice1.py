######## write a pyhton program to add two numbers
a = input("Enter First Number: ")
a = float(a)
b = input ("Enter Second Number: ")
b = float(b)
c = a+b
print ("The sum is:", c)

####### write a python program to find the remainder when a number is divided by 7
#### use modulus (%) operator 

a = 45
b = 7
print (a%b)

###### use comparison operators to find out whether a given variable a is greater than b or not
a = input("Enter a: ")
b = input("Enter b: ")
c = a>=b
print (c)     # will return a boolean value either True or False


###### write a python program to find the average of two numbers entered by the user
a = input("Enter 1st num: ")
a = float(a)            # remember to convert from type str to float. not int because decimal is needed
b = input("Enter 2nd num: ")
b = float(b)
c = (a+b)/2
print ("the average is", c)

####### write a python program to calculate the cube of a number entered by the user
a = input ("Enter number: ")
a = float(a)
b = a**3
print ("the square of this number is", b)