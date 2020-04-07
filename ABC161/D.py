import queue

K = int(input())
q = queue.Queue()
for i in range(1,10):
    q.put(i)
for i in range(K-1):
    x = q.get()
    if x%10 != 0: q.put(x*10 + x%10 - 1)
    q.put(x*10 + x%10)
    if x%10 != 9: q.put(x*10 + x%10 + 1)
print(q.get())
