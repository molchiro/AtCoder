N, K = list(map(int, input().split()))
civils = list(map(int, input().split()))

base = K//N
thresh_n = K%N
thresh_a = sorted(civils)[thresh_n]
for c in civils:
    print(base + (1 if c < thresh_a else 0))