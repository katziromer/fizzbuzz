lim = int(input("choose limit")) + 1
for x in range(1,lim):
    if x%15 != 0:
        if x%5==0: print("Buzz") 
        if x%3==0: print("Fizz")
        if x%3!=0 and x%5!=0: print(x)
    else: print("FizzBuzz")