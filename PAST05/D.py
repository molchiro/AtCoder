N = int(input())
S = [input() for _ in range(N)]
S.sort(key=lambda x: (int(x), -len(x)))
print(*S, sep='\n')