from collections import defaultdict

N = int(input())

dd = defaultdict(int)

for i in range(1, 10**4):
    if i**2 > N:
        break
    for j in range(i+1, 10**4):
            if i**2 + j**2 > N:
                break

            dd[i**2 + j**2] += 1
            # print(i, j)

ans = []
for k, v in dd.items():
     if v == 1:
          ans.append(k)
ans.sort()
print(len(ans))
print(*ans)
