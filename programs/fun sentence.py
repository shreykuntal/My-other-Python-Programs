import random
while True:
    a=random.randint(0,6)
    b=random.randint(0,3)
    c=random.randint(0,2)
    noun=['Shrey','Dipu bhaiya','Nishi bhaiya','Papa','Mummy','Abhishek','Anurag']
    verb=[' is playing ',' is eating ', ' is running ',' is dancing ']
    etc=[' for fitness ',' for enjoyment ',' for breaking records ']
    print(str(noun[a])+str(verb[b])+str(etc[c]))
    doyou=input("Do you want to generate more? Yes(y) or No(n)")
    
    if doyou=='y':
        continue
    elif doyou=='n':
        print("Thansks for using")
        break
    else:
        print("Are you blind!")
        break

