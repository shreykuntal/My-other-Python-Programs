import random as r
while True:
    high=100
    low=0
    guess_times=0
    print("Think of a number from 1 to 100 and press enter to continue...")
    _=input()
    while True:
        if low>high:
            print("Don't try to cheat with me you cheater! The program is now quitting!")
            if_play='n'
            break
        guess_times+=1
        guess=r.randint(low,high)
        num=input("Is your number "+str(guess)+" ?. Reply in YES(y), HIGH(h), LOW(l) and press enter: ")
        if num=='y':
            print("YAY!")
            print("NUMBER OF GUESSES WERE: "+str(guess_times))
            if_play=input("Do you want to play again? Reply in YES(y), NO(n): ")
            if if_play=="y":
                break
            elif if_play=="n":
                print("Thanks for playing!")
                break
            else:
                break
        elif num=='h':
            low=guess
            low+=1
        elif num=='l':
            high=guess
            high-=1
        else:
            print("Are you blind?! Don't you saw to reply in (y) or (h) or (l). FOOL! The program is now quitting!")
            if_play="n"
            break
    if if_play=="y":
        continue
    elif if_play=='n':
        break
    else:
        print("Are you blind?! Don't you saw to reply in (y) or (n). FOOL! The program is now quitting!")
            
            
        
    
                        
                        
                                 

                     
        
