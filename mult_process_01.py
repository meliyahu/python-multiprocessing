import multiprocessing


def worker(num):
    """
    worker function
    :return:
    """
    print(f'Worker {num} is working...')
    return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
