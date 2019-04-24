import multiprocessing


def worker():
    """
    worker function
    :return:
    """
    print('Worker working...')
    return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
