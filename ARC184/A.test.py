import subprocess
FILE = "A.py"


# ans = [1, 15, 16, 100, 105, 300, 400, 500, 600, 1000]
ans = [x for x in range(991, 1001)]
coins = [x+1 in ans for x in range(1000)]
# print(coins)

process = subprocess.Popen(
    ["python3", FILE], 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)

process.stdin.write('1000 10 950\n')
process.stdin.flush()
while True:
    # print(process.stdout.readline().strip().split())
    inputs = process.stdout.readline().strip().split()
    # print(inputs)
    t, *nums = inputs
    if t == '!':
        print(*nums)
        exit(0)
    a, b = nums
    is_same = coins[int(a)-1] == coins[int(b)-1]
    # if a == '1':
        # print(is_same)
    # print(is_same)
    process.stdin.write(f'{int(not is_same)}\n')
    process.stdin.flush()

