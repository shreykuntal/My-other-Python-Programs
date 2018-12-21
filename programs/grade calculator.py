sub=str(input("Which subject you want to choose(PCM,PCB or Humanities)?: "))
if sub.upper()=='PCM': 
    print ("Please Enter Marks of: ")
    math=float(input("Maths: "))
    phy=float(input("Physics: "))
    chem=float(input("Chemistry: "))
    per=((math+phy+chem)/(300))*100

    if per>=85:
        print (("You are eligible to take PCM! Your percentage is"),float(per),('% and minimum required percentage is 85%'))
    else:
        print(("Sorry! Minimum percentage required is 85.0% and yours is"),float(per),('%'))

elif sub.upper()=='PCB':
    print ("Please Enter Marks of: ")
    ph=float(input("Physics: "))
    che=float(input("Chemistry: "))
    bio=float(input("Biology: "))
    pe=((ph+che+bio)/(300))*100
    if pe>=80:
        print (("You are eligible to take PCM! Your percentage is"),float(pe),('% and minimum required percentage is 80%'))
    else:
        print(("Sorry! Minimum percentage required is 80.0% and yours is"),float(pe),('%'))
elif sub.lower()=="humanity" or sub.lower()=="humanities":
    print("Please Enter Marks of: ")

    sst=float(input("Social Studies: "))
    eng=float(input("English: "))
    p=((sst+eng)/(200))*100
    if p>=70:
        print (("You are eligible to take Humanities! Your percentage is"),float(p),('% and minimum required percentage is 70%'))
    else:
        print(("Sorry! Minimum percentage required is 70.0% and yours is"),float(p),('%'))
    

else:
    print ("ARE YOU OUT OF YOUR MIND? You have enter from these topics(PCM,PCB or Humanities)!!")

    print ("Now you have to restart the program!".upper())

    


