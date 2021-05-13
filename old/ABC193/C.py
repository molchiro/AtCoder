N = int(input())
rejects = set()
for i in range(2, int(N**0.5)+1):
    j = 2
    while i**j <= N:
        rejects.add(i**j)
        j += 1

print(N-len(rejects))