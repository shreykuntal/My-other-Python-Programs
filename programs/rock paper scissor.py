import random as r
a='rock'
b='paper'
c='scissor'
while True:
    second=''
    choose=input("Choose rock(r), paper(p) or scissor(s): ")
    game=r.randint(1,3)
    if game==1:
        game=a
    elif game==2:
        game=b
    else:
        game=c
    if choose=='r' and game==a:
        choose=a
        print(choose+" vs "+a)
        print("DRAW!")
        
    elif choose=='r' and game==b:
        choose=a
        print(choose+" vs "+b)
        print("You LOSE!")
    elif choose=='r' and game==c:
        choose=a
        print(choose+" vs "+c)
        print("You WIN!")
    elif choose=='p' and game==a:
        choose=b
        print(choose+" vs "+a)
        print("You WIN!")
    elif choose=='p' and game==b:
        choose=b
        print(choose+" vs "+b)
        print("DRAW!")
    elif choose=='p' and game==c:
        choose=b
        print(choose+" vs "+c)
        print("You LOSE!")
    elif choose=='s' and game==a:
        choose=c
        print(choose+" vs "+a)
        print("You LOSE!")
    elif choose=='s' and game==b:
        choose=c
        print(choose+" vs "+b)
        print("You WIN!")
    elif choose=='s' and game==c:
        choose=c
        print(choose+" vs "+c)
        print("DRAW!")
    again=input("(y) to play again or (n) to leave: ")
    if again=="y":
        continue
    elif again=='n':
        break
    else:
        print("Are you blind?")
