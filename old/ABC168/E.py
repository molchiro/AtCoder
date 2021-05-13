from collections import Counter

N = int(input())

pos_box = []
neg_box = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    AB = A * B
    if AB > 0:
        pos_box.append(AB)
    else:
        neg_box.append(-AB)

pos_box = Counter(pos_box)
neg_box = Counter(neg_box)

print(pos_box.keys())
print(neg_box.keys())

paired = set(pos_box.keys()) & set(neg_box.keys())
pos_only = set(pos_box.keys()).difference(paired)
neg_only = set(neg_box.keys()).difference(paired)

print(paired, pos_only, neg_only)

ans = 1
for key in paired:
    ans *= 2**pos_box[key] + 2**neg_box[key] - 1

friendly_n = sum([pos_box[key] for key in pos_only]) + sum([neg_box[key] for key in neg_only])

ans *= 2**friendly_n
ans -= 1

print(ans)

