import matplotlib.pyplot as plt
import random as rnd
import time
import os

plt.rcParams["figure.figsize"] = (10,6)

def merge_sort(lst, n, x, b):
    def merge(a, l, m, u):
        i = l
        j = m+1
        k = l
        while i <= m and j <= u:
            if a[i] <= a[j]:
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1
            k += 1
        if i > m:
            while j <= u:
                b[k] = a[j]
                j += 1
                k += 1
        else:
            while i <= m:
                b[k] = a[i]
                i += 1
                k += 1

        for k in range(l, u+1):
            a[k] = b[k]

    def MS(a, l, u):
        if l < u:
            m = (l+u) // 2
            MS(a, l, m)
            MS(a, m+1, u)
            plt.xlabel('No. of elements')
            plt.ylabel('Range of elements')
            plt.text(l, a[l], a[l])
            plt.bar(x, a)
            plt.bar(x[l:m+1], a[l:m+1], color='red')
            plt.bar(x[m+1:u+1], a[m+1:u+1], color='green')
            plt.pause(0.01)
            plt.clf()
            merge(a, l, m, u)
            plt.xlabel('No. of elements')
            plt.ylabel('Range of elements')
            plt.text(l, a[l], a[l])
            plt.bar(x, a)
            plt.pause(0.000000000001)
            plt.clf()

    n = int(input("Enter the number of elements: "))
    b = [0] * n
    x = []
    lst = []
    if input_type == 1:
            for i in range(n):
                lst.append(int(input(f'Element {i+1}: ')))
                x.append(i+1)
    else:
            lst = rnd.sample(range(1, n * 10 + 1), n)
            rnd.shuffle(lst)
            for i in range(n):
                x.append(i+1)
    print("Before sorting:", lst)
    start = time.time()
    MS(lst, 0, n-1)
    end = time.time()
    merge_sort_time_complexity = end-start
    print("After sorting:", lst)
    plt.xlabel('No. of elements')
    plt.ylabel('Range of elements')
    plt.text(0.3, 100, merge_sort_time_complexity)
    plt.bar(x, lst)
plt.show()


merge_sort_time_complexity = 0

print('\nAlgorithm to visualize:')
print('Merge Sort')
print('How do you want to generate your input?')
print('1. Manual Entry\n2. Randomly generated array')
input_type = int(input('Choice:'))
    
merge_sort([], 0, [], [])

plt.pause(2.5)
plt.close()
