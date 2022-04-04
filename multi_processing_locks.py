from multiprocessing import cpu_count, Process, Lock, Value, get_logger, log_to_stderr
import time
import logging


def add_500_no_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()


def sub_500_no_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()


if __name__ == '__main__':

    pool_size = cpu_count() * 2
    print(f"CPUs: {pool_size}")

    total = Value('i', 500)
    lock = Lock()

    log_to_stderr()
    logger = get_logger()
    logger.setLevel(logging.INFO)

    add_process = Process(name='ADD', target=add_500_no_lock, args=(total, lock))
    sub_process = Process(name='SUB', target=sub_500_no_lock, args=(total, lock))

    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()
    print(total.value)
