v = 9
while v <= 65:
    print(v, end=' ')
    v += 4
print()

k = 3
for x in range(13):
    print(k, end=' ')
    k *= 2
print()

for y in range(1, 41):
    m = y
    if y % 4 == 0:
        m = -1
        print(m, end=' ')
print()
