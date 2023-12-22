# taking INPUTS
x = int(input('Enter a number:'))
print(x)
print(type(x))

## taking list as input
# one by one
n = int(input('Enter the list size:'))
List = list()
print('Enter the input elements:')
for i in range(0,n):
    List.append(input())
print('Input List seen', List)

# using list and map
print('Enter the input list:')
List = list(map(int, input().split()))
print('Input List seen', List)


# giving OUTPUTS
print('Hello World!')
print(List)
print('AB CD', end='/')
print('S T I', sep='&')


# managing imports
from math import factorial, gcd
print('factorial of 5 = ', factorial(5))
print('GCD of 24,100 =', gcd(24, 100))