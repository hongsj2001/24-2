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

def insertSort(a,n):
    i=2
    while(i<=n):
        k=a[i]
        j=i
        while(a[j-1]>k):
            a[j]=a[j-1]
            j=j-1
        a[j]=k
        i=i+1
    return a

def shellSort(a,n):
    h=1
    while(h<n):
        h=h*3+1
    while(h>0):
        i=1
        while(i+h<=n):
            k=a[i+h]
            j=i+h
            while(a[j-h]>k and j-h>0):
                a[j] = a[j-h]
                j=j-h
            a[j]=k
            i=i+1
        h=int(h/3)
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
