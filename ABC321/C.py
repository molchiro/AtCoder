_321_like_number_list = []
for i in range(1, 1<<10):
    tmp = ''
    for j in range(10):
        if i >> j & 1:
            tmp += str(j)
    _321_like_number_list.append(int(tmp[::-1]))
_321_like_number_list.sort()

K = int(input())
# 0番目の要素が0であることに注意
print(_321_like_number_list[K])
