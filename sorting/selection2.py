a = [1,4,4,5,4,3,5,4,4]

def selection_sort(a):
    for i in range(len(a)):
        m = i
        for j in range(i,len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a

# selection_sort(a)

def insertion_sort(a):
    for i, v in enumerate(a):
        while i > 0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i -=1
    return a

# insertion_sort(a)

def bubble_sort(l):
    n = len(l)
    for i in reversed(range(n)):
        s = False
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                s = True
        if not s:
            return l
    return l

bubble_sort(a)

1,2,