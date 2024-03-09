import time
import threading

start = time.perf_counter()
threads = []


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Finished sleeping!")


for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


end = time.perf_counter()
total_time = end - start
print(f"Finished in {round(total_time, 2)} second(s)")
