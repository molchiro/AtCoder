def __main__():
    orders = []
    for i in range(5):
        orders.append(int(input()))
    last = min(orders, key=(lambda x: (x-1)%10))
    orders.remove(last)
    print(sum(map((lambda x: (x+9)//10*10), orders)) + last)
if __name__ == "__main__":
    __main__()