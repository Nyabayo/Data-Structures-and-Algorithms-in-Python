#The Fibonacci Number Algorithm using aLoop
prev2 = 0
prev1 = 1
print(prev2)
print(prev1)
for fibo in range(18):
    newfibo = prev2 + prev1
    print(newfibo)
    prev2 = prev1
    prev1 = newfibo
    