'''
1. arithmetic operators ---> +, -, *, /, ** (power), % (Modulus: returns the remainder when the first operand is divided by the second)
2. assigned operators ----> =, +=, -=, *= etc 
## (compute value as per opertor to the defined variable and replace 
and store this new value in the variable.)
3. comparision operators ----> ==, >, <, >=, <=, != (not equal to)
4. logical operators  ----> and, or, not etc
'''
a = 3
b = 4
c= a+b
print ("c =", c)     # string "c =" gets printed as it is and 
#                    c is an expression a + b which gets calculated and then printed

d = 5
d += 2      #assigned operator
d *= 5
print ("d =", d)   # will return d = 35  i.e., 5+2=7*5=35 

e = (4>=7)
print ("e = ", e)   # will return e = False

f = 14>7
print ("f =", f)   # will return True