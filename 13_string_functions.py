#   1. string length
# the function 'len' returns the length of the string
example = "the quick brOwn fox jumps Over the lazy dog"
print (len(example))   # will return '43', a numeric value with number of characters (including space) in the string

#   2. string endswith 
# the .endswith function tells whether the string ends with the string "insert specific word" or not
print (example.endswith("dog"))    # will return True

#    3. string count character
# counts the total number of occurences of the specified character(s) or word. it is case sensitive
print (example.count("O"))    # will return 2 and not 3
print (example.count("the"))   # will return 2
print (example.count("qui"))    # will return 1

#    4. string capitalize
# this function capitalises the first character of a given string
print (example.capitalize()) # will return 'The quick brown fox jumps over the lazy dog'

#    5. find character(s)
# find func returns ''first'' occurence/ lowest index in the string where substring character(s) are found. 
# returns -1 if not found
print (example.find("brOw"))   # is case sensitive. and returns 10

#    6. replace character(s)
# .replace("oldword","newword") func replaces (''all occurence'') the selected characters with new characters
print(example.replace("lazy", "active"))   # will return 'the quick brOwn fox jumps Over the active dog'
