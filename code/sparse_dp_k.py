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

def identify(x, y):
    n = len(x) ; m = len(y)
    p = -1 ; l = -1
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
    return (p,l)

def build_sequence(s, k):
    return [s[i:i+k] for i in range(len(s)-k+1)]

def linear_search(x, y, t):
    for l in range(t, 0, -1):
        h = set(b for b in build_sequence(x, l))
        for b in build_sequence(y, l):
            if b in h:
                return b
    return ""

def sparse_dp_k(x, y, k):
    if len(x) == 0 or len(y) == 0:
        return ""
    if len(y) > len(x):
            x,y = y,x
    xk = build_sequence(x, k)
    yk = build_sequence(y, k)
    ik, lk = identify(xk, yk)
    if ik != -1 and lk != -1:
        i = ik + k - 1
        l = lk + k - 1
        return x[i-l+1 : i+1]
    return linear_search(y, x, k-1)
