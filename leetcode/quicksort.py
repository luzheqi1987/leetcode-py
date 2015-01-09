'''
Created on 2015.1.9

@author: Administrator
'''

def quicksort(numbers):
    length = len(numbers)
    partition1(numbers, 0, length - 1)
    return numbers
    
def partition(numbers, start, end):
    if start >= end or start < 0 or end >= len(numbers):
        return 
    mid = (start + end) / 2
    tmp = numbers[end]
    numbers[end] = numbers[mid]
    numbers[mid] = tmp
    i = start
    j = end - 1
    index = end
    while i < j:
        while i < j and numbers[i] < numbers[index]:
            i = i + 1
        
        while i < j and numbers[j] > numbers[index]:
            j = j - 1
            
        if i < j:
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp  
    if numbers[i] > numbers[index]:    
        tmp = numbers[i]
        numbers[i] = numbers[index]
        numbers[index] = tmp    
    
    partition(numbers, start, i - 1)
    partition(numbers, j + 1, end)

def partition1(numbers, start, end):
    if start >= end or start < 0 or end >= len(numbers):
        return 
    mid = (start + end) / 2
    tmp = numbers[end]
    numbers[end] = numbers[mid]
    numbers[mid] = tmp
    i = start  
    
    while i < end and numbers[i] < numbers[end]:
        i += 1
         
    j = i    
    while j < end:
        if numbers[j] > numbers[end]:
            j += 1
        else:
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
            i += 1
            j += 1
        
    if numbers[i] > numbers[end]:    
        tmp = numbers[i]
        numbers[i] = numbers[end]
        numbers[end] = tmp    
    
    partition(numbers, start, i - 1)
    partition(numbers, j + 1, end)
    
    
#######################################################################
def partition2(numbers, length, start, end):
    if not numbers or start < 0 or end >= length or length <= 0:
        raise RuntimeError('Invalid Paramaters')
        return 
    mid = (start + end) / 2
    swap(numbers, mid, end)
    
    i = start
    small = start - 1  
    for i in range(start, end):
        if numbers[i] < numbers[end]:
            small += 1
            if small != i:
                swap(numbers, small, i)
    
    small += 1
    swap(numbers, small, end)
    
    return small

def swap(numbers, start, end):
    if start < 0 or end >= len(numbers):
        raise RuntimeError('Invalid Parameters')
    tmp = numbers[start]
    numbers[start] = numbers[end]
    numbers[end] = tmp

def quick_sort(numbers, length, start, end):
    if start == end:
        return
    
    index = partition2(numbers, length, start, end)
    if index > start:
        quick_sort(numbers, length, start, index - 1)
    if index < end:
        quick_sort(numbers, length, index + 1, end)
        
############################################################################  

def find_k(numbers, k):
    if not numbers or k - 1 < 0 or k - 1 > len(numbers):
        raise RuntimeError('Invalid Parameters')
    k = k - 1
    start = 0
    end = len(numbers) - 1
    index = partition2(numbers, len(numbers), start, end)
    while index != k:
        if index > k:
            end = index - 1
            index = partition2(numbers, len(numbers), start, end)
        elif index < k:
            start = index + 1
            index = partition2(numbers, len(numbers), start, end)
    return numbers[k]

  
    
if __name__ == '__main__':
    numbers = [2, 3, 1, 4, 6, 3, 7, 5, 9, 100, 23, 64, 36, 85, 34, 27, 8, 2]
    # quicksort(numbers)
    quick_sort(numbers, len(numbers), 0, len(numbers) - 1)
    print numbers
    print find_k(numbers, 15)
