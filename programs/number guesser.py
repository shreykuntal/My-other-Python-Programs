import random
print (("Choose a number from 1 to 100").upper())
b=float((random.randint(1,120)))
x=(b/2)
z=float(x)
a=input("Press 1 and enter to continue ")
if a=="1":
    print(("Multiply your number by 2").upper())
    c=input("Press 1 and enter to continue ")
    if c=="1":
        print((("Add %d to your answer")%(b)).upper())
        d=input("Press 1 and enter to continue ")
        if d=="1":
            print (("Divide your answer by 2").upper())
            e=input("Press 1 and enter to continue ")
            if e=="1":
                print (("Subtract the original number from your answer").upper())
                f=input("Press 1 and enter to continue ")
                if f=="1":
                    g=input('IS YOUR ANSWER '+str(z)+'?YES OR NO')
                    if g.lower()=="yes": 
                        print ("YAY!")
                    else:
                        print("Do you even know how to calculate?")
                else:
                    print ("Do you even know number 1?")
            else:
                print ("Do you even know number 1?")
        else:
            print ("Do you even know number 1?")
    else:
        print ("Do you even know number 1?")
else:
    print ("Do you even know number 1?")
     


    
        
    
