
'''
def cocktailShakerSort(a,n):
    d=True
    i=1
    k=n
    while(i<=k):
        if(d):
            j=i
            while(j<k):
                if(a[j]>a[j+1]):
                    a[j],a[j+1] = a[j+1],a[j]
                j+=1
            k-=1
            d=False
        else:
            j=k
            while(i<j):
                if(a[j]>a[j-1]):
                    a[j],a[j-1] = a[j-1],a[j]
                j-=1
            i+=1
            d=True
'''

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

N = 10
a = [-1, 6, 2, 8, 1, 3, 1, 5, 5, 10, 7]
print(a)
cocktailShakerSort(a, N)
print(a)