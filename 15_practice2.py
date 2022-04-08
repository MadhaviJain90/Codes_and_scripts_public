# write a python program to display a user entered name followed by Good Afternoon using input function

a = input("Enter name here:\n ")
print (a, "Good Afternoon")
print ("Good Night," + a)

# write a program to fill in a letter template given below with name and date
# letter = '''Dear <|Name|>,
#             you are selected!!
#             <|Date|>'''
letter = '''

Dear <|NAME|>,
         
         you are selected!!
         have a great day ahead

Date: <|DATE|>

'''

# print(letter.replace("<|NAME|>", "Madhavi"), letter.replace("<|DATE|>", "12/December/2021")) ##WRONG WAY
# you need to assign new value to the variable so
letter = letter.replace("<|NAME|>", "Madhavi")
letter = letter.replace("<|DATE|>", "12/December/2021")
print (letter)