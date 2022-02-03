from array import array

def merge_sort(a: array) -> array:
    if len(a) == 1:
        return a
    
    middle_index = len(a)//2
    first_half = merge_sort(a[:middle_index])
    second_half = merge_sort(a[middle_index:])
    
    return merge(first_half, second_half)

def merge(a: array,b: array) -> array:
    c = [None] * (len(a)+len(b))
    i = 0
    j = 0
    
    for k in range(len(c)):
        
        if(i+1 > len(a) and j+1 > len(b)):
            return c
        
        if i+1 > len(a):
            c[k] = b[j]
            j += 1
        elif j+1 > len(b):
            c[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            c[k] = a[i]
            i += 1
        elif b[j] < a[i]:
            c[k] = b[j]
            j += 1
    
    return c

print("*** Merge Sort ***")
unsorted_list = [31111,5,433,64,1,22,7]
print(f"Unsorted Input: {unsorted_list}")
result = merge_sort(unsorted_list)
print(f"Sorted Output: {result}")
