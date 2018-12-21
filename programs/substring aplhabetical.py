s = '!@#$#!@djsfijag2gkihjdsa123iskmkkdjwjka_002' # YOUR STRING HERE

alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

toPrint = []

will_continue = ''

for k in range(0 ,len(s)):
        if s[k] in alphabets :
                t = s[k]
                largest = k
                break 

if k == len(s) - 1:
        will_continue = 'no'

if will_continue != 'no':
        for i in range(k+1, len(s)):
                if s[i] in alphabets:
                        if (s[largest].lower()) <= (s[i].lower()):
                                largest = i
                                t += s[largest]     
                        else:
                                largest = i
                                toPrint.append(t)
                                t = ''
                                t += s[i]                       
        toPrint.append(t)
        
        length = toPrint[0]
        
        largest_index = 0

        for j in range(1,len(toPrint)):
                if len(toPrint[j]) > len(toPrint[largest_index]):
                        length = toPrint[j]
                        largest_index = j
        print('Longest substring in alphabetical order is ' + length)

else:
        print("There is no string.")