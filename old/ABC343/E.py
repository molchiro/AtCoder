import dataclasses

@dataclasses.dataclass
class Line:
    # l < r を満たさない時の動作は検証していない
    l: float
    r: float
    
    def len(self):
        if self.l == None or self.r == None:
            return 0
        else:
            return self.r - self.l

    def __and__(self,other):
        """
        ２つの共通区間を返す
        ２つの区間が共通部分を持たない時は[None, None)を返す
        """

        if None in (self.l, self.r, other.l, other.r):
            return Line(None, None) 

        if self.l <= other.l:
            a, b = self, other
        else:
            a, b = other, self
        
        if a.r < b.l:
            return Line(None, None)
        
        return Line(b.l, min(a.r, b.r))

    def __or__(self,other):
        """
        ２つを結合した区間を返す
        ２つの区間が連続しない時は[None, None)を返す
        """
        if self.l <= other.l:
            a, b = self, other
        else:
            a, b = other, self
        
        if a.r < b.l:
            return Line(None, None)
        
        return Line(a.l, max(a.r, b.r))
    
assert Line(1, 3.2).len() == 2.2
assert Line(1, 4) | Line (2, 5) == Line(1, 5)
assert Line(1, 3) | Line (3, 5) == Line(1, 5)
assert Line(1, 2) | Line (4, 5) == Line(None, None)
assert Line(1, 4) & Line (2, 5) == Line(2, 4)
assert Line(1, 3) & Line (3, 5) == Line(3, 3)
assert Line(1, 2) & Line (4, 5) == Line(None, None)

@dataclasses.dataclass
class Square:
    x: Line
    y: Line

    def S(self):
        # 区間がfloatの時は誤差が生じることに注意して使う
        return self.x.len() * self.y.len()
    
    def __and__(self, other):
        x = self.x & other.x
        y = self.y & other.y
        return Square(x, y)

assert Square(Line(1, 2), Line(-3, 0)).S() == 3
assert Square(Line(3, 3), Line(2, 3)).S() == 0
assert Square(Line(1, 2), Line(None, 3)).S() == 0
assert Square(Line(1, 2.2), Line(-3, 0)).S() - 3.6 <= 10**10
assert Square(Line(1, 3), Line(2, 5)) & Square(Line(2, 4), Line(1, 3)) == Square(Line(2, 3), Line(2, 3))
assert Square(Line(1, 3), Line(2, 5)) & Square(Line(2, 4), Line(-1, 1)) == Square(Line(2, 3), Line(None, None))
assert Square(Line(1, 3), Line(2, 5)) & Square(Line(3, 4), Line(1, 3)) == Square(Line(3, 3), Line(2, 3))

@dataclasses.dataclass
class Qube:
    x: Line
    y: Line
    z: Line

    def V(self):
        # 区間がfloatの時は誤差が生じることに注意して使う
        return self.x.len() * self.y.len() * self.z.len()
    
    def __and__(self, other):
        x = self.x & other.x
        y = self.y & other.y
        z = self.z & other.z
        return Qube(x, y, z)
    

assert Qube(Line(1, 2), Line(-3, 0), Line(5, 8)).V() == 9
assert Qube(Line(3, 3), Line(2, 3), Line(5, 8)).V() == 0
assert Qube(Line(1, 3), Line(2, None), Line(5, 8)).V() == 0
assert Qube(Line(1, 2.2), Line(-3, 0), Line(5, 8)).V() == 10.8
assert Qube(Line(1, 3), Line(2, 5), Line(5, 8)) & Qube(Line(2, 4), Line(1, 3), Line(6, 9)) == Qube(Line(2, 3), Line(2, 3), Line(6, 8))


V1, V2, V3 = list(map(int, input().split()))

qube0 = Qube(Line(0, 7), Line(0, 7), Line(0, 7))

V = 7*7*7*3
for x1 in range(-1, 8):
    for y1 in range(-1, 8):
        for z1 in range(-1, 8):
            qube1 = Qube(Line(x1, x1+7), Line(y1, y1+7), Line(z1, z1+7))
            for x2 in range(-1, 8):
                for y2 in range(-1, 8):
                    for z2 in range(-1, 8):
                        qube2 = Qube(Line(x2, x2+7), Line(y2, y2+7), Line(z2, z2+7))
                        qube01 = qube0 & qube1
                        qube02 = qube0 & qube2
                        qube12 = qube1 & qube2
                        qube012 = qube01 & qube2
                        v3 = qube012.V()
                        v2 = qube01.V() + qube02.V() + qube12.V() - 3*v3
                        v1 = V - 2*v2 - 3*v3
                        # print(v1, v2, v3)
                        # input()
                        if (v1, v2, v3) == (V1, V2, V3):
                            print('Yes')
                            print(0, 0, 0, x1, y1, z1, x2, y2, z2)
                            exit()

print('No')