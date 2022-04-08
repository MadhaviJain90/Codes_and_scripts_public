# use square brackets to access a specific indexed character in the string. 
name = "Madhavi"
print (name[6])   # will return i and not v, because string index starts from 0.  
#print (name[7])   # will return string index out of range in this case.

## changing an indexed string does not work
# name[3] = "d" will not replace h in Madhavi to d.  # TypeError: 'str' object does not support item assignment

print (name[1:4])     # [n,m] will return sequence of characters from index n to index m-1
# i.e index 1 to index 4-1= 3. i.e answer will be 'adh' 

print (name[:3])    # will automatically start from first index (0) and end at 3-1 character. ie. Mad
print (name[1:])    # will automatically end at the last index i.e. adhavi

## negative indexing -1, -2, -3,.... 
# starts from -1 (for the last indexed character e.g. in madhavi -1 index is i and -7 index is m
# negative indexing helps when a character from the end needs to be accessed but length is unkwown 
# or string needs to be sliced from back to front string direction 

print (name[-7])    # will return M
print (name[-7:])   # will return Madhavi
print (name[-6:-3]) #will return adh


################## slicing with skip value ##############
# we can provide a skip value as part of our slice as the third value in the []
# eg. word = amazing       
# word [1:6:2] ie skip every 2nd charac startng from index 1 and will return 'mzn'

print (name[0:6:2])  # will return Mda
print (name[::3])   #blanks mean automatic start and end at skip by 3 will return 'Mhi'