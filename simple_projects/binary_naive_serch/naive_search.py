#naive_sech below

def naive_serch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return (i, 'th position is containing the number')
    return "target is not containing the list"


l = [1,2,3,4,5,6,8,9,10,7]
target = int(input("Enter the target number"))
print (str(naive_serch(l,target)))