N = int(input())
A = list(input())
# print(A)

def solve(S, C):
    global N
    # print(S, C)
    if len(S) == 3:
        ones = 0
        for i in range(3):
            if S[i] == '1':
                ones += 1

        if ones == 3:
            C.sort()
            return C[0]+C[1]
        elif ones == 2:
            tmp = []
            for i in range(3):
                if S[i] == '1':
                    tmp.append(C[i])
            return min(tmp)
        elif ones == 1:
            tmp = []
            for i in range(3):
                if S[i] == '0':
                    tmp.append(C[i])
            return min(tmp)
        else:
            C.sort()
            return C[0]+C[1]
    # elif len(S) == 3**N:
    #     res = []
    #     c = []
    #     ones = 0
    #     zeros = 0
    #     for i in range(len(S)//3):
    #         for j in range(3):
    #             s = S[i*3+j]
    #             if s == '1':
    #                 ones += 1
    #             else:
    #                 zeros += 1
                
    #         if ones >= 2:
    #             res.append('1')
    #             c.append(2-zeros)
    #         else:
    #             res.append('0')
    #             c.append(2-ones)
    else:
        res = []
        c = []
        for i in range(len(S)//3):
            ones = 0
            zeros = 0
            for j in range(3):
                s = S[i*3+j]
                if s == '1':
                    ones += 1
                else:
                    zeros += 1
            # print(i, i*3, ones)
                
            if ones == 3:
                # 操作回数が少ない方から二箇所選んで操作する
                res.append('1')
                tmp = []
                for j in range(3):
                    tmp.append(C[i*3+j])
                tmp.sort()
                c.append(tmp[0]+tmp[1])
            elif ones == 2:
                # 元々1だったもののうち操作回数が少なくて住む方を採用する
                res.append('1')
                tmp = 3
                for j in range(3):
                    if S[i*3+j] == '0':
                        continue
                    tmp = min(tmp, C[i*3+j])
                c.append(tmp)
            elif ones == 1:
                # 元々0だったもののうち操作回数が少なくて住む方を採用する
                res.append('0')
                tmp = 3
                for j in range(3):
                    if S[i*3+j] == '1':
                        continue
                    tmp = min(tmp, C[i*3+j])
                c.append(tmp)
            else:
               # 操作回数が少ない方から二箇所選んで操作する
                res.append('0')
                tmp = []
                for j in range(3):
                    tmp.append(C[i*3+j])
                tmp.sort()
                c.append(tmp[0]+tmp[1])


    return solve(res, c)

print(solve(A, [1]*(3**N)))