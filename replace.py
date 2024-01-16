#Psudeo code
#First declare a variable by assigning a string with ! insted of space
#Than replace the "!" with space using replace function and sore the new string into another variable
#Print the string with space
#print the all charecters of string in upper case by using upper() function
#print the string in reverse order by applyin specific syntax


#declare a variable by assigning a string with ! insted of space
sentence="The!quick!brown!fox!jumps!over!the!lazy!dog."
#Replace the "!" with space using replace function and sore the new string into another variable
sentence1=sentence.replace("!"," ")
#Print the string with space
print(sentence1)
#print the all charecters of string in upper case by using upper() function

print(sentence1.upper())
#print the string in reverse order by applyin specific syntax

print(sentence1[::-1])