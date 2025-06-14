#Search for number x in tuple using loop

tup=(1,4,9,16,25,36,49,64,81,100)
x=36
for el in tup:
    if (el==x):
        print("found",x)
        break
    print(el)

    
"""number found with idx"""
tup=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
for el in tup:
    if (el==x):
        print("found",idx)
        break
    idx+=1

"""Range func"""
print(range(5)[1])
