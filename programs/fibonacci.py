def fib(m):
    """Gives fibonacci number
        of m. """
    if m < 2:
        return 1
    elif m > 2:
        return fib(m-1) + fib(m-2)
    else:
        print("Please enter something valid.")
        return 'retry'#returns 'retry' if something irrelevant is entered.
def checkfib(n):
    """Checks if n is a
            fibonacci number. """
    if n < 2:
        return True
    elif n > 2:
        if fib(n-1) + fib(n-2) == n:
            return True
        return False
    else:
        print("Please enter something valid.")
        return 'retry'#returns 'retry' if something irrelevant is entered.
while True:
    what = input("(c) to check if number is a fibonacci (f) to find fibonacci number.")
    while True:
        if what == 'c':
            n = int(input("Enter number: "))
            result = checkfib(n)
            if result != 'retry':
                print(result)
            else:
                continue
        elif what == 'f':
            m = int(input("Enter a number: "))
            result = fib(m)
            if result != 'retry':
                continue
            else:
                print(result)
        else:
            print("Please enter something relevant.")
            continue