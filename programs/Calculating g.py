import math
G=(6.7)*(10**-11)
M=float(input("Enter value of M(kg): "))
d=float(input("Enter value of d(m): "))
g=(G*M)/(d**2)
print ("g =",g,"m/s^2")
c=input("Do you want to see what is the meaning of e: ")
if c.lower()=="yes" or c.lower()=="y":
    print ("e=10^x.For example:2e+15=2*10^15.And 2e-15=2*10^-15.")
else:
    print ("Thanks for using our program!")
        
    
    
 

