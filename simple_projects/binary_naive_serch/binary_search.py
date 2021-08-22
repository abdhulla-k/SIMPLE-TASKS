# binary serch 

def binary_search(l, target, low = None, high = None):
    
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if low > high:
        return "list is not containing target"

    midpoint = (low + high) // 2    # average of l

    if l[midpoint] == target:
        return (midpoint , 'th position is condaining the number')

    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)

    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)

if __name__=='__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    target = int(input("enter target number"))
    
    print(binary_search(l, target))