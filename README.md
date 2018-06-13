## Synopsis
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

Gauss's trick involves computing the middle term *ad + bc* not by finding the terms invidividually, but by finding the product of *(a + b)(c + d)*, which equals *ac + ad + bc + bd*, and then subtracting *ac* and *bd*, which we have to solve for separately anyways. The steps for Karatsuba's Multiplication algorithm can be summarized as follows:

* Recursively compute ac
* Recursively compute bd
* Recursively compute *(a + b)(c + d) = ac + ad + bc + bd*

## Motivation

The motivation for writing this algorithm is to use merge sort and achieve a linear O(n) time complexity for the problem of finding the number of inversions in an array.

## Acknowledgements

This algorithm is part of the Stanford University Algorithms 4-Course Specialization on Coursera, instructed by Tim Roughgarden.
