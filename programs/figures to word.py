one_digit='one','two','three','four','five','six','seven','eight','nine','zero'
teen='ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen'
ten_digit='twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'

print("PLEASE DON'T USE ANY PARENTHESIS.\nPLEASE ENTER LESS THAN FIVE DIGIT NUMBER\nPRESS ENTER TO CONTINUE")
_=input()
while True:
    no=0
    num=input("Enter an integer: ")
    if len(num)>4:
        print("Are you blind?! Didn't I told you to enter less than five digit number?. Program is now quitting!")
        break
    if num[0]=='(' or num[0]==')' or num[0]=='[' or num[0]==']' or num[0]=='{' or num[0]=='}':
        print("Are you blind?! Didn't you saw the above capitalised line! Program is now quitting!")
        
        break
    while True:
        if len(num)==2:
            one=num[1]
            ten=num[0]
            if num[0]+num[1]=='10':
                print(teen[0])
                break
            elif num[0]+num[1]=='11':
                print(teen[1])
                break
            elif num[0]+num[1]=='12':
                print(teen[2])
                break
            elif num[0]+num[1]=='13':
                print(teen[3])
                break
            elif num[0]+num[1]=='14':
                print(teen[4])
                break
            elif num[0]+num[1]=='15':
                print(teen[5])
                break
            elif num[0]+num[1]=='16':
                print(teen[6])
                break
            elif num[0]+num[1]=='17':
                print(teen[7])
                break
            elif num[0]+num[1]=='18':
                print(teen[8])
                break
            elif num[0]+num[1]=='19':
                print(teen[9])
                break
            if one=='1':
                one=one_digit[0]
            elif one=='2':
                one=one_digit[1]
            elif one=='3':
                one=one_digit[2]
            elif one=='4':
                one=one_digit[3]
            elif one=='5':
                one=one_digit[4]
            elif one=='6':
                one=one_digit[5]
            elif one=='7':
                one=one_digit[6]
            elif one=='8':
                one=one_digit[7]
            elif one=='9':
                one=one_digit[8]
            elif one=='0':
                one=''
            else:
                print("What the hell have you entered!? The program is now quitting!")
                no=1
                break
            if ten=='2':
                ten=ten_digit[0]
            elif ten=='3':
                ten=ten_digit[1]
            elif ten=='4':
                ten=ten_digit[2]
            elif ten=='5':
                ten=ten_digit[3]
            elif ten=='6':
                ten=ten_digit[4]
            elif ten=='7':
                ten=ten_digit[5]
            elif ten=='8':
                ten=ten_digit[6]
            elif ten=='9':
                ten=ten_digit[7]
            else:
                print("What the hell have you entered!? The program is now quitting!")
                no=1
                break
            print(ten+' '+one)
            break
        elif len(num)==1:
            one=num[0]
            if one=='1':
                print(one_digit[0])
                break
            elif one=='2':
                print(one_digit[1])
                break
            elif one=='3':
                print(one_digit[2])
                break
            elif one=='4':
                print(one_digit[3])
                break
            elif one=='5':
                print(one_digit[4])
                break
            elif one=='6':
                print(one_digit[5])
                break
            elif one=='7':
                print(one_digit[6])
                break
            elif one=='8':
                print(one_digit[7])
                break
            elif one=='9':
                print(one_digit[8])
                break
            elif one=='0':
                print(one_digit[9])
                break
            else:
                print("What the hell have you entered!? The program is now quitting!")
                no=1
                break
        elif len(num)==3:
            hundred=num[0]
            one=num[2]
            ten=num[1]
            z=0
            for i in num:
                if i==hundred:
                    if i=='1':
                        hundred=one_digit[0]
                    elif i=='2':
                        hundred=one_digit[1]
                    elif i=='3':
                        hundred=one_digit[2]
                    elif i=='4':
                        hundred=one_digit[3]
                    elif i=='5':
                        hundred=one_digit[4]
                    elif i=='6':
                        hundred=one_digit[5]
                    elif i=='7':
                        hundred=one_digit[6]
                    elif i=='8':
                        hundred=one_digit[7]
                    elif i=='9':
                        hundred=one_digit[8]
                    else:
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
                
                elif i==ten:
                    if ten=='1' and one=='0':
                        teens=teen[0]
                        z=1
                        break
                    elif ten=='1' and one=='1':
                        teens=teen[1]
                        z=1
                        break
                    elif ten=='1' and one=='2':
                        teens=teen[2]
                        z=1
                        break
                    elif ten=='1' and one=='3':
                        teens=teen[3]
                        z=1
                        break
                    elif ten=='1' and one=='4':
                        teens=teen[4]
                        z=1
                        break
                    elif ten=='1' and one=='5':
                        teens=teen[5]
                        z=1
                        break
                    elif ten=='1' and one=='6':
                        teens=teen[6]
                        z=1
                        break
                    elif ten=='1' and one=='7':
                        teens=teen[7]
                        z=1
                        break
                    elif ten=='1' and one=='8':
                        teens=teen[8]
                        z=1
                        break
                    elif ten=='1' and one=='9':
                        teens=teen[9]
                        z=1
                        break
                    elif ten=='1':
                        
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
                    elif i=='2':
                        ten=ten_digit[0]
                    elif i=='3':
                        ten=ten_digit[1]
                    elif i=='4':
                        ten=ten_digit[2]
                    elif i=='5':
                        ten=ten_digit[3]
                    elif i=='6':
                        ten=ten_digit[4]
                    elif i=='7':
                        ten=ten_digit[5]
                    elif i=='8':
                        ten=ten_digit[6]
                    elif i=='9':
                        ten=ten_digit[7]
                    elif i=='0':
                        ten=''
                    else:
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
                elif i==one:
                    if i=='1':
                        one=one_digit[0]
                    elif i=='2':
                        one=one_digit[1]
                    elif i=='3':
                        one=one_digit[2]
                    elif i=='4':
                        one=one_digit[3]
                    elif i=='5':
                        one=one_digit[4]
                    elif i=='6':
                        one=one_digit[5]
                    elif i=='7':
                        one=one_digit[6]
                    elif i=='8':
                        one=one_digit[7]
                    elif i=='9':
                        one=one_digit[8]
                    elif i=='0':
                        one=''
                    else:
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
            if no==1:
                break
            if z==1:
                print(hundred+ ' hundred and '+teens)
                break
            elif z==0:
                print(hundred+ ' hundred and '+ten+' '+one)
                break
        elif len(num)==4:
            thousand=num[0]
            hundred=num[1]
            one=num[3]
            ten=num[2]
            z=0
            for i in num:
                if i==thousand:
                    if i=='1':
                        thousand=one_digit[0]
                    elif i=='2':
                        thousand=one_digit[1]
                    elif i=='3':
                        thousand=one_digit[2]
                    elif i=='4':
                        thousand=one_digit[3]
                    elif i=='5':
                        thousand=one_digit[4]
                    elif i=='6':
                        thousand=one_digit[5]
                    elif i=='7':
                        thousand=one_digit[6]
                    elif i=='8':
                        thousand=one_digit[7]
                    elif i=='9':
                        thousand=one_digit[8]
                    else:
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
                            
                elif i==hundred:
                    if i=='1':
                        hundred=one_digit[0]
                    elif i=='2':
                        hundred=one_digit[1]
                    elif i=='3':
                        hundred=one_digit[2]
                    elif i=='4':
                        hundred=one_digit[3]
                    elif i=='5':
                        hundred=one_digit[4]
                    elif i=='6':
                        hundred=one_digit[5]
                    elif i=='7':
                        hundred=one_digit[6]
                    elif i=='8':
                        hundred=one_digit[7]
                    elif i=='9':
                        hundred=one_digit[8]
                    elif i=='0':
                        hundred=''
                    else:
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
                
                elif i==ten:
                    if ten=='1' and one=='0':
                        teens=teen[0]
                        z=1
                        break
                    elif ten=='1' and one=='1':
                        teens=teen[1]
                        z=1
                        break
                    elif ten=='1' and one=='2':
                        teens=teen[2]
                        z=1
                        break
                    elif ten=='1' and one=='3':
                        teens=teen[3]
                        z=1
                        break
                    elif ten=='1' and one=='4':
                        teens=teen[4]
                        z=1
                        break
                    elif ten=='1' and one=='5':
                        teens=teen[5]
                        z=1
                        break
                    elif ten=='1' and one=='6':
                        teens=teen[6]
                        z=1
                        break
                    elif ten=='1' and one=='7':
                        teens=teen[7]
                        z=1
                        break
                    elif ten=='1' and one=='8':
                        teens=teen[8]
                        z=1
                        break
                    elif ten=='1' and one=='9':
                        teens=teen[9]
                        z=1
                        break
                    elif ten=='1':
                        
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
                    elif i=='2':
                        ten=ten_digit[0]
                    elif i=='3':
                        ten=ten_digit[1]
                    elif i=='4':
                        ten=ten_digit[2]
                    elif i=='5':
                        ten=ten_digit[3]
                    elif i=='6':
                        ten=ten_digit[4]
                    elif i=='7':
                        ten=ten_digit[5]
                    elif i=='8':
                        ten=ten_digit[6]
                    elif i=='9':
                        ten=ten_digit[7]
                    elif i=='0':
                        ten=''
                    else:
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
                elif i==one:
                    if i=='1':
                        one=one_digit[0]
                    elif i=='2':
                        one=one_digit[1]
                    elif i=='3':
                        one=one_digit[2]
                    elif i=='4':
                        one=one_digit[3]
                    elif i=='5':
                        one=one_digit[4]
                    elif i=='6':
                        one=one_digit[5]
                    elif i=='7':
                        one=one_digit[6]
                    elif i=='8':
                        one=one_digit[7]
                    elif i=='9':
                        one=one_digit[8]
                    elif i=='0':
                        one=''
                    else:
                        print("What the hell have you entered!? The program is now quitting!")
                        no=1
                        break
            if no==1:
                break
            if z==1:
                if hundred=='':
                    print(thousand+' thousand  and '+teens)
                    break

                else:
                    print(thousand+' thousand '+hundred+ ' hundred and '+teens)
                
                    break
                
            elif z==0:
                if hundred=='':
                    print(thousand+' thousand and '+ten+' '+one)
                    break
                else:
                    print(thousand+' thousand '+hundred+ ' hundred and '+ten+' '+one)
                    break
    if no==1:
        break
    ask=input("(y) for more or (n) to exit: ")
        
    if ask=='y':
        continue
    elif ask=='n':
        break
    else:
        print("Are you blind? Program is now quitting!")
        break
                
    
            
            
            
                    
                
            
                        
                
        
        
            
            
