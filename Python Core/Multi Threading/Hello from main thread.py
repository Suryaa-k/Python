import threading

def worker():
    print("Hello from worker thread")

t = threading.Thread(target=worker)
t.start()

print("Hello from main thread")

t.join()