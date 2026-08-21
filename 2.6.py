for i in range(10,38, 3):
    print(i, end=', ' if i != 37 else '\n')

for i in range(998,899, -2):
    print(i, end=', ' if i != 900 else '\n')

for i in range(20):
    if i % 2 == 0:
        print(1, end=', ' if i != 19 else '\n')
    else:
        print(-1, end=', ' if i != 19 else '\n')

for i in range(60):
    if i % 3 == 2:
        print(9, end=', 'if i != 59 else '\n')
    else:
        print(7, end=', 'if i != 59 else '\n')