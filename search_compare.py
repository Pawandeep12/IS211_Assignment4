import time
import random

def get_me_random_list(n):

    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    time_taken = time.time() - start_time
    return found, time_taken


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1
    time_taken = time.time() - start_time
    return found, time_taken


def binary_search_iterative(a_list, item):
    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    time_taken = time.time() - start_time
    return found, time_taken


def binary_search_recursive(a_list, item):
    start_time = time.time()

    def recursive_search(a_list, item):
        if len(a_list) == 0:
            return False
        else:
            midpoint = len(a_list) // 2
            if a_list[midpoint] == item:
                return True
            else:
                if item < a_list[midpoint]:
                    return recursive_search(a_list[:midpoint], item)
                else:
                    return recursive_search(a_list[midpoint + 1:], item)

    result = recursive_search(a_list, item)
    time_taken = time.time() - start_time
    return result, time_taken


def run_search_algorithms(list_size):
    algorithms = {
        "Sequential Search": sequential_search,
        "Ordered Sequential Search": ordered_sequential_search,
        "Binary Search Iterative": binary_search_iterative,
        "Binary Search Recursive": binary_search_recursive
    }

    for name, algorithm in algorithms.items():
        total_time = 0
        for _ in range(100):
            random_list = get_me_random_list(list_size)
            if name != "Sequential Search":
                random_list = sorted(random_list)
            _, time_taken = algorithm(random_list, 99999999)
            total_time += time_taken
        avg_time = total_time / 100
        print(f"{name} took {avg_time:10.7f} seconds to run, on average for a list of {list_size} elements")


if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]
    for size in list_sizes:
        run_search_algorithms(size)

