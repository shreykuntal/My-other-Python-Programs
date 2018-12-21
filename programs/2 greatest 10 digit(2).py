for_odds =[13,5,9,8,2] #your list here #random.sample(range(150), 100) # 100 random numbers b/w 0,150
odd=0
for j in for_odds:
        if j%2==0:
                del for_odds[for_odds.index(j)]
        elif j%2!=0:
                odd+=1                
if odd<=1:
        print('insufficient numbers')
else:
        del for_odds[for_odds.index(max(for_odds))]
        print ("The second greatest odd number is ",max(for_odds))


