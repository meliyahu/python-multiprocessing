from multiprocessing import Pool
import time
import os


def f(n):
    sum = 0
    for i in range(1000):
        sum += i * i

    return sum


if __name__ == "__main__":
    t1 = time.time()
    # p = Pool(os.cpu_count())
    p = Pool()
    result = p.map(f, range(100000))
    p.close()
    p.join()
    sum = 0
    for item in result:
        sum += item

    print(f'Parallel Total is: {sum}')

    print(f"Pool took: { time.time() - t1}")

    result = []
    t2 = time.time()

    for i in range(100000):
        result.append(f(i))
    sum = 0
    for item in result:
        sum += item

    print(f'Serial total is: {sum}')

    print(f"Serial took: { time.time() - t2}")

