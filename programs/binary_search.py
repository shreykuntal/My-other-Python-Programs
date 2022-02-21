def search(L, item):
    beg = 0
    last = len(L) - 1
    mid = (beg + last) //2
    while last - beg > 1:
        mid = (beg + last)//2
        if item < L[mid]:
            last = mid
        elif item > L[mid]:
            beg = mid
        if L[mid] == item:
            return mid
    else:
        return False
L = [1, 3, 5, 7, 9]
print(search(L,8))
