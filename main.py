# Standard Libraries
from typing import List
import sys
import traceback

# Custom Modules
from core.quick_sort import QuickSort
from utils import file_utils


# Create necessary class objects
quick_sort = QuickSort()


def task1(loaded_num_list: List[int]) -> None:
    loaded_numbers_count = len(loaded_num_list)

    # Step #1.1: Reset the total comparisons so not to affect the result of the next task
    quick_sort.reset_total_comparisons()

    # Step #1.2: Call quick sort function
    quick_sort.sort(array=loaded_num_list, lo=0, hi=loaded_numbers_count - 1)

    # Step #1.3: Get & print the total comparisons number
    print(
        f"[INFO] Task #1 - The total number of comparisons using quick sort method: "
        f"{quick_sort.get_total_comparisons()}"
    )


def task2(loaded_num_list: List[int]) -> None:
    loaded_numbers_count = len(loaded_num_list)

    # Step #2.1: Reset the total comparisons so not to affect the result of the next task
    quick_sort.reset_total_comparisons()

    # Step #2.2: Call quick sorting method (but with swapping elements)
    quick_sort.sort_with_swapping_elements(array=loaded_num_list, lo=0, hi=loaded_numbers_count - 1)

    # Step #2.3: Get & print the total comparisons number through swapping elements method
    print(
        f"[INFO] Task #2 - The total number of comparisons using quick sort method with swapping first and second "
        f"elements: {quick_sort.get_total_comparisons()}"
    )


def task3(loaded_num_list: List[int]) -> None:
    loaded_numbers_count = len(loaded_num_list)

    # Step #3.1: Reset the total comparisons so not to affect the result of the next task
    quick_sort.reset_total_comparisons()

    # Step #3.2: Call quick sorting method (with median)
    quick_sort.sort_with_median(array=loaded_num_list, lo=0, hi=loaded_numbers_count - 1)

    # Step #3.3: Get & print the total comparisons number through method with median
    print(
        f"[INFO] Task #3 - The total number of comparisons using sorting though median: "
        f"{quick_sort.get_total_comparisons()}"
    )


def stop():
    sys.exit(1)


def main():
    try:
        # Load list from file
        loaded_num_list = file_utils.load_list_from_txt_file(file_path="files/input_10000_numbers.txt")

        # Call the function with a necessary task (to avoid depth recursion error)
        task3(loaded_num_list)
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
