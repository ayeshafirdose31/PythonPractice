#Search for a number x in this tuple using loop 

nums=(1,4,9,16,25,36,49,64,81,100)

x=int(input("Enter the number to find: "))

i=0

while i<len(nums):
    if (nums[i]==x):
        print("found at idx",i)
    i+=1