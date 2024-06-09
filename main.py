# Standard Libraries
import sys

# Custom Modules
from utils import file_utils


def stop():
    sys.exit(1)


def main():
    try:
        # Step #1: Load list from file
        loaded_num_list = file_utils.load_list_from_txt_file(file_path="files/input_10000_numbers.txt")

        ...
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed due to error: {e}")
        stop()


if __name__ == '__main__':
    main()
