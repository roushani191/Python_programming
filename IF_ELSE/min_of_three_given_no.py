#program to find min of three given number
a = int(input('Enter first no.:'))
b = int(input('Enter second no.:'))
c = int(input('Enter third no.:'))

if a<b and a<c :
    print('Minimum of the three given no. is ',a)

elif b<c and b<a :
    print('Minimum of the three given no. is ',b)   

else:
    print('Minimum of the three given no. is ',c)     