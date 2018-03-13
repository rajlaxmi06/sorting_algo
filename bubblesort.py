def bubble_sort(list,n):
    for k in range(0,n):
        for i in range(0,n-k-1):
            if (list[i]>list[i+1]):
                 list[i], list[i+1] = list[i+1], list[i]
    print("The order of elements after sorting:")
    for i in range(0,n):
        print("%d" %list[i])

n=int(input("Enter the no. of elements you want to enter"))
list=['']*n
for i in range(0,n):
    m=int(input("Enter the list element"))
    list[i]=int(m)
print("The order of elements before sorting:")
for i in range(0,n):
    print("%d" %list[i])
bubble_sort(list,n)