H, W = list(map(int, input().split()))

S = [input() for _ in range(H)]

def judge(h0, w0, h1, w1):
    # print(h0, w0, h1, w1)
    global S
    h = h1-h0
    w = w1-w0
    for i in range(h*w//2):
        y = i//w
        x = i%w
        
        y_ = h-1-y
        x_ = w-1-x

        # print((h0+y, w0+x) , (h0+y_,w0+x_))

        if S[h0+y][w0+x] != S[h0+y_][w0+x_]:
            return 0

    return 1

ans = 0

for h0 in range(H):
    for w0 in range(W):
        for h1 in range(h0+1, H+1):
            for w1 in range(w0+1, W+1):
                if judge(h0, w0, h1, w1):
                    ans += 1

print(ans)