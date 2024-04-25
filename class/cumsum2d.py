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