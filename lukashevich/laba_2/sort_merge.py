text_sort = 'sdgdrgdfgd'

def mergeSort(text_sort):
    if len(text_sort) <= 1:
        return text_sort

    mid = (len(text_sort) - 1) // 2
    left = mergeSort(text_sort[:mid + 1])
    right = mergeSort(text_sort[mid + 1:])
    result_sort = merge(left, right)
    return result_sort
def merge(left, right):
    result = []
    i = j = 0

    while (i <= len(left) - 1 and j <= len(right)-1):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i>len(left)-1:
        while j <= len(right)-1:
            result.append(right[j])
            j += 1

    else:
        while i <= len(left) - 1:
            result.append(left[i])
            i += 1

    return ''.join(result)


result_sort = mergeSort(text_sort)
print(result_sort)

def BinarySearch(text, val):
    left = 0
    right = len(text)-1
    index = -1
    while (left <= right) and (index == -1):
        mid = (left + right) // 2
        if text[mid] == val:
            index = mid
        else:
            if val < text[mid]:
                right = mid - 1
            else:
                left = mid + 1
    if index == -1:
        return False
    else:
        return True

print(BinarySearch(result_sort, "k"))

