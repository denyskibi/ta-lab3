# Standard Libraries
from typing import List


def load_list_from_txt_file(file_path: str) -> List[int]:
    loaded_num_list = []

    with open(file_path, 'r') as file_content:
        for line in file_content:
            number_el = line.strip()
            number = int(number_el)

            loaded_num_list.append(number)

    return loaded_num_list
