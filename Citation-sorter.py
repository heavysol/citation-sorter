# Created on 27 Mar '23
# Citation sorter
import re

# Opening reference file to be read
cites = open('WOC-argument-REFERENCES.txt', 'r') # Opens citation doc in Py; PUT ALL REFERENCES IN THIS TEXT FILE FOR SORTING
references = cites.readlines() # Puts all the lines in the file in one array, the thing readlines() does 

#for reference in references: # italicises title section of reference
   # print(re.sub("). " +"\w" +".", "\x1B[3m" +"\w" +"\x1B[0m", reference))
   #print(re.search("). (.*) .", reference))

n = 0
for reference in references:
    n += 1
            
userInput = int(input('Hello there! This program sorts references of citations in an order you desire.\n Which order would you like to sort your citations? Type in the number before the option to select your chosen option.\n 1 - In ascending alphabetical order of author \n 2 - In descending alphabetical order of author \n 3 - In ascending year \n 4 - In descending year \n')) # Intro to program, detailing the sorting options for user to select

if userInput == 1: # Prints references from ascending alphabetical order of author
    print('======The references from ascending alphabetical order of author======')
    for reference in sorted(references, reverse = False):
        print(reference)
    print('======End of references======')
    print('>==> total number of references:', n)

elif userInput == 2: # Prints references from descending alphabetical order of author
    print('======The references from descending alphabetical order of author======')
    for reference in sorted(references, reverse = True):
        print(reference)
    print('======End of references======')
    print('>==> total number of references:', n)

elif userInput == 3: # Prints references from ascending year
    print('======The references from ascending year======')
    for reference in sorted(re.findall('^(....)$')):
        print(reference)
    print('======End of references======')
    print('>==> total number of references:', n)

elif userInput == 4: # Prints references from descending year
    print('======The references from descending year======')
    for reference in references:
        print(reference)
    print('======End of references======')
    print('>==> total number of references:', n)