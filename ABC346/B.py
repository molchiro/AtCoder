piano = 'wbwbwwbwbwbw'
inf_piano = piano*200
W, B = list(map(int, input().split()))
from collections import Counter
for i in range(12):
    c = Counter(list(inf_piano[i:i+W+B]))
    if c['w'] == W and c['b'] == B:
        print('Yes')
        exit()

print('No')
