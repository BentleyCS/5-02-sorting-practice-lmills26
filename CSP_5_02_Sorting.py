import random


def bubbleSort(items:list):
    swaps = 0
    comparisons = 0
    while True:
        swapsInLoop = 0
        for i in range(0, len(items)-1):
            comparisons += 1
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swaps +=1
                swapsInLoop +=1
        if swapsInLoop == 0:
            break
    return items, swaps, comparisons

def insertionSort(items: list):
    swaps = 0
    comparisons = 0
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]
                swaps += 1
                j -= 1
            else:
                break
        items[j + 1] = key
    return items, swaps, comparisons

def selectionSort(items : list):
    swaps = 0
    comparisons = 0
    for i in range(0, len(items)-1):
        nextSmallestpos = i
        for j in range(i+1, len(items)):
            comparisons +=1
            if items[j] < items[nextSmallestpos]:
                nextSmallestpos = j

        items[i], items[nextSmallestpos] = items[nextSmallestpos], items[i]
        swaps += 1
    return items, swaps, comparisons


y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
