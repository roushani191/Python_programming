f_num = int(input('Enter the 1st no.: '))
s_num = int(input('Enter the 2nd no.: '))

op = input('Enter the operator(+,-,/,*,%):') #operation user want to perform

if op == '+':
    print(f_num + s_num)

elif op == '-':
    print(f_num - s_num)

elif op == '*':
    print(f_num * s_num)

elif op == '/':
    print(f_num / s_num)

else: 
    print(f_num % s_num)