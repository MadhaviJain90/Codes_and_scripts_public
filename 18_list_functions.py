list1 = [1, 3, 7, 8.5, -2, 0, 40]
#list method functions come when writing list. <--(dot)
# for permanent changes to lists use overwrite functions first instead of print functions directly
# EG. list1 = list1(sort())

# 1. list length using len(insert_listname) function 
print(len(list1))   # will return 7

# 2. list type
print (type(list1))     # will return <class 'list'>

# 3. list sort in ascending order
print(list1.sort())  #Will update/sort list in increasing order and return "None"
print (list1)  # list will now be returned as [-2, 0, 1, 3, 7, 8.5, 40]
# to arrange list in descending order, first sort in ascending order and then use reverse function

# 4. reverse list and descending order list
list2 = [3, 6, 1, -1, 0, 7]
print("list 2 is:             ", list2)
list2.reverse()
print("reverse list 2:        ", list2)   #lists the list in reverse (end to start order) and not decsending order i.e [7, 0, -1, 1, 6, 3]
list2.sort()   # will update/sort list in ascending order
#list2.reverse   # will reverse ascending order list.. effectively makng descending order list
print("sort list 2:           ", list2)  # will return [-1, 0, 1, 3, 6, 7]
list2.reverse()
print("descending order list2 :", list2)

# 5. append list ... meaning adds one new object at the end of the list. list gets updated automatically.
# will be helpful to run append in loop when using machine learning or web scrapping. it will keep on adding values.
list3 = [0, 4, 6, 2, 8]
print("list 3 was:            ", list3)
list3.append(0)
print ("list 3 is appended to: ", list3)
#list3.append(12, 15, 20, 40)       # will not work
#print("list is further appended: ", list3)   # returns TypeError: list.append() takes exactly one argument (4 given)

# 6. count a certain (only 1) item/ object in the list
print(list3.count(0))  # returns 2, because there are two zeros in the list

# 7. insert(index, newvalue) in list 
list3.insert(2,3)   #insert newvalue = 3 at index = 2
print ("new inserted value at index 2 in list 3:", list3)  #returns [0, 4, 3, 6, 2, 8, 0]

# 8. remove first occurence of a value
list3.remove(0)
print("remove 1st 0 from list", list3)   # removes 1st zero in the list. keeps the last one. use loops to remove all zeros

# 9. pop function in lists. pop will delete item at specified index value and return the updated list
list3.pop(3)   #will delete value at index 3 i.e. 2
print ("list after pop value at index 3: ", list3)

# 10. extend lists meaning one list can be joined by another list
list3.extend(list2)
print ("extend list2 to list3",list3)     #will return 
