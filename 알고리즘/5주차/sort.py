def cocktailShakerSort(a, n):
    d = True
    i=1
    k=n
    while (i<=k):
        if (d):
            for j in range(i, k):
                if (a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
            k-=1
            d = False
        else:
            for j in range(k, i, -1):
                if (a[j] < a[j-1]):
                    a[j],a[j-1]=a[j-1],a[j]
            i+=1
            d = True

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

def exchangeSort(a,n):
    i=1
    while(i<n):
        j=i+1
        while(j<=n):
            if(a[i]<a[j]):
                a[i],a[j] = a[j],a[i]
            j+=1
        i+=1
def mergeSort(a,b,l,r):
    if(r>l):
        m=(r+l)//2
        mergeSort(a,b,l,m)
        mergeSort(a,b,m+1,r)
        merge1(a,b,l,m,r)


def merge1(a,b,l,m,r):
    i=l
    j=m+1
    k=l
    while(i<=m and j<=r):
        if(a[i]<a[j]):
            b[k]=a[i]
            i=i+1
        else:
            b[k]=a[j]
            j=j+1
        k=k+1
    if i > m:
        for p in range(j, r+1):
            b[k] = a[p]
            k += 1
    else:            
        for p in range(i, m+1):
            b[k] = a[p]
            k += 1
    for p in range(l, r+1):
        a[p] = b[p]

def selectionSort(a, n):
    i=1
    while(i<n):
        j=i
        min_index=j
        while(j<=n):
            if(a[j]<a[min_index]):
                min_index=j
            j+=1
        a[i],a[min_index] = a[min_index],a[i]
        i+=1
    return a
def bubbleSort(a,n):
    i=n
    while(i>1):
        j=1
        while(j<i):
            if(a[j]>a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
            j+=1
        i-=1
    return a

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")