# Standard Libraries
from typing import List


class QuickSort:
    def __init__(self):
        self._total_comparisons: int = 0

    def sort(self, array: List[int], lo: int, hi: int) -> None:
        if lo < hi:
            # Performing the separation procedure and getting the position of the reference element and
            # the number of comparisons
            p = self._split_array_into_parts(array, lo, hi)

            self.sort(array, lo, p - 1)  # recursive sorting the left part of the array
            self.sort(array, p + 1, hi)  # recursive sorting the right part of the array

    def sort_with_swapping_elements(self, array: List[int], lo: int, hi: int) -> None:
        if lo < hi:
            # Swap the first and last elements before start sorting
            array[lo], array[hi] = array[hi], array[lo]

            # Performing the separation procedure and getting the position of the reference element and
            # the number of comparisons
            p = self._split_array_into_parts(array, lo, hi)

            self.sort_with_swapping_elements(array, lo, p - 1)  # recursive sorting the left part of the array
            self.sort_with_swapping_elements(array, p + 1, hi)  # recursive sorting the right part of the array

    def get_total_comparisons(self) -> int:
        return self._total_comparisons

    def reset_total_comparisons(self) -> None:
        self._total_comparisons = 0

    def _split_array_into_parts(self, array: List[int], lo: int, hi: int) -> int:
        i = lo - 1  # start from minus one index to calculate swaps ??
        pivot = array[hi]  # setting the last element as a reference

        # Selection of elements and their comparison with the reference element
        for j in range(lo, hi):
            self._total_comparisons += 1
            if array[j] <= pivot:  # if the current is less than or equal to the reference
                i += 1
                array[i], array[j] = array[j], array[i]  # swap elements

        # Placing a reference element between smaller and larger ones
        array[i + 1], array[hi] = array[hi], array[i + 1]

        return i + 1
