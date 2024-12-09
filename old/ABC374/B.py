S = (input()+'X'*100)[:100]
T = (input()+'X'*100)[:100]
for i in range(100):
    if S[i] != T[i]:
        print(i+1)
        break
else:
    print(0)