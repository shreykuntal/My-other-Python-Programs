import random as r
nums = '1234567890'
special_char = '!@#$%^&*<>?/'
small_alpha = 'abcdefghijklmnopqrstuvwxyz'
caps_alpha = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
while True:
    len_pass = int(input("\nHow many letters should password contain?: "))
    password = ''
    for j in str(len_pass):
        if j in nums:
            fine_int = True
        else:
            fine_int = False
    if fine_int == True:        
        while True:
            len_pass = int(len_pass)
            for i in range(len_pass):
                chooser = r.randint(1,4)
                if chooser == 1:
                    choose_char = r.randint(0,9)
                    password += nums[choose_char]
                elif chooser == 2:
                    choose_char = r.randint(0,11)
                    password += special_char[choose_char]
                elif chooser == 3:
                    choose_char = r.randint(0,25)
                    password += small_alpha[choose_char]
                elif chooser == 4:
                    choose_char = r.randint(0,25)
                    password += caps_alpha[choose_char]
            break
        else:
            print("\nPlease enter a valid input.\n")
            continue
    print('\n',password,'\n\n; here is your',len_pass,'letters password.\n')
    ask = input("(y) for more or any other key to exit: ")
    if ask == 'y':
        continue
    else:
        break
    
