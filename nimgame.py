n, t = map(int, input().split())
piles = list(map(int, input().split()))

xor_value = 0

for stones in piles:
    xor_value ^= stones

if xor_value != 0:
    print(t)
else:
    if t == 1:
        print(2)
    else:
        print(1)