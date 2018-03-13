def insertionsort(list,n):
    for i in range (1,n):
        key=list[i]
        j=i-1
        while (j>=0 and key < list[j]):
            list[j+1]=list[j]
            j-=1
        list[j+1]=key

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
insertionsort(list,n)
print("The order of elements after sorting:")
printarr(list,n)