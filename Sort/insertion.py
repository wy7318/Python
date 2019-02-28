# nested loop
# Good for small date
# O(n^2)

def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i-1, 0, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
