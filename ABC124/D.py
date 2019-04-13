N, K = list(map(int, input().split()))
G_S = list(input())

l_blob = [0,0]
c_blob = [0,0]
r_blob = [0,0]
l, r = 0,0

prev = '1'
temp = 0

for i in range(K):
    for i, s in enumerate(G_S):
        if s == '1':
            if prev == '0':
                r_blob = [i,i]
            else:
                r_blob[1] = i
        else:
            if prev == '0':
                c_blob[1] = i
            else:
                x = r_blob[1] - l_blob[0]
                if x > temp and c_blob != [0,0]:
                    l, r = c_blob
                    temp = x

                c_blob = [i,i]
                l_blob = r_blob[:]
            r_blob = [i,i]
        prev = s

    x = r_blob[1] - l_blob[0]
    if x > temp and c_blob != [0,0]:
        l, r = c_blob

    if c_blob == [0,0]:
        break

    for j in range(r-l+1):
        G_S[l+j] = '1' if G_S[l+j] == '0' else '0'
    
ans = 0
temp = 0
for s in G_S:
    if s == '1':
        temp += 1
    else:
        ans = max(ans,temp)
        temp = 0

print(ans)


