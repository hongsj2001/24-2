'''
def makeRun(a,n):
    i=1
    r=[]
    while(i<n):
        l=[]
        k=i
        l.append(a[k])
        while(k<n):
            if(a[k]<=a[k+1]):
                l.append(a[k+1])
            else:
                break
            k+=1
        i=k
        r.append(l)
    return r
'''

def makeRun(a,n):
    i=1
    r=[]
    while(i<=n):
        m=[]
        m.append(a[i])
        while(i+1<n) and (a[i]<=a[i+1]):
            m.append(a[i+1])
            i+=1
        r.append(m)
        i+=1
    return r

def merge(a,b):
    i, j, n1, n2 = 0, 0, len(a), len(b)
    l = []
    while i < n1 and j < n2:
        if (a[i] < b[j]):
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1
    if (i == n1):
        for k in range(j, n2):
            l.append(b[k])
    else:
        for k in range(i, n1):
            l.append(a[k])
    return l


def naturalMerge(a, n):
    r = makeRun(a, n)
    m = len(r)
    while m > 1:
        i = 0
        p = []
        while (i < m):
            if (i == m-1):
                p.append(r[i])
            else:
                p.append(merge(r[i], r[i+1]))
            i += 2
        r = []
        m = len(p)
        for j in range(m):
            r.append(p[j])
    for i in range(n):
        a[i+1] = r[0][i]
    return a

a=[0, 6, 7, 8, 3, 4, 1, 5, 9, 10, 2]
print(a)
print(makeRun(a,10))
print(naturalMerge(a, 10))