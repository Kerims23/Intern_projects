#making the triangle shape for tree
def triangle_shape(n):
    for i in range(n):
        for o in range(n-i):
            print(' ', end=' ')
        for p in range(2*i+1):
            print ('*', end=' ')
        print()

#making pole shape 
def pole_shape(n):
    for i in range(n):
        for o in range(n-1):
            print(' ', end=' ')
        print('* * *')

#call function
row = int(input("Enter number of rows: "))

triangle_shape(row)
triangle_shape(row)
pole_shape(row)