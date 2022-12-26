import pathlib
from pathlib import Path


def names_gen(name_file: str, letter: str):
    path_file = Path(pathlib.Path.cwd(), "HW13", name_file)
    with open(path_file, mode="r") as file:
        for file_data in file:
            if file_data[0] == letter:
                yield file_data
    return None


asf = names_gen("unsorted_names.txt", "S")
print(next(asf))
print(next(asf))
