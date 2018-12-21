import time
import math

num = int(input("Enter number"))
i = 2
start_time = time.time()
while i < math.sqrt(num):
    if num % i == 0:
        print("It's a prime!")
        num = 0
    i += 1
if num != 0:
    print("It was not a prime")
    print("It was divisible by"+(i-1))

print("--- %s seconds ---" % (time.time() - start_time))
