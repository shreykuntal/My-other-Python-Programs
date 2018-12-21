import math
while True:
    number=['1','2','3','4','5','6','7','8','9','0','-','+']
    num = input("Enter an integer: ")
    proper=0
    for i in range(len(num)):
        if proper>0:
            number.remove('-')
            number.remove('+')
            proper=float('-inf')
        if num[i] in number:
            will_continue='y'
        else:
            will_continue='n'
            break
        proper+=1
    if will_continue=='y':
        num=int(num)
        primes=0
        negetive=''
        if num<0:
            num=abs(num)
            negetive='y'
        minus1=num-1
        while minus1>2:
            i = 2
            check=math.sqrt(minus1)
            prime=int(math.sqrt(minus1))
            isprime=''
            while i<=check:
                if check==prime:
                    isprime='n'
                    break
                if check<1.6 or minus1==4:
                    isprime='n'
                    break
                if minus1 % i == 0:
                    isprime='n'
                    break
                if minus1 % 2==0:
                    isprime='n'
                    break
                i += 1
            if isprime != 'n' and negetive=='y':
                print('-'+str(minus1))
                primes=1
            elif isprime!='n':
                print(minus1)
                primes=1
            minus1-=1
        if primes==0:
            print("No prime number found!")
        ask=input("(y) for more. (n) to quit: ")
        if ask=='y':
            continue
        elif ask=='n':
            break
    else:
        print("Please don't use space and enter relevant values.\n")
        continue