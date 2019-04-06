def sort(n,a,s):
    """
    n = name
    a = age
    s = score
    All should be lists
    """
    from operator import itemgetter
    data = []
    for i in range(len(n)):
        toData = ()
        toData += (n[i], a[i], s[i])
        data.append(toData)
    print(data)
    data_sorted = sorted(data,key=itemgetter(0,1,2))
    return data_sorted
print(sort(['hesoyam','hesoyam','hesoyam'],[18,17,17],[100,20,50]))