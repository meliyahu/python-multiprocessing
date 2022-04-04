import time
from datetime import datetime, timedelta
import os
from multiprocessing import Pool


def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s


def sum_square_with_mp(numbers):
    """
    Demonstrates multi-processing
    :param numbers:
    :return:
    """
    start_time = time.time()
    # p = Pool(os.cpu_count())  # Distribute according to number of cores
    p = Pool()  # Distribute according to number of cores
    result = p.map(sum_square, numbers)
    p.close()
    p.join()
    end_time = time.time() - start_time
    d = get_formatted_time(end_time)
    # print(f"Processing {len(numbers)} numbers took {d.day - 1} days:{d.hour} hours {d.minute} minute {d.second} seconds WITH multiprocessing")
    print(f"Processing {len(numbers)} numbers took {d.day - 1} days {d.hour} hours {d.minute} minute {d.second} seconds {d.microsecond} microseconds")


def sum_square_without_mp(numbers):
    """
    Demonstrate without multi-processing
    :param numbers:
    :return:
    """
    start_time = time.time()
    result = []
    for number in numbers:
        result.append(sum_square(number))

    end_time = time.time() - start_time
    d = get_formatted_time(end_time)

    # print(f"Processing {len(numbers)} numbers took {d.day-1} days:{d.hour} hours {d.minute} minute {d.second} seconds WITHOUT multiprocessing")

    print(f"Processing {len(numbers)} numbers took {d.day-1} days {d.hour} hours {d.minute} minute {d.second} seconds {d.microsecond} microseconds")


def get_formatted_time(seconds):
    sec = timedelta(seconds=int(seconds))
    d = datetime(1, 1, 1) + sec
    return d


if __name__ == "__main__":
    numbers = range(10000)
    sum_square_with_mp(numbers)
    sum_square_without_mp(numbers)
