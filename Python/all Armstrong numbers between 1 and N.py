n = int(input())
for x in range(1, n+1):
    digits = len(str(x))
    if sum(int(d)**digits for d in str(x)) == x:
        print(x, end=' ')
print()