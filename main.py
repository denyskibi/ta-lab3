# Standard Libraries
import sys

# Custom Modules
from core.quick_sort import QuickSort
from utils import file_utils


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    quick_sort = QuickSort()

    try:
        # Step #1: Load list from file
        loaded_num_list = file_utils.load_list_from_txt_file(file_path="files/input_10000_numbers.txt")

        # Step #2: Call quick sort function
        loaded_numbers_count = len(loaded_num_list)
        quick_sort.sort(array=loaded_num_list, lo=0, hi=loaded_numbers_count - 1)

        # Step #3: Get & print the total comparisons number
        total_comparisons = quick_sort.get_total_comparisons()
        print(f"[INFO] The total number of compilations using quick sort method: {total_comparisons}")
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()


if __name__ == '__main__':
    main()
