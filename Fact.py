#WAP to find the factorial of first n numbers. (using for)

# n=5
# i=1
# mul=1

# while i<=n:
#     mul*=i
#     i+=1
#     print(mul)
    
"""using for loop"""
n=5
mul=1
for i in range(1,n+1):
    mul*=i
    i+=1
print(mul)