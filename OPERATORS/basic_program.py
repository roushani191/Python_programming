#sum of the digits of three digit no. enterd by user
number = int(input('Enter a 3 digit number: '))
a = number%10
number = number//10
b = number%10
number = number//10
c = number%10
print('sum of the digits:',a+b+c)
