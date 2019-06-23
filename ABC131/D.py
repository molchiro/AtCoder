def main():
    N = int(input())
    tasks = []
    for i in range(N):
        tasks.append(list(map(int, input().split())))
    tasks.sort(key=lambda x: x[1])
    t = 0
    for task in tasks:
        t += task[0]
        if t > task[1]:
            print('No')
            return
    print('Yes')
if __name__ == "__main__":
    main()
