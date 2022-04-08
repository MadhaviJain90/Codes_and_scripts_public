# write a program to detect double spaces in a string 
line = "Tuples can contain  any number of elements and of any  datatype (like strings, integers, list)"
print(line.count("  "))    # will return 2 ie total count 2
print(line.find("  "))    #will return 18 ie 18 place 1st instance

#replace double spaces in above line with single spaces
line = line.replace("  ", " ")
print (line)     #will return 'Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.)'

# write the following letter properly using escape sequence characters

# Wazirabad, New Delhi – 33
# Dated: 17 February 2021
# The Editor
# Hindustan Times
# New Delhi.
# Subject: Need for people’s movement for the clean Yamuna
# Dear Editor
# I am Radha G, member of NGO AWAAZ. I am writing to you in order to highlight the deteriorating condition of the river Yamuna.
# The city of Delhi is getting contaminated water from the river Yamuna. The residents are to be blamed for this. They pollute the river with garbage, sewage, and filth. The river water is full of bacteria, plastic, chemicals, and other waste materials. It is unfit for consumption.
# The people have been demanding a Water Treatment Plant. The authorities have not yet responded to the repeated requests.
# I request you to highlight the problem in your newspaper and arouse public interest. We all need to get together in order to get the plant set up in the area.
# Thank You
# Yours sincerely
# Radha G

letter = '''Wazirabad, New Delhi-33\nDated: 17 February 2021\nThe Editor\nHindustan Times\nNew Delhi\n\tSubject: Need for people\'s movement for the clean Yamuna
Dear Editor\n\tI am Radha G, member of NGO AWAAZ. I am writing to you in order to highlight the deteriorating condition of the river Yamuna.The city of Delhi is getting contaminated water from the river Yamuna. The residents are to be blamed for this. They pollute the river with garbage, sewage, and filth. The river water is full of bacteria, plastic, chemicals, and other waste materials. It is unfit for consumption.
\n\tThe people have been demanding a Water Treatment Plant. The authorities have not yet responded to the repeated requests.I request you to highlight the problem in your newspaper and arouse public interest. We all need to get together in order to get the plant set up in the area.
\nThank You\nYours sincerely\nRadha G'''
print (letter)