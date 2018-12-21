import math
G=(6.7)*(10**-11)
M=float(raw_input("Enter value of M(kg): "))
m=float(raw_input("Enter value of m(kg): "))
d=float(raw_input("Enter value of d(m): "))
F=(G*M*m)/(d**2)
print "Force= ",F,"N"
c=raw_input("Do you want to see what is meaning of e: ")
if c.lower()=="yes":
    print "e=10^x.For example:2e+15=2*10^15.And 2e-15=2*10^-15."
else:
    print "Thanks for using our program!"
        
    
    
 

