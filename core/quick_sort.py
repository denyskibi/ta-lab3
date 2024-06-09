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

    def sort_with_median(self, array: List[int], lo: int, hi: int) -> None:
        if lo < hi:
            # Step #1: Choosing the reference element as the median of three: the first, the last and the middle
            pivot_index = self._get_median_of_three_elements(array, lo, hi)
            array[pivot_index], array[hi] = array[hi], array[pivot_index]

            # Step #2: Performing the separation of array
            p = self._split_array_into_parts(array, lo, hi)

            # Step #3: Recursive sorting array parts
            self.sort_with_median(array, lo, p - 1)
            self.sort_with_median(array, p + 1, hi)

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

    @staticmethod
    def _get_median_of_three_elements(array: List[int], lo: int, hi: int) -> int:
        median = (lo + hi) // 2

        if array[hi] < array[lo]:
            array[lo], array[hi] = array[hi], array[lo]

        if array[median] < array[lo]:
            array[median], array[lo] = array[lo], array[median]

        if array[hi] < array[median]:
            array[hi], array[median] = array[median], array[hi]

        return median

