#naive_sech below

def naive_serch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


l = [1,2,3,4,5,6,7,8,9,10]
print(naive_serch(l,target=7))