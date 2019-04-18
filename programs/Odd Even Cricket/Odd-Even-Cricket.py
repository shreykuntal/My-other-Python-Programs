# Rules:
# This game is played like Rock-Paper-Scissors
# There are total of 8 numbers that you play with(given in list nums)
# The batsman and the bowler each bring a number.
# If the numbers are same the batsman is out
# and if not the number the batsman brought is added as run(s) to his score.

# One to Five numbers are shown with number of fingers the number is.
# Six is shown with a thumb
# Ten is shown with fist 
# Twenty is shown with a index finger and a thumb

# :) Hope you enjoy it.

def AIbowl(guessed_bat):
    import random
    if len(guessed_bat) > 1:
        if guessed_bat[-1] == guessed_bat[-2]:
                    last = random.choice([True, False])
                    if last == True:
                        return guessed_bat[-1]
    for num in guessed_bat:
        if guessed_bat.count(num) > 1:
            should_I = random.choice([x for x in range(50)])
            verses = random.choice([x for x in range(10)])
            max_time = guessed_bat[0]
            if should_I >= verses:
                for num in guessed_bat:
                    if guessed_bat.count(num) > guessed_bat.count(max_time):
                        max_time = num
                return max_time
            else:
                break
    return random.choice(nums)

def toss(user_odd_or_even, user_num):
    import random
    comp_num = random.choice([1,5,3,20,3,1,5,10,20,6,2,3,10,2,3,20,3,5,1,2,6,20,3,2])
    print('Computer chose:',comp_num)
    if user_odd_or_even.lower() == 'o':
        if (comp_num + user_num) % 2 == 0:#computer won the toss
            return random.choice(['comp'])
        else:
            return None
    else:
        if (comp_num + user_num) % 2 != 0:#computer won the toss
            return random.choice(['comp'])
        else:
            return None

def bat_or_ball(winner):#toss function will be passed
    import random
    if winner == None:
        print('You have won the toss!')
        while True:
            print('\n--------')
            user_choose = input('(b) to bat and (f) to ball: ')
            if user_choose == 'b' or user_choose == 'f':
                break
            print('\n--------')
            print('Please enter something relevant.')
            continue
        return user_choose
    else:
        print('You lose the toss :(')
        comp_bat_ball = random.choice(['bat', 'ball'])
        print("Computer choose to %s" % (comp_bat_ball))
        return comp_bat_ball

def AIbat(guessed_bowl):
    import random
    ab = random.sample(nums, 6)
    ba = random.sample(nums, 6)
    abc = random.sample(nums, 6)
    a = random.sample(nums, 6)
    b = random.sample(nums, 6)
    c = random.sample(nums, 6)
    should_I = random.choice([x for x in range(10)])
    verses = random.choice([x for x in range(50)])
    if should_I < verses:
        return random.choice(random.choice([abc, a, ba, c, b, ab]))
    return guessed_bowl[-1]

def gameplay():
    while True:
        if start_game == 'b' or start_game == 'ball':
            guessed_bat = []
            score_user = 0
            while True:
                print('\n--------')
                play = True
                while play:
                    bat_num = input('Enter run(s): ')
                    if not(bat_num in ['1','2','3','4','5','6','10','20']):
                        print('\n--------')
                        print('Please enter something relevant.')
                        continue
                    bat_num = int(bat_num)
                    break
                guessed_bat += [bat_num]
                comp_ball = AIbowl(guessed_bat)
                print('\n--------')
                print('Your number:',bat_num)
                print('Computer\'s number:',comp_ball)
                if comp_ball == bat_num:
                    target = score_user+1
                    print('\n--------')
                    print('Oh! You are out!')
                    print('Your score is:',score_user)
                    print('Computer\'s target:',target)
                    guessed_bowl = []
                    score_comp = 0
                    while True:
                        print('\n--------')
                        while True:
                            ball_num = input('Enter bowling number: ')
                            if not(ball_num in ['1','2','3','4','5','6','10','20']):
                                print('\n--------')
                                print('Please enter something relevant.')
                                continue
                            ball_num = int(ball_num)
                            break
                        guessed_bowl += [ball_num]
                        comp_bat = AIbat(guessed_bowl)
                        print('\n--------')
                        print('Your number:',ball_num)
                        print('Computer\'s number:',comp_bat)
                        if comp_bat == ball_num:
                            if score_comp + comp_bat == score_user:
                                print('\n--------')
                                print('Scores are tied! Match drawn.')
                                print('Your score was:',score_user)
                                print('Computer\'s score was: %d' % (score_comp))
                                play = False
                                break
                            print('\n--------')
                            print('Congratulations! You won the match!')
                            print('Your score was:',score_user)
                            print('Computer\'s score was: %d' % (score_comp))
                            play = False
                            break
                        elif score_comp + comp_bat >= target:
                            score_comp += comp_bat
                            print('\n--------')
                            print('Alas! You lose! Better luck next time.')
                            print('Your score was:',score_user)
                            print('Computer\'s score was: %d' % (score_comp))
                            play = False
                            break
                        else:
                            score_comp += comp_bat
                            print('\n--------')
                            print('Score:',score_comp)
                else:
                    score_user += bat_num
                    print('\n--------')
                    print('Score:',score_user)
                    continue
                break
        
        elif start_game == 'f' or start_game == 'bat':
            guessed_bowl = []
            score_comp = 0
            while True:
                print('\n--------')
                play = True
                while play:
                    ball_num = input('Enter bowling number: ')
                    if not(ball_num in ['1','2','3','4','5','6','10','20']):
                        print('\n--------')
                        print('Please enter something relevant.')
                        continue
                    ball_num = int(ball_num)
                    break
                guessed_bowl += [ball_num]
                comp_bat = AIbat(guessed_bowl)
                print('\n--------')
                print('Your number:',ball_num)
                print('Computer\'s number:',comp_bat)
                if comp_bat == ball_num:
                    target = score_comp+1
                    print('\n--------')
                    print('Wow! You have out computer!')
                    print('Computer\'s score is:',score_comp)
                    print('Your target:',target)
                    guessed_bat = []
                    score_user = 0
                    while True:
                        print('\n--------')
                        while True:
                            bat_num = input('Enter run(s): ')
                            if not(bat_num in ['1','2','3','4','5','6','10','20']):
                                print('\n--------')
                                print('Please enter something relevant.')
                                continue
                            bat_num = int(bat_num)
                            break
                        guessed_bat += [bat_num]
                        comp_ball = AIbowl(guessed_bat)
                        print('\n--------')
                        print('Your number:',bat_num)
                        print('Computer\'s number:',comp_ball)
                        if comp_ball == bat_num:
                            if score_user + bat_num == score_comp:
                                print('\n--------')
                                print('Scores are tied! Match drawn.')
                                print('Your score was:',score_user)
                                print('Computer\'s score was: %d' % (score_comp))
                                play = False
                                break
                            print('\n--------')
                            print('Alas! You lose! Better luck next time.')
                            print('Your score was:',score_user)
                            print('Computer\'s score was: %d' % (score_comp))
                            play = False
                            break
                        elif score_user + bat_num >= target:
                            score_user += bat_num
                            print('\n--------')
                            print('Congratulations! You won the match!')
                            print('Your score was:',score_user)
                            print('Computer\'s score was: %d' % (score_comp))
                            play = False
                            break
                        else:
                            score_user += bat_num
                            print('\n--------')
                            print('Score:',score_user)
                else:
                    score_comp += comp_bat
                    print('\n--------')
                    print('Score:',score_comp)
                    continue
                break
        break

from os import system
system('cls')
nums = [4, 20, 1, 6, 3, 2, 10, 5]
print('Welcome Player!')
print('To Odd-Even Cricket \`o`/')
print('Version: 1.00.0')
while True:
    print('\n--------')
    user_odd_or_even = input('(o) for odd and (e) for even: ') 
    user_num = input('Enter a number: ')
    if (user_odd_or_even.lower() == 'o' or user_odd_or_even == 'e') and (user_num in ['1','2','3','4','5','6','10','20']):
        user_num = int(user_num)
        start_game = bat_or_ball(toss(user_odd_or_even, user_num))
        gameplay()
    else:
        print('\n--------')
        print('One or both of inputs are irrelevant.')
        continue
    print('\n--------')
    ask = input("(y) to play again and any other key to exit: ")
    if ask.lower() == 'y':
        continue
    else:
        print('\n--------')
        print('Thanks for playing!')
        break