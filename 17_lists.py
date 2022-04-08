##       1. python lists are containers to store a set of values of any data type
# CREATE LISTS USING SQ BRACKETS []
#eg. friends = [110, "manisha", "mom", "motu", 7, 10, False, None]

emptylist = []
filllist = [1, 4]
emptylist.extend(filllist) # will return [1, 4] in emptylist
print("empty list is now filled: ",emptylist)

##       2.  list indexing
# lists can be indexed just like a string. Indexes start from 0
list1 = [110, "motu", "manisha", 70, 2]
print(list1[2]) ### will return = manisha and not motu
#print (list1[5]) ## will return Error: list index out of range

# 3. include strings within quotes just like the way in variable or print function. Numeric & boolean dont need quotes

# 4. Lists are ordered. meaning the sequence of entitites in the list container will not change
#eg list = [1, 10, 2, 4, 3]   # print(list) will return [1, 10, 2, 4, 3] and not [1, 2, 3, 4, 10]

# 5. lists can be edited/ updated
a = [-1, 4, -8.5, 0, 45]
print (a)
a[0]= 20       # to edit/update the first entry of the list
print (a)      # will now return [20, 4, -8.5, 0, 45]
a[1:4] = -5, 7, "MADHAVI"      #to edit index values 1 to 3 (n-1)
print (a) 
#a [0, 2:4] = 1, 1, 1     # wont work
#print (a)                # will return TypeError: list indices must be integers or slices, not tuple

#   6. LIST SLICING
# lists can be sliced in the same manner as string slicing
b = ["motu", "tom", "sam", 8, 67, "mom"]
print(b[0:4])    #will print index 0, 1, 2, and 3 ...i.e ['motu', 'tom', 'sam', 8] 
print(b[::2])    #will return ['motu', 'sam', 67]  start to finish of list, but skip every 2nd value
print(b[-3:])    #will return [8, 67, 'mom']... i.e index -3, -2, and -1

#   7. list methods e.g sorting, reversing, appending, inserting etc are very important and widely used list functions
#refer to 18_list_functions.py