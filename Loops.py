"""Loops"""
#Loops are used to repeat instructions 

"""2 Types of loops
1)for loop
2)while loop"""

count=1 #var on which the iterar=tion is performed is known as iterator

while count<=5:
    print("hello",count)
    count+=1   #iteration is the act of performing the task 
    
print(count)

#another way of loop 

i=5

while i>=1:
    print(i)
    i -=1
    
    
"""Range functions= returns a sequence of numbers, starting from 0 by default, and increments by
1 (by default), and stops before a specified number."""

"""Pass Statement"""
#pass is a null statement that does nothing. It is used as a placeholder for future code.
for i in val:
    pass