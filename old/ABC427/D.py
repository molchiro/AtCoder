from functools import cache



T = int(input())
for _ in range(T):

    N, M, K = list(map(int, input().split()))
    board = input()
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        graph[a].append(b)

    # 残りnターンでplayerが勝つことが確定する手が存在するならtrue
    @cache
    def solve(params):
        u, player, k = params
        global graph, board
        if k == 1:
            for v in graph[u]:
                if board[v] == player:
                    return True
            else:
                return False
        
        # 相手が勝つ=自分が負けるなので、falseになる手を探索する
        for v in graph[u]:
            if solve((v, 'A' if player == 'B' else 'B', k-1)):
                continue
            return True
        else:
            return False
    
    print('Alice' if solve((0, 'A', 2*K)) else 'Bob')