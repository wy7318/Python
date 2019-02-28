#Slow sorting algorithm
# O(n^2)

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j]>A[j+1]:
                A[j], A[j+1]= A[j+1], A[j]
    return A
A=['b', 'a', 'c', 'f', 'g']
bubble_sort(A)
print(A)
