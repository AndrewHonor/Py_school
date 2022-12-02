x = int(input())
y = int(input())
for n in range(x if x %2 ==0 else x+1, y+1, 2):
    print(n, end=' ')
