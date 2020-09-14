N = int(input())
add = []
diff = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    add.append(x+y)
    diff.append(x-y)
add.sort()
diff.sort()
print(max(add[-1]-add[0], diff[-1]-diff[0]))