n = int(input())
digits = len(str(n))
print("Armstrong" if sum(int(d)**digits for d in str(n)) == n else "Not Armstrong")