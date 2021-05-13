ST = input().split()
AB = list(map(int, input().split()))
U = input()
AB[ST.index(U)] -= 1
print(*AB)
