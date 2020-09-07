count= 0
x = int(input())
y = -99999990
while(y < x):
    y = int(input())

while y > x:
    if y % 2 == 0:
        y = y // 2
        count += 1
        print(x , y)
    else:
        y += 1
        count += 1
        print(x , y)
    if x == y:
        break

while (y <x):
    y+= 1
    print(x, y)
    count += 1
    if x == y:
        break
print(count)
