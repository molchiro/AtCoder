def __main__():
    P = []
    for i in range(5):
        P.append(int(input()))
    k = int(input())
    
    for i in range(4):
        for j in range(i+1,5):
            if abs(P[i] - P[j]) > k:
                print(":(")
                return
    print("Yay!")
    return

if __name__ == "__main__":
    __main__()
