# write a program to store seven fruits in a list entered by the user

a1 = input("Enter fruit 1: ")
a2 = input("Enter fruit 2: ")
a3 = input("Enter fruit 3: ")
a4 = input("Enter fruit 4: ")
a5 = input("Enter fruit 5: ")
a6 = input("Enter fruit 6: ")
a7 = input("Enter fruit 7: ")

list_fruits = [a1, a2, a3, a4, a5, a6, a7]
print(list_fruits)               # returns ['apple', 'banana', 'mango', 'kiwi', 'orange', 'grapes', 'strawberry']


# write a program to accept marks of 6 students and display them in sorted manner
m1 = input("Enter studen 1 marks: ")
print("marks accepted")
m2 = input("Enter studen 2 marks: ")
print("marks accepted")
m3 = input("Enter studen 3 marks: ")
print("marks accepted")
m4 = input("Enter studen 4 marks: ")
print("marks accepted")
m5 = input("Enter studen 5 marks: ")
print("marks accepted")
m6 = input("Enter studen 6 marks: ")
print("marks accepted")
m1 = float(m1)
m2 = float(m2)
m3 = float(m3)
m4 = float(m4)
m5 = float(m5)
m6 = float(m6)

#can also be written as m = float(input("Enter marks:"))    ### will convert marks from str to int/float here only 

list_of_marks = [m1, m2, m3, m4, m5, m6]
print("Student marks: ",list_of_marks)    
#returns Student marks:  ['21', '43', '67', '09', '97', '78'] if not converted to float/ int
list_of_marks.sort()             
print("Student marks low to high: ", list_of_marks) 
#Student marks low to high:  [09, 21, 43, 67, 78, 97]


# write a program to sum a list with 4 numbers
list1 = [30, 60, 700, 15]
print(sum(list1))    #returns 805

