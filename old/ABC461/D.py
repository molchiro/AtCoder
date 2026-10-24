class cumsum_2d:
    def __init__(self, two_d_list: list[list[int]]):
        H = len(two_d_list)
        W = len(two_d_list[0])
        self.inner_cumsum = [[0]*(W+1) for h in range(H+1)]
        for h in range(H):
            for w in range(W):
                self.inner_cumsum[h+1][w+1] += self.inner_cumsum[h+1][w] + two_d_list[h][w]
        for h in range(H):
            for w in range(W):
                self.inner_cumsum[h+1][w+1] += self.inner_cumsum[h][w+1]
    
    def get(self, p1: tuple[int, int], p2: tuple[int, int]) -> int:
        """左上と右下を指定して累積和を取得する

        左上、右下、いずれもその座標を含めた範囲

        Args:
            p1 tuple[int, int]: 左上の座標 0-indexed
            p1 tuple[int, int]: 右下の座標 0-indexed

        Returns:
            int: 累積和



        Examples:

            p1=(1, 2), p1=(3, 3)の時、
              two_d_list[1][2]
              + two_d_list[1][3]
              + two_d_list[2][2]
              + two_d_list[2][3]
              + two_d_list[3][2]
              + two_d_list[3][3]
            の結果を返す

        Note:
            注意事項や注釈など

        """
        h1, w1 = p1
        h2, w2 = p2
        ans = 0
        ans += self.inner_cumsum[h2+1][w2+1]
        ans -= self.inner_cumsum[h1][w2+1]
        ans -= self.inner_cumsum[h2+1][w1]
        ans += self.inner_cumsum[h1][w1]
        return ans


H, W, K = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]
# print(S)

field = []
for s in S:
    field.append([int(x) for x in s] + [10**18])

# print(field)
c2d = cumsum_2d(field)

ans = 0
for h in range(H):
    for w in range(W):
        ok = w-1
        ng = W
        while ng - ok > 1:
            test = (ng+ok)//2
            if c2d.get((h, w), (h, test)) < K:
                ok = test
            else:
                ng = test
        l = ok # ギリKを超えない
        # print(l)

        ok = W
        ng = -1
        while ok - ng > 1:
            test = (ng+ok)//2
            if c2d.get((h, w), (h, test)) > K:
                ok = test
            else:
                ng = test
        r = ok # ギリKを超える


        ans += max(r-l-1, 0)

        for dh in range(1, H-h):

            while l >= w and c2d.get((h, w), (h+dh, l)) >= K:
                l -= 1

            while r-1 > l and c2d.get((h, w), (h+dh, r-1)) > K:
                r -= 1
            ans += max(r-l-1, 0)


            # print('h, w, h+dh, l, r, ans', (h, w, h+dh, l, r, ans))

print(ans)