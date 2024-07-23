S = input()
counter = [0]*26
M = 0
for s in S:
    idx = ord(s) - ord('a')
    counter[idx] += 1
    M = max(counter[idx], M)
for i in range(26):
    if counter[i] == M:
        print(chr(ord('a')+i))
        break