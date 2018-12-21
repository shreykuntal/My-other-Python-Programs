for_odds =[1,2,3,4,5,6,7,8,9,10] #your list here #random.sample(range(150), 100) # 100 random numbers b/w 0,150
biggest_odd=float('-inf')

for i in for_odds:
	if i%2!=0:
		if i>biggest_odd:
			biggest_odd=i

print("The greatest odd number is ", biggest_odd)
del for_odds[for_odds.index(biggest_odd)]
biggest_odds=float('-inf')
for j in for_odds:
	if j%2!=0:
		if j>biggest_odds:
			biggest_odds=j
print("The second greatest odd number is ", biggest_odds)


   
    


    
    
        

    
