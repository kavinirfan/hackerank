"""n = int(input())
zombies = list(map(int, input().split()))
B = int(input())

for zi in zombies:
    if B < zi:
        print("NO")
        break

    B -= (zi % 2) + (zi // 2)
else:
   print("YES")
"""
"""n, B = map(int, input().split())
zombies = list(map(int, input().split()))

for zi in zombies:
    if B < zi:
        print("NO")
        break

    B -= (zi % 2) + (zi // 2)
else:
    print("YES")
"""
"""n = int(input())
B = int(input())
zombies = list(map(int, input().split()))

for zi in zombies:
    if B < zi:
        print("NO")
        break

    B -= (zi % 2) + (zi // 2)
else:
    print("YES")
"""
"""n = int(input())
B = int(input())

zombies = list(map(int, input().split()))

for zi in zombies:
    if B < zi:
        print("NO")
        break

    B -= (zi % 2) + (zi // 2)
else:
    print("YES")
"""
n = int(input("Enter the number of zombies: "))
B = int(input("Enter Bob's energy: "))

zombies = list(map(int, input("Enter zombie energies: ").split()))

if len(zombies) != n:
    print("Please enter exactly", n, "zombie energies.")
else:
    for zi in zombies:
        if B < zi:
            print("NO")
            break

        B -= (zi % 2) + (zi // 2)
    else:
        print("YES")