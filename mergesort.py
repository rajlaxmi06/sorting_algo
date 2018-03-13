def merge(list,l,m,r):
    n1=m-l+1
    n2=r-m
    list1=[]
    list2=[]
    for i in range(0,n1):
        list1.append(list[l+i])
    for j in range(0,n2):
        list2.append(list[m+1+j])
    k=l
    i=0
    j=0

    while(i<n1 and j<n2):
         if (list1[i] <= list2[j]):
             list[k]=list1[i]
             i=i+1
             k=k+1
         else:
             list[k]=list2[j]
             j=j+1
             k=k+1
    
    while(i<n1):
        list[k]=list1[i]
        i=i+1
        k=k+1
    while(j<n2):
        list[k]=list2[j]
        j=j+1
        k=k+1

def mergesort(list,l,r):
    if (l<r):
        m=int((l+(r-1))/2)
        mergesort(list,l,m)
        mergesort(list,m+1,r)

        merge(list,l,m,r)

def printarr(list,n):
    for i in range(0,n):
        print("%d" %list[i])

n=int(input("Enter the total numbers of elements"))
list=[0]*n
for i in range(n):
    m=int(input("Enter the elements"))
    list[i]=m
print("The order of elements before sorting:")
printarr(list,n)
mergesort(list,0,n-1)
print("The order of elements after sorting:")
printarr(list,n)