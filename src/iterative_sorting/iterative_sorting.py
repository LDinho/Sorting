# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp_smallest_value = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_smallest_value
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swap occurs here if line 25 is true
                placeholder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = placeholder
                is_swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
