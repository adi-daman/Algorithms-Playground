#   Each c_n represents the line in the function block at acts as a constant cost 
#   n = length of elements in list
#   Recursive call: n depth
#   While loop: Size of sorted list: 0, 1, 2, ..., m - 2, m - 1
#       When already sorted, inner loop is not entered: c_22
#       Reversed order, so whole list needs to be shifted: Length of List sorted partition (m - 1)
#   Therefore, at   best case   :   Recursive call, n
#                   worst case  :   Recursive call, n and whole list to be shifted at each level is n - 1 times
#                                   Therefore (n(n - 1))/2 = 1/2 * (n^2 - n) 
#
#   f(n) = (n(n -1))/2 + ... in set Big-oh(n^2)     iff n >= 2 as when 0 <= 1/2 - 1/n <= c2  (c2 = 1/2)
#   f(n) = (n(n -1))/2 + ... in set Big-Omega(n^2)  iff n >= 2 when 0 <= c1 <= 1/2 - 1/n     (c1 = 0)               TODO - verify
#   f(n) = (n(n -1))/2 + ... in set Big-Theta(n^2)  iff n >= 2 when c1 <= 1/2 - 1/n <= c2    (c1 = 0 and c2 = 1/2)  TODO - verify
 
def recursive_insertion_sort(List):
    if len(List) == 0:
        return List
    else:
        Tail = List[-1] # The end item
        List = recursive_insertion_sort(List[0:len(List) - 1]) + [Tail] # Sorted partition, unsorted partition
        Index = len(List) - 2 # Point to the end of the sorted portion of the list
        while(Index >= 0 and List[Index] > Tail):
            List[Index + 1] = List[Index]
            Index = Index - 1
        List[Index + 1] = Tail
        return List

#print (recursive_insertion_sort([3,1,2,1]))
#print (recursive_insertion_sort([1,2,3,4]))