# Codigo para Python 3.7
# (en realidad solo importan los prints jeje)

'''
    compares adjacent items and exchanges those that are out of order
'''
def bubblesort(A):
    for n in range(len(A)-1,0,-1):
        for i in range(n):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
    return A

'''
    repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginnin
'''
def selectionsort(A):
    for i in range(len(A)):
        mini = min(A[i:])
        min_index = A[i:].index(mini)
        A[i + min_index] = A[i] 
        A[i] = mini   
    return A

'''
    1. Divide the unsorted list into n sublists, each containing one element
        (a list of one element is considered sorted).
    2. Repeatedly merge sublists to produce new sorted sublists until there
        is only one sublist remaining. This will be the sorted list.
'''
def mergesort(A):
    n = len(A)
    if n == 1:
        return A
    Ap = mergesort(A[:int(n/2)])
    App = mergesort(A[int(n/2):])
    return merge(Ap,App)

def merge(L,R):
    Re = []
    while len(L) > 0 and len(R) > 0:
        if L[0] < R[0]:
            Re.append(L.pop(0))
        else:
            Re.append(R.pop(0))
    if len(L) > 0:
        Re += L
    elif len(R) > 0:
        Re += R
    return Re

A = [1,0,-1,20,1,-20,-50]
print('Merge sort:')
print(A,mergesort(A))
print('Selection sort:')
print(A,selectionsort(A))
print('Bubble sort:')
print(A,bubblesort(A))
