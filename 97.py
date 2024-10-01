import threading
import time

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


# Normal Code
# time1 = time.perf_counter()
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()

# Same code using Threads
time3 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()
time4 = time.perf_counter()

t1.join()
t2.join()
t3.join()
# Calculating Time
# print(time2 - time1)
print(time4 - time3)
