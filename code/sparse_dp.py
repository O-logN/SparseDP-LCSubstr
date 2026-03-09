from dataclasses import dataclass

@dataclass
class Cell:
    length: int
    upd: int

def build_map(s):
    d = dict()
    for i,c in enumerate(s):
        if c not in d: d[c] = []
        d[c].append(i)
    return d

def sparse_dp(x, y):
    if len(y) > len(x): x,y = y,x
    n = len(x) ; m = len(y)
    p = 0 ; l = 0
    mapEnds = build_map(y)
    row = [Cell(length=0,upd=-2) for _ in range(m)]
    for i in range(n):
        lstEnds = mapEnds.get(x[i],[])
        for j in reversed(lstEnds):
            row[j].upd = i
            if j-1 >= 0 and row[j-1].upd == i-1:
                row[j].length = row[j-1].length+1
            else:
                row[j].length = 1
            if row[j].length > l:
                l = row[j].length
                p = i
    return x[p-l+1 : p+1] if l > 0 else ""
