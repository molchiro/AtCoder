K = int(input())
S = input()
T = input()
S_ = [S.count(str(i)) for i in range(1, 10)]
T_ = [T.count(str(i)) for i in range(1, 10)]

deck = [K - S_[i] - T_[i] for i in range(9)]

# print(deck)

a = 0
b = 0
for i in range(9):
    for j in range(9):
        if deck[i] == 0:
            continue
        if deck[j] == 0:
            continue
        if i == j and deck[i] == 1:
            continue
        

        if i == j:
            c = deck[i]*(deck[i]-1)
        else:
            c = deck[i]*deck[j]
        
        a += c
        
        takahashi = S_[:]
        takahashi[i] += 1
        p_tahakashi = sum([(i+1)*10**takahashi[i] for i in range(9)])
        aoki = T_[:]
        aoki[j] += 1
        p_aoki = sum([(i+1)*10**aoki[i] for i in range(9)])
        if p_tahakashi > p_aoki:
            b += c
        
        # print(i+1, j+1, p_tahakashi, p_aoki)

print(b/a)