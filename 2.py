n = int(input('please give a positive integer: '))
if n > 0:
    p = 1 # product
    k = n
    while k > 1:
        p *= k # p = p * k
        k -= 1 # k = k - 1
    print(f'{n}! = {p}')
else:
    print('give integer is not positive')
