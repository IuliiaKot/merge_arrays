def mergearray(a, b):
    idx_a = 0
    idx_b = 0
    while (idx_b < len(b)):
        print idx_a
        if (a[idx_a] > b[idx_b] and (a[idx_a] != None)):
            a.insert(idx_a, b[idx_b])
            a.pop()
            idx_b += 1
        elif (a[idx_a] == None):
            a.insert(idx_a, b[idx_b])
            a.pop()
            break
        else:
            idx_a += 1
    print a
    
a = [1, 14, 29, None, None, None, None, None]
b = [2, 10, 35]
mergearray(a, b)
