def freq(s):
    """
    Takes s a string
    Return number of occurence of every word
    """
    s = sorted(s.split(' '))
    freq = s.count(s[0])
    print(s[0],':',freq)
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
                freq = s.count(s[i])
                print(s[i],':',freq)