s = input()
res = ''.join([c for c in s if c.lower() not in 'aeiou'])
print("Without vowels:", res)