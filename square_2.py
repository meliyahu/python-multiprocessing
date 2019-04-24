import os
import time
from multiprocessing import Process, current_process, cpu_count


def square(numbers):
    """
    This function squares the numbers in the list
    :param numbers:
    :return:
    """
    for number in numbers:
        time.sleep(0.5)  # 0.5 secs
        result = number * number
        print(f"The number {number} squares to {result}")


if __name__ == '__main__':
    # print(f"This computer has {cpu_count()} cores.")
    processes = []
    numbers = range(100)
    for i in range(50):
        process = Process(target=square, args=(numbers,))
        processes.append(process)

        # Processes are spawned by creating a Process object and
        # then calling its start() method
        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing completed!")
