def partition(list,low,high):
    i=(low -1)
    pivot=list[high]

    for j in range(low,high):
        if(list[j]<=pivot):
            i=i+1
            list[i],list[j]=list[j],list[i]
    
    list[i+1],list[high] = list[high],list[i+1]
    return (i+1)

def quicksort(list,low,high):
    if(low < high):
        p=partition(list,low,high)
        quicksort(list,low,p-1)
        quicksort(list,p+1,high)

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
quicksort(list,0,n-1)
print("The order of elements after sorting:")
printarr(list,n)