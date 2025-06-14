"""Break & Continue"""

#Break: Use to terminate the loop when encountered 
#Continue: Terminates the execution in current iteration and continues execution of the loop with the next iteration 
 
"""Break"""
i=0

while i<=5:
    if (i==3):
        break #terminates the complete iteration 
    i+=1
    print(i)



"""Continue"""
i=0

while i<=5:
    if (i==3):
        i+=1
        continue #skips 
    print(i)
    i+=1
    
    
    
"""odd numbers using while"""

i=1
while i<=10:
    if (i%2==0):
        i+=1
        continue
    print(i)
    i+=1
    
"""even numbers using while"""

i=1
while i<=10:
    if (i%2!=0):
        i+=1
        continue
    print(i)
    i+=1