a = int(input('please give the value of a: '))
b = int(input('please give the value of b: '))

result = 0

if a >= 100:
    if b <= 50:
        result = 1
else:
    if b >= 100:
        if a <= 50:
            result = 1

print(result)