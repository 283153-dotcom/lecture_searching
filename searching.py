import time
from curses.ascii import isxdigit
from operator import index
from pathlib import Path
import json
from generators import unordered_sequence, ordered_sequence
import matplotlib.pyplot as plt



def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    with open (file_path, "r") as json_file:
        data_json=json.load(json_file)
        if field in data_json.keys():
            return data_json[field]
        else:
            return None


def linear_search(sequence, searched_number):
    count=0
    positions=[]

    for i, item in enumerate(sequence):
        if item==searched_number:
            count +=1
            positions.append(i)

    searched_dictionary={"count":count, "positions":positions}
    return searched_dictionary


def binary_search(searched_list, searched_number):
    lowest=0
    highest=len(searched_list)-1

    while lowest<=highest:
        middle=(lowest+highest)//2
        if searched_list[middle]==searched_number:
            return middle
        elif searched_list[middle]<searched_number:
            lowest=middle+1
        else:
            highest=middle-1
    return None

def test_complexity(list_of_n):
    time_linear=[]
    time_binary=[]
    number=21
    for n in list_of_n:
        unordered_data=unordered_sequence(n)
        ordered_data=ordered_sequence(n)
        duration_linear=0
        duration_binary=0
        repetitions=100
        for measurements in range(repetitions):
            start_time_linear = time.perf_counter()
            found_number = linear_search(unordered_data, number)
            end_time_linear = time.perf_counter()
            duration_linear=end_time_linear-start_time_linear

            start_time_binary=time.perf_counter()
            found_bin=binary_search(ordered_data, number)
            end_time_binary=time.perf_counter()
            duration_binary=end_time_binary-start_time_binary
        time_linear.append(duration_linear/repetitions)
        time_binary.append(duration_binary/repetitions)

    print(time_linear)
    print(time_binary)
    plt.plot(list_of_n, time_linear)
    plt.plot(list_of_n, time_binary)

    plt.xlabel("Velikost vstupu.")
    plt.ylabel("Čas [s]")
    plt.title("Porovnání vyhledávacích algoritmů")
    plt.show

def pattern_search(sequency, pattern):
    indices={}

    return indices

def main():
    my_data=read_data("sequential.json", "ordered_numbers")
    print(my_data)
    number = 21
    duration=0
    repetitions=100
    for measurements in range(100):
        start_time = time.perf_counter()
        found_number=linear_search(my_data, number)
        end_time= time.perf_counter()
        duration +=end_time-start_time
    print(found_number)
    print(duration/repetitions)
    searched_dictionary=linear_search(my_data, 5)
    print(searched_dictionary)
    middle=binary_search(my_data, number)
    print(middle)

    sizes = [100, 500, 1000, 5000, 10000]
    test_complexity(sizes)

if __name__ == "__main__":
    main()
