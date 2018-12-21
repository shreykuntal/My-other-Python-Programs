import time
while True:
    a=int(input("Enter an integer: "))
    b=2
    start_time = time.time()
    while True:
        if b==int(a/2):
            f='y'
            break
        elif a%b==0:
            f='n'
            break
        else:
            b+=1
    if f=='n':
        print(str(a)+" is not a prime number")
        print(str(a)+" is divisible by "+str(b))   
    else:
        print(str(a)+" is a prime number")

    print("--- %s seconds ---" % (time.time() - start_time))
    ask=input("Do you want to try another number? (y) or (n)")
    
    if ask=='y':
        continue
    elif ask=='n':
        break
    else:
        print("Are you blind folded?")
    

        
    
    
