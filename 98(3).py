# Creating a pool of worker processes

from multiprocessing import Pool


def process_task(task):
    # Do some work here
    print("Task processed:", task)


if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)
