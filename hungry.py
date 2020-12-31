def getTotal(lst):
    total=0
    for item in lst:
        total=total+item
    return total

l1={1,2,3,4,5}
l2={11,22,33,44,55}
totalL1=getTotal(l1)
totalL2=getTotal(l2)
print("Total of List 1:" , totalL1 )
print("Total of List 2:" , totalL2 )