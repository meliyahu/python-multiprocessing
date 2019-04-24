from multiprocessing import Process, Lock, Value
import time


def add_500_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total += 5
    return total


def sub_500_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total -= 5
    return total


if __name__ == '__main__':
    total = 500
    print(total)
    total = add_500_no_mp(total)
    print(total)
    total = sub_500_no_mp(total)
    print(total)
