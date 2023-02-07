def reverse_number(n):
    if str(n)[0] == '-':
        n = -1*int(''.join(reversed(str(n)[1:])))
    else:
        n = int(''.join(reversed(str(n))))
    return n

num1 = 123
print(reverse_number(num1))

num2 = 254
print(reverse_number(num2))

num3 = -981
print(reverse_number(num3))