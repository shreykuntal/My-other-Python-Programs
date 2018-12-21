import datetime
while True:
    while True:
        name=input("Enter your name: ")
        dob=input("Please enter your DOB(dd/mm/yyyy): ")
        bill=input("Please enter your bill: ")
        phone=input("Please enter your Mobile No.: ")
        time=str(datetime.datetime.now())
        name=('Name = '+name+'\n')
        dob=('DOB (dd/mm/yyyy) = '+dob+'\n')
        bill=('Bill = Rs.'+bill+'\n')
        phone=("Mobile No. : "+phone+'\n')
        info=[name,dob,bill]
        tofile=open("Bill.xls",'a')
        tofile.write(name)
        tofile.write(dob)
        tofile.write(bill)
        tofile.write(phone)
        time=('Time: '+time+'\n\n')
        tofile.write(time)
        tofile.close()
        break
    ask=input("(y) for more or (n) to quit: ")
    if ask=='y':
        continue
    else:
        break


