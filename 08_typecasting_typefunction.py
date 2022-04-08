#type function id used to find the data type of the given variable in python
# same as variable type
# use typecasting to convert between acceptable types --->
# a number can be converted to string and vice versa (if possible)
# "31" or '31' is a string literal while 31 is a numeric literal

a = "3434"    # a is a string but can be converted to float or integer
a1 = int(a)
a2 = float(a)
b = "madhavi"
c = 34
c1 = str(c)
#b1 = int(b)

print (type (a))    # ill reurn <class 'str'>
print (type(a1))    # will return <class 'int'>
print (type(a2))    # will return <class 'float'>
#print (type(b1))    # will return ERROR because madhavi is an invalid literal for int()
print (a2+5)        # will return 3439.0   ie float
print (a1+5)        # will return 3439     ie integer
print (type(c1))       # will return <class 'str'>, but value will remain 34