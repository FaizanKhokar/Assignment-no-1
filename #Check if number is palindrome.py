#Check if number is palindrome
Number = input('Enter your number: ')
Number1 = Number
Number2 = Number1[::-1]
if Number1 == Number2 :
    print('Given number is a palindrome')
else:
    print('Given number is not a palindrome')