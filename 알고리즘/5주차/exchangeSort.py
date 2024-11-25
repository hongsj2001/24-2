def exchangeSort(a,n):
    i=1
    while(i<n):
        j=i+1
        while(j<=n):
            if(a[i]<a[j]):
                a[i],a[j] = a[j],a[i]
            j+=1
        i+=1

N = 10
a = [-1, 6, 2, 8, 1, 3, 1, 5, 5, 10, 7]
print(a)
exchangeSort(a, N)
print(a)