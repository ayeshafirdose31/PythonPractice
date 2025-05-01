"""Conditional Statements """

#if-elif-else
num=5
if num>3:
    print("maybe") # proper spacing is indentation
if num>4:
    print("Check")
    
print("""Ends code""")
    
"""prints both ifs when the statement becomes true, but elif gets executed only when if becomes false"""
#else executes if all other ifs and elifs becomes false

#Nesting 

#WAP to print if a person is eligible for driving or not and the condition should be if age is greater than 80 cannot drive 

age=int(input("Enter the age: "))
if age>=18:
    if age>=80:
        print("Cannot drive")
    else:
        print("can drive")
else:
    print("not eligible")