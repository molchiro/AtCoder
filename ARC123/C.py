T = int(input())
for _ in range(T):
    S = input()
    ans = 0
    while S != '0':
        ans += 1
        if int(S[0]) > 3:
            A = [3]*len(S)
        else:
            A = [int(S[0])]
            for i in range(1, len(S)):
                if int(S[i]) > 3:
                    A += [3]*(len(S)-i)
                    break
                elif int(S[i]) == 0:
                    A[-1] -= 1
                    A += [3]*(len(S)-i)
                    break
                else:
                    A.append(int(S[i]))
        A_ = ''.join([str(a) for a in A])
        A_ = int(A_)
        # print(S, A)
        S_ = int(S) - int(A_)
        if S_ == 0:
            break
        S_ = str(S_)
        # print(S_)
        for i, s in enumerate(S_):
            if s == '0':
                # print('hoge')
                A[i] -= 1
        A = ''.join([str(a) for a in A])
        A = int(A)
        # print(S, A)
        S = int(S) - int(A)
        S = str(S)
    print(ans)