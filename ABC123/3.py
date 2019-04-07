def __main__():
    N = int(input())
    trans = []
    for i in range(5):
        trans.append(int(input()))
    bn = min(trans)
    print(4 + (N-1)//bn + 1)
if __name__ == "__main__":
    __main__()