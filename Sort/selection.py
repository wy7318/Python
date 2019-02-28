# nested loop
# Good for small date(<10000)
# O(n^2)

def selection_sort(A):
    for i in range(0, len(A)-1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = A[j]
        if minIndex !=i:
            A[i], A[minIndex] = A[minIndex], A[i]

A=[3,2,5,4,1]
selection_sort(A)
print(A)
