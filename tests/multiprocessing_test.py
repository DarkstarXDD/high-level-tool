import multiprocessing
import time

start = time.perf_counter()


def do_something():
    print("Start sleeping for 5 second(s)...")
    time.sleep(5)
    print("Done sleeping...")


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)
    p3 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end = time.perf_counter()
    total_time = end - start

    print(f"Finished in {round(total_time, 2)} second(s)...")
