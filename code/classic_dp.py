def classic_dp(x, y):
	if len(y) > len(x): x,y = y,x
	n = len(x) ; m = len(y)
	p = 0 ; l = 0
	row = [0 for _ in range(m)]
	for i in range(n):
		for j in range(m-1, -1, -1): # almost "classic"...
			if x[i] == y[j]:
			  row[j] = row[j-1]+1 if j > 0 else 1
			else:
				row[j] = 0
			if row[j] > l:
				p = i
				l = row[j]
	return x[p-l+1 : p+1] if l > 0 else ""
