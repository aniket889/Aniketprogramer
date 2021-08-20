# write the programme use in zip function in python
x = int(input("enter the range of x"))
y = int(input("enter the range of y"))
for x,y in zip(range(1,6), range(5,-1)):
    if x == 3 and y == 3:
        continue
    else:
        print(x,"   ",y)
        