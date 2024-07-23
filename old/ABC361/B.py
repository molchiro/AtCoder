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
    
a, b, c, d, e, f = list(map(int, input().split()))
g, h, i, j, k, l = list(map(int, input().split()))

A = Qube(Line(a, d), Line(b, e), Line(c, f))
B = Qube(Line(g, j), Line(h, k), Line(i, l))
C = A&B

# print(C.V())
print('Yes' if C.V() > 0 else 'No')