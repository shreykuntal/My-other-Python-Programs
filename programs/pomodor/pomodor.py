#POMODOR PROGRAM! AUDIO FILE ALSO GIVEN TO TEST. PLEASE ENTER RELETIVE PATH TO AUDIO FILE.
import pygame
import time
nums = '1234567890'
def sound(file):#function for playing sound
    pygame.init()#initialises pygame
    pygame.mixer.init()#initialises pygame mixer
    pygame.mixer.music.load(file)#loads music file
    pygame.mixer.music.play()#plays music file
    time.sleep(4)#program sleeps for 4 seconds
    pygame.mixer.music.stop()#stops music file
while True:
    fine = ''#if 'n' then user input is not valid. Used below.
    pomodor_min = input("Enter pomodor time(mins): ")
    for check in range(len(pomodor_min)):#checks if user input is valid input
        if not(pomodor_min[check] in nums):
            print("Please don't enter decimal or enter something relevant.\n")
            fine = 'n'
            break
    if fine == 'n':
        continue
    else:
        break
while True:
    fine = ''
    pomodor_rest = input("Enter rest time(mins): ")
    for check in range(len(pomodor_rest)):#checks if user input is valid input
        if not(pomodor_rest[check] in nums):
            print("Please don't enter decimal or enter something relevant.\n")
            fine = 'n'
            break
    if fine == 'n':
        continue     
    else:
        break
pomodor_min = int(pomodor_min)
pomodor_rest = int(pomodor_rest)
print("\nPomodor Time(mins):",pomodor_min)
print("Rest Time(mins):",pomodor_rest)
time_in_sec = (pomodor_min * 60) 
rest_in_sec = (pomodor_rest * 60)
print("\nPress Ctrl+C to exit.\n")
print("Get ready to focus and press enter")
_=input()
while True:
    sec = -1 #current second
    n = 0 #if n exceeds time_in_sec or rest_in_sec under loops get break(Time checker)
    while n < time_in_sec:
        time.sleep(1)#program sleeps for 1 seconds
        if sec < 0:
            sec = 59
            pomodor_min -= 1
        time_left = str(pomodor_min).zfill(2)+':'+str(sec).zfill(2)#countdown timer and 
        print(time_left + "\r", end="")#everytime it prints overwrites previous
        n += 1
        sec -= 1
    sound('/home/shrey/Documents/python/programs/pomodor/alarm-clock-01.wav')#enter your path to your music file
    print("Time is up! Time for rest.\n")
    n = 0
    sec = -1
    while n < rest_in_sec:
        time.sleep(1)#program sleeps for 1 seconds
        if sec < 0:
            sec = 59
            pomodor_rest -= 1
        time_left = str(pomodor_rest).zfill(2)+':'+str(sec).zfill(2)
        print(time_left + "\r", end="")
        n += 1
        sec -= 1
    print("Time is up! Focus on your work.\n")    
    sound('/home/shrey/Documents/python/programs/pomodor/alarm-clock-01.wav')#enter your path to your music file
    pomodor_min = int(time_in_sec/60)
    pomodor_rest = int(rest_in_sec/60)