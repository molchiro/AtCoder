Q = int(input())
stack = [0]*100

for _ in range(Q):
    query = input()
    if query == "2":
        print(stack.pop())
    else:
        _, x = query.split()
        stack.append(int(x))