N = int(input())
R = input()
C = input()

board = [None]*(N**2)

def judge():
    # print(board)
    # 行・列の条件
    # print('#1-1')
    for i in range(N):
        x = board[i*N:(i+1)*N]
        if x.count('A') > 1 or x.count('B') > 1 or x.count('C') > 1 or x.count('.') > N-3:
            return False
    # print('#1-2')
    for i in range(N):
        x = board[i::N]
        if x.count('A') > 1 or x.count('B') > 1 or x.count('C') > 1 or x.count('.') > N-3:
            return False
    # Rの条件
    # print('#2')
    for i, c in enumerate(R):
        for j in range(N):
            x = board[i*N+j]
            if x == None or x == c:
                break
            if x == '.':
                continue
            if x != c:
                return False
    # Cの条件
    # print('#3')
    for i, c in enumerate(C):
        for j in range(N):
            x = board[i+j*N]
            if x == None or x == c:
                break
            if x == '.':
                continue
            if x != c:
                return False
        
    return True

def dfs(i):
    # print(board)
    # input()
    if i==N**2:
        return True
    
    for s in ['A', 'B', 'C', '.']:
        board[i] = s
        if judge():
            if dfs(i+1):
                return True
        board[i] = None
    else:
        return False

if dfs(0):
    print('Yes')
    for i in range(N):
        print(''.join(board[i*N:(i+1)*N]))
else:
    print('No')