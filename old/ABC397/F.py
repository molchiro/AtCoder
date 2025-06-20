N = int(input())
A = list(map(int, input().split()))
ans = 0
B = []
seen = set()
for a in A:
    if a in seen:
        B.append(a)
    else:
        ans += 1
        seen.add(a)

# print(ans, B)

left = [0]
seen_l = set()
for b in B:
    if b in seen_l:
        left.append(left[-1])
    else:
        seen_l.add(b)
        left.append(left[-1]+1)
        
right = [0]
seen_r = set()
for b in B[::-1]:
    if b in seen_r:
        right.append(right[-1])
    else:
        seen_r.add(b)
        right.append(right[-1]+1)
right = right[::-1]
# print(left)
# print(right)

from bisect import bisect_left, bisect_right

tmp = 0

for i in range(len(B)+1):
    l = bisect_left(left, i)
    if l > len(B):
        continue
    for j in range(len(B)+1):
        ct = 0
        seen_m = set()
        for m in range(l, len(B)):
            if ct >= j:
                break

            b = B[m]
            if b in seen_m:
                continue
            else:
                ct += 1
                seen_m.add(b)
            
        
        if ct < j:
            break

        if i+j == len(B) and A[-1] == B[-1]:
            continue

        # print(i, j, l, m+1, i+j+right[m+1])

        tmp = max(tmp, i+j+right[m+1])

print(ans+tmp)
