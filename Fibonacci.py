i = 0
j = 1
k = 0
fib = 0
count = input('Enter number of Fibonacci numbers:')
check = True
while check == True:
    try:
        count = int(count)
        check = False
    except ValueError:
        count = input('Enter number of Fibonacci numbers, again:')
print('Fibonacci sequance:')
while i < count:
    print(str(i+1) + ':' + str(fib))
    fib = j + k
    j = k
    k = fib
    i += 1
