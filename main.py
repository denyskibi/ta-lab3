# Standard Libraries
from typing import List
import sys

# Custom Modules
from core.quick_sort import QuickSort
from utils import file_utils


# Create necessary class objects
quick_sort = QuickSort()


def task1(loaded_num_list: List[int]) -> None:
    loaded_numbers_count = len(loaded_num_list)

    # Step #1.1: Call quick sort function
    quick_sort.sort(array=loaded_num_list, lo=0, hi=loaded_numbers_count - 1)

    # Step #1.2: Get & print the total comparisons number
    print(
        f"[INFO] Task #1 - The total number of comparisons using quick sort method: "
        f"{quick_sort.get_total_comparisons()}"
    )

    # Step #1.3: Reset the total comparisons so not to affect the result of the next task
    quick_sort.reset_total_comparisons()


def task2(loaded_num_list: List[int]) -> None:
    loaded_numbers_count = len(loaded_num_list)

    # Step #2.1: Call quick sorting function (but with swapping elements)
    quick_sort.sort_with_swapping_elements(array=loaded_num_list, lo=0, hi=loaded_numbers_count - 1)

    # Step #2.2: Get & print the total comparisons number
    print(
        f"[INFO] Task #2 - The total number of comparisons using quick sort method with swapping first and second "
        f"elements: {quick_sort.get_total_comparisons()}"
    )


def stop():
    sys.exit(1)


def main():
    try:
        # Load list from file
        loaded_num_list = file_utils.load_list_from_txt_file(file_path="files/input_10000_numbers.txt")

        task2(loaded_num_list)
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()


if __name__ == '__main__':
    main()
