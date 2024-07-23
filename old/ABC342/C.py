N = int(input())
S = input()
Q = int(input())
dic = {chr(ord('a')+i): chr(ord('a')+i) for i in range(26)}
for _ in range(Q):
    c, d = input().split()
    for k, v in dic.items():
        if v == c:
            dic[k] = d
print(''.join([dic[s] for s in S]))