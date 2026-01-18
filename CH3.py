name="harryking"    #string is immuteable

sliced_string=name[-3:]

print(sliced_string)

#skipping values
#string[starting index: ending index(excluded from printing) :skipping/jumping value(index calculation)]

string="IT WILL CRY"
print(string[0::5])

string_1="This string is for fun. Only for educational purpose."
print(string_1[0::2])

#functons for string

length=len(string)
print(length)

print(len(string_1))

#string ends with function..counts for the ending character not of the word but the whole string...
#syntax is general strname.endswith("matching characters in your string or you want to check")
#key points: write it in string and used only for true and false display..

print(string_1.endswith("ose."))

future='this is a sring named "future"'
print(future)

# -------------Pracice Set 3-------------

# 1

name=input("Enter your name : ")
print(f"Good afternoon {name}")

#2

name=input("Enter your name : ")
date=input("Enter current date of issuance of letter : ")

letter='''
Dear <name>,
You are selected.
Thanks!
<date>
'''
print(letter.replace("<name>",name).replace("<date>",date))#original string will not be changed!!!

#3 Detect double space in string

string="Harry is a good  boy!"
print(string.find("  "))

#4 Replace upper double space with single space

string="Harry is a good  boy!"
print(string.replace("  "," ")) #original space doesnot change

#5 formate the letter

letter="Dear Harry,\n\tThis python course is Helpful.\n\tThanks!"
print(letter)