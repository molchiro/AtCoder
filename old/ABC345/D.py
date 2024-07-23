N, H, W = list(map(int, input().split()))
TILES = [tuple(map(int, input().split())) for _ in range(N)]

from itertools import permutations

class Board:
    def __init__(self, H, W) -> None:
        self.H = H
        self.W = W
        self.cels = [[0]*W for _ in range(H)]

    def put(self, h, w, tile: tuple[int, int]):
        for i in range(tile[0]):
            # はみ出るか確認
            if not 0 <= h+i < self.H:
                return False
            for j in range(tile[1]):
                # はみ出るか確認
                if not 0 <= w+j < self.W:
                    return False
                # すでに置かれていないか確認
                if self.cels[h+i][w+j]:
                    return False
                # 置く
                self.cels[h+i][w+j] = 1
        # 全マスおけたなら正常終了
        return True

# 並び替え*90度回転 N! x 2^N 通り
for order in permutations(range(N), N):
    for i in range(1<<N):
        # 状態の初期化
        tiles = []
        for j in range(N):
            A, B = TILES[order[j]]
            if i>>j & 1:
                tiles.append((B, A))
            else:
                tiles.append((A, B))
        board = Board(H, W)
        now = 0

        # act
        while now < H*W:
            h = now//W
            w = now%W
            now += 1
            # すでにタイルがあるか確認する
            if board.cels[h][w]:
                continue
            # タイルを置く
            # もうタイルがないなら失敗
            if not tiles:
                break
            # タイルを取り出して置く
            tile = tiles.pop()
            res = board.put(h, w, tile)
            # はみ出たなら失敗
            if res == False:
                break
        else:
            # 一度もbreakせずにwhileを抜けたら成功
            print('Yes')
            # print(board.cels)
            exit()
    
    # input()



print('No')
            
