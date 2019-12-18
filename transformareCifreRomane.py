convertor={'1':'I', '4':'IV', '5':'V', '9':'IX', '10':'X', '40':'XL', '50':'L', '90':'XC', '100':'C', '400':'CD', '500':'D', '900':'CM', '1000':'M'}

def lowerOrder(currOrder):
    if currOrder=='1000':
        return '900'
    if currOrder=='900':
        return '500'
    if currOrder=='500':
        return '400'
    if currOrder=='400':
        return '100'
    if currOrder=='100':
        return '90'
    if currOrder=='90':
        return '50'
    if currOrder=='50':
        return '40'
    if currOrder=='40':
        return '10'
    if currOrder=='10':
        return '9'
    if currOrder=='9':
        return '5'
    if currOrder=='5':
        return '4'
    if currOrder=='4':
        return '1'
    if currOrder=='1':
        return '1'

num=int(input())
if num>3999:
    print('Transformation impossible. Romans weren\'t that smart')
elif num<0:
    print('Error, negative numbers is arab invention')
else:
    roman=''
    currentOrder='1000'
    while num>0:
        intOrder=int(currentOrder)
        coef=num//intOrder
        num-=intOrder*coef
        roman+=convertor[currentOrder]*coef
        currentOrder=lowerOrder(currentOrder)

print(roman)