#Calculate the multiplication and sum of two numbers
number1 = int(input('Enter first number : '))
number2 = int(input('Enter second number : '))
product = number1 * number2
sum = number1 + number2
#Print product if it is lower than or equal to 1000
if product <=1000 :
    print('The product of two given numbers is', product)
#Otherwise return sum
else:
    print('The sum of two given numbers is', sum)