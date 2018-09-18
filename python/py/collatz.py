def collatz(number):
    backNumber = 0
    if number % 2 == 0:
        backNumber = number // 2
    else:
        backNumber = 3 * number + 1
    print(backNumber)
    return backNumber


try:
    n = int(input())
    i = 0
    while True:
        i += 1
        n = collatz(n)
        if n == 1:
            break
    print('number sum:' + str(i))
except:
    print('Please input a integer.')
    
    
    