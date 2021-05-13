primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
A, B = list(map(int, input().split()))
Ns = [set() for _ in range(B-A+1)]
for i in range(A, B+1):
    for p in primes:
        if i%p == 0:
            Ns[i-A].add(p)
ans = 1
reminders = []
wildcards_n = 0
for x in Ns:
    if x == set():
        wildcards_n += 1
    else:
        reminders.append(x)

print(wildcards_n, reminders)


dic = {p: [] for p in primes}
for p in primes:
    tmp = []
    for x in reminders:
        if p in x:
            dic[p].append(x)
        else:
            tmp.append(x)
    # print(target)
    reminders = tmp[:]
print(dic)
for p in primes:
    for s in dic[p]:
        print(s)

H, W = list(map(int, input().split()))
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
list(map(int, input().split()))