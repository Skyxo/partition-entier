import copy

def partitions_sans_successeurs(n):
    a=n*[1]
    L=[a]
    k=n
    while k>1:
        y=a[k-1]-1
        x=a[k-2]+1
        q,r=divmod(y,x)
        a=a[:k-2]+q*[x]+[x+r]
        k+=q-1
        L+=[a]
    return L

m=3
n=5

def add_parts(list_, m):
    
    flist_ = []

    i = 0
    while i < len(list_) :
        
        if len(list_[i]) <= m:
            list_[i]+=[0]*(m-len(list_[i]))
            flist_.append(list_[i])

        i+=1

    return flist_

def homog(list_, m):
    flist_ = []

    for i in range(len(list_)):
        for o in range(m*(m-1)):
            
            list_[i][-o], list_[i][-o+1] = list_[i][-o+1], list_[i][-o]
            flist_.append(list_[i])

    return flist_


print(homog(add_parts(partitions_sans_successeurs(n), m), m))