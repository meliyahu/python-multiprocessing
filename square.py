import os
import time
from multiprocessing import Process, current_process, cpu_count


def square(num):
    result = num * num

    # Using os module to print out the process id
    # assigned to the call of this function assigned by the operating system
    # process_id = os.getpid()
    # print(f"Process ID: {process_id}")
    # OR
    # use the current_process function to get the name
    # of the Process object
    process_name = current_process().name
    print(f"Process name: {process_name}")
    print(f"The number {num} squares to {result}")
    time.sleep(3)
    print(f'Exiting')


if __name__ == '__main__':
    print(f"This computer has {cpu_count()} cores.")
    processes = []
    # numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    numbers = [1, 2, 3, 4]
    for number in numbers:
        process = Process(name='Square_Of ' + str(number), target=square, args=(number,))
        processes.append(process)

        # Processes are spawned by creating a Process object and
        # then calling its start() method
        process.start()
