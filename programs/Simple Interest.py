print ("note:Please Enter'.0' after any non-decimal value".upper())
a=float(input("Enter Principal:Rs."))
b=float(input("Enter Rate%: "))
c=float(input("Enter Time(in years): "))
d=(a*b*c)/100
print ("[your entered values are:]".upper())
print ("Principal:Rs.",a)
print ("Rate%:",b)
print ("Time:",c,"year(s)")
print ("simple interest is:".upper())
print ("Rs.",float(d))

