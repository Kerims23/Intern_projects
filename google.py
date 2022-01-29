from posixpath import split


def jump(self, A):
    l = len(A)
    count = 0 
    pos = 0 
    for i in range(1,l):
        letter = split(A[i])
    while(pos < l-1):
        if(pos >= A[pos]):
            return -1
        elif(pos < A[pos]):
            count += 1
            pos = A[pos]
        return count 


self = 5
A = "5 5 5"
print(jump(self, A))
