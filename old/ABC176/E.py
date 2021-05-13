H, W, M = list(map(int, input().split()))
hrz = [0]*H
vrt = [0]*W
targets = set()
for _ in range(M):
    h, w = list(map(lambda x: int(x) - 1, input().split()))
    targets.add((h, w))
    hrz[h] += 1
    vrt[w] += 1

hrz_max = max(hrz)
vrt_max = max(vrt)
hrz_max_lines = [i for i in range(H) if hrz[i] == hrz_max]
vrt_max_lines = [i for i in range(W) if vrt[i] == vrt_max]
for h in hrz_max_lines:
    for w in vrt_max_lines:
        if not (h, w) in targets:
            print(hrz_max+vrt_max)
            exit()
print(hrz_max+vrt_max-1)
