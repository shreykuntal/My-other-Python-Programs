import random as r
snakes = [16, 47, 49, 56, 62, 63, 87, 93, 95, 99]
downfall = [6, 26, 30, 53, 19, 60, 24, 73, 75, 78]
ladder = [2, 4, 9, 21, 28, 36, 51, 61, 71]
up_rise = [37, 14, 31, 42, 84, 44, 74, 82, 91]
while True:
        winner = None
        while winner == None:
                plyr1 = 0
                plyr2 = 0
                while True:
                        print("Press enter to roll the dice!")
                        _=input()
                        dice = r.randint(1,6)
                        print("Value of dice is:",dice,'\n')
                        if (plyr1 + dice) > 100:
                                plyr1 = plyr1
                        else:
                                plyr1 += dice
                        if plyr1 in snakes:
                                down = snakes.index(plyr1)
                                plyr1 = downfall[down]
                                print("Player 1 came to a snake on", snakes[down],"and fell to",plyr1,"!\n")
                        elif plyr1 in ladder:
                                up = ladder.index(plyr1)
                                plyr1 = up_rise[up]
                                print("Player 1 came to a ladder on", ladder[up],"and climbed to",plyr1,"!\n")
                        if plyr1 == 100:
                                winner = 'plyr1'
                                print("Player 1st:",plyr1)
                                print("Player 2nd:",plyr2)
                                break
                        print("Press enter to roll the dice!")
                        _=input()
                        dice = r.randint(1,6)
                        print("Value of dice is:",dice,'\n')
                        if (plyr2 + dice) > 100:
                                plyr2 = plyr2
                        else:
                                plyr2 += dice
                        if plyr2 in snakes:
                                down = snakes.index(plyr2)
                                plyr2 = downfall[down]
                                print("Player 2 came to a snake on", snakes[down],"and fell to",plyr2,"!\n")
                        elif plyr2 in ladder:
                                up = ladder.index(plyr2)
                                plyr2 = up_rise[up]
                                print("Player 2 reached a ladder on", ladder[up],"and climbed to",plyr2,"!\n")
                        if plyr2 == 100:
                                winner = 'plyr2'
                                print("Player 1st:",plyr1)
                                print("Player 2nd:",plyr2)
                                break
                                
                        print("Player 1st:",plyr1)
                        print("Player 2nd:",plyr2)
        if winner == 'plyr1':
                print("\nPlayer 1st wins!")
        else:
                print("\nPlayer 2nd wins!")
        ask = input("(y) to play again or any other key to quit: ")
        if ask == 'y':
                continue
        else:
                break