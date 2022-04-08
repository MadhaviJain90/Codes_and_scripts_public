# input function allows the user to take input from the keyboard as a string, even if it is a number

a = input ("Enter Your Name: ")
print (a)     # after running it will ask to enter name in the terminal. Enter the name eg madhavi and press enter
# then it will only return "madhavi" as the answer. ie "a" now has the value "madhavi" stored in it
# just like earthdata asks for username and password when downloading through wget function on cmd.

b = input ("Enter a number: ")    #eg enter the number 25.4
print (b)         #it will print 25.4
print (type (b))   # but the type will not be numeric. It will be <class 'str>


# if the enter number value needs to be an interger then change the type of the variable using typecasting
c = input("Enter a numeric value: ")
c = float(c)   # convert string input value to float typem

print (type (c))    # will return <class 'float'> and the number is successfully converted
