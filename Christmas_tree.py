def triangle_shape(n):
    for i in range(n):
        for o in range(n-i):
            print(' ', end=' ')
        for p in range(2*i+1):
