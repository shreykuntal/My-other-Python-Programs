which=int(input("Of which number you would like to print table: "))
hmany=int(input("To how much should I print table of "+str(which)+" ?: "))
a=0
b=0
while a!=hmany:
    b+=1
    print (str(which)+" x "+str(b)+" = "+str(which*b))
    a+=1
    
