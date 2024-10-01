import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # Syntax 1
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())

        # Syntax 2
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingDemo()
