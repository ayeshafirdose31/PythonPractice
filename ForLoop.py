"""For Loop"""
#Loops are used for sequential traversal. For traversing list, string, tuples etc
val=[1,2,3,4,5,6,7,8,9,0]

"""while """ 
i=0
while i<len(val):
    print(val[i])
    i+=1
    
# """For Loop"""
val=[1,2,3,4,5,6,7,8,9,0]

for i in val:
    print(i)
    
"""for with else"""

name=["Mufasa","leo","China","India","Russia","America","England"]

for char in name:
    print(char)
else:
    print("END OF NAMES")
    

"Break in for loop"
str="Mufasa"

for i in str:
    if (i=="a"):
        print("a is found",i)
        break
    print(i)
else:
    print("End")