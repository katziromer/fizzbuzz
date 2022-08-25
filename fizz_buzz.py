num = 1
x = int(input("choose limit"))
while num<=x:
    if num%15 !=0:
        if num%3 == 0:print("Fizz")
        if num%5 == 0:print("Buzz")
        if num%3 != 0 and num%5 !=0:print(num)
    else: print("FizzBuzz")
    num+=1   