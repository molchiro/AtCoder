from itertools import product

poly1 = [list(input()) for _ in range(4)]
poly2 = [list(input()) for _ in range(4)]
poly3 = [list(input()) for _ in range(4)]

def check(poly1, x1, y1, poly2, x2, y2, poly3, x3, y3):
    field = [[0]*4 for _ in range(4)]
    def put(poly, x, y):
        # はみ出たらエラー
        try:
            for i, row in enumerate(poly):
                for j, e in enumerate(row):
                    if e == "#":
                        field[y+j][x+i] += 1
        except IndexError:
            raise

    try:
        put(poly1, x1, y1)
        put(poly2, x2, y2)
        put(poly3, x3, y3)
    except:
        return False
    
    return all([x for row in field for x in row])

# poly2とpoly3の回転を全探索
for _ in range(4):
    for _ in range(4):
        # 各polyの左上の位置を全探索
        for x1, y1, x2, y2, x3, y3 in product(range(4), repeat=6):
            if check(poly1, x1, y1, poly2, x2, y2, poly3, x3, y3):
                print('Yes')
                exit()
        poly3 = poly2[::-1]
        poly3 = list(map(list, zip(*poly2)))
    poly2 = poly2[::-1]
    poly2 = list(map(list, zip(*poly2)))
print('No')