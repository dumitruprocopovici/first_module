firstNumber = input('Enter a number:')
check = True
while check == True:
    try:
        firstNumber = float(firstNumber)
        check = False
    except ValueError:
        firstNumber = input('Enter a number, again:')

operator = input('Enter an operator:')
operatorList = ('+', '-', '*', '/')
while not (operator in operatorList):
    operator = input('Enter an operator, again:')

secondNumber = input('Enter a 2nd number:')
check = True
while check == True:
    try:
        secondNumber = float(secondNumber)
        check = False
    except ValueError:
        secondNumber = input('Enter a 2nd number, again:')

if operator == '+':
    Result = firstNumber + secondNumber
elif operator == '-':
    Result = firstNumber - secondNumber
elif operator == '*':
    Result = firstNumber * secondNumber
elif operator == '/':
    Result = firstNumber / secondNumber


print('Result=' + str(Result))
