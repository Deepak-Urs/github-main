def sumOfDigits(num):
    assert int(num) == num and num >= 0, 'Enter a positive integer'
    if num == 0:
        return 0
    else:
        return int(num%10) + int(num//10)
    
print(sumOfDigits(12))
print(sumOfDigits(-12))