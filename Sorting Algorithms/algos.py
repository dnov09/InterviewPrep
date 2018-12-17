# Sorting Algorithms
#%%
def selection_sort(lst):
    # find the minimum in the unsorted subarray
    for i in range(len(lst)):
        min_idx = i
        # checks the next number and performs the check
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        # Swap the new minimum with the current minimum
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print("Selection sort: {}".format(lst))

def insertion_sort(lst):
    # Swapping method
    # for i in range(1, len(lst)):
    #     for j in range(i-1, -1, -1):
    #         if lst[j] > lst[j+1]:
    #             lst[j], lst[j+1] =  lst[j+1], lst[j]
    #         else:
    #             break

    # Shifting method -> 2x faster because no swapping
    for i in range(1, len(lst)):
        curr_num = lst[i]
        for j in range(i-1, -1, -1):
            if lst[j] > curr_num:
                lst[j+1] = lst[j]
            else:
                lst[j+1] = curr_num
                break
    
    print("Insertion sort: {}".format(lst))


def quicksort(lst):
    pass

def mergesort(lst):
    pass

def heapsort(lst):
    pass

def create_array(size=10, max=100):
    from random import randint
    return [randint(0, max) for _ in range(size)]
# --------------------------------------------------------------- #
#%% 
selection_sort(create_array())
insertion_sort(create_array())
# quicksort(create_array())
# mergesort(create_array())
# heapsort(create_array())
