def time_taker(_N):
    L = []
    for i in range(_N):
        l = [float(f) for f in range(_N)]
        L += l
    return len(L)
