#### tuples
# tuples are written in simple brackets ()
# unlike lists, tuples when once defined are 'immutable' meaning they can not be changed

emptytuple = ()   #empty tuple with () brackets
a = (1, )    #tuple with one element needs a comma
a1 = (5)  # will not be recognized as tuple but as a number.. REMEMBER COMMA IS NEEDED FOR SINGLE ELEMENT TUPLE
a2 = (1, 7, 2)  # tuple with 2 or more elements dont need comma at end

t = (10, 2, 4, 5, 8, 0, 8, 8)  
print(type(t))   #will return <class 'tuple'>
print(t[0])   #will print item/element at index=0 i.e. 10
print(t[:2])   # will return (10, 2)
print(t[::3])  # will return (10,5,8)   ie tuple from start to end, but skip by 3

# values of tuples can not be updated
#t[0] = 34
#print(t)     #will return TypeError: 'tuple' object does not support item assignment


### TUPLE FUNCTIONS- count and index
# 1. count-- counts the number of times specified element is present in the tuple
print("the number 8 is present", t.count(8), "times in tuple t")

# 2. index---- returns first index of a value
print("the number 8 is present at index", t.index(8), "in tuple t")  # will not register the 2nd and 3rd 8.