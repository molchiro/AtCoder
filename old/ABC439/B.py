N = int(input())

def act(n):
    l = list(str(n))
    l = [int(x)**2 for x in l]
    return sum(l)

seen = set()
while not N in seen:
    seen.add(N)
    N = act(N)
    # print(N)

print('Yes' if N==1 else 'No')