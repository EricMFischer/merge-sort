'''
A file contains all of the 100,000 integers between 1 and 100,000 (inclusive)
in some order, with no integer repeated. Compute the number of inversions
in the file given, where the ith row of the file indicates the ith entry of
an array. Because of the large size of this array, you should implement a
fast divide-and-conquer algorithm.

[1,3,2] -> 1 inversion, arr[1] > arr[2]
Largest number of inversions in an n-element array = n(n-1) / 2

Algorithm for counting inversions:

sort_count_inv(arr, length)
if length = 1 # if length is 1, there are no inversions
  return 0
else
  a = sort_count_inv(1st half of arr, length/2)
  b = sort_count_inv(2nd half of arr, length/2)
  c = merge_count_split_inv(a,b)
return a + b + c;


Example:

To have step 3 merge_count_split_inv run in O(n), we can use step 3 from
merge sort, which uncovers split inversions as it merges.
To use step 3 from merge sort, however, we'll need our input arrays to
merge_count_split_inv to be sorted.

merge_count_split_inv
In merging elements to a sorted result, split inversions will always originate
from the 2nd array b, as it contains numbers that came "afterwards in the
array" relative to numbers in a.

So when an element of the second array b gets copied to output c, increment a
count by the number of elements remaining in the first array a.
'''


def merge_count_split_inv(a, b):
    output = []
    count = 0
    for a_index, a_value in enumerate(a):
        # while b has elements and a_value > b[0], pop off elements of b to
        # output, incrementing count each time for elements left in a
        while (b and a_value > b[0]):
            left_in_a = len(a) - a_index
            count += left_in_a
            output.append(b.pop(0))

        # if the a value is smaller or the while loop exited because b ran out,
        # copy element of a to output, and do not increment count
        output.append(a_value)

    # after we have gone through all elements of a, if there are elements
    # left in b, add them all to output
    output.extend(b)

    return output, count


def sort_count_inv(arr, length):
    if length == 1:
        return arr, 0
    else:
        half_len = length // 2
        first_half = arr[:half_len]
        second_half = arr[half_len:]
        a_output, a_count = sort_count_inv(first_half, len(first_half))
        b_output, b_count = sort_count_inv(second_half, len(second_half))
        c_output, c_count = merge_count_split_inv(a_output, b_output)
    return c_output, a_count + b_count + c_count


# arr = [8, 7, 6, 5, 4, 3, 2, 1]
f = open('array_inversions.txt', 'r')
arr = list(map(int, f.read().splitlines()))

result = sort_count_inv(arr, len(arr))
print('result: ', result)

f.close()
