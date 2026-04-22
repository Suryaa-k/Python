# 1.Write a Python program that creates a worker thread which prints “Hello
# from worker thread” while the main thread prints “Hello from main thread”, and
# ensure that the main thread waits for the worker thread to finish execution
# before the program exits.

# 2.Write a Python program that creates three separate threads where each
# thread prints numbers from 1 to 5, and every printed number must be prefixed
# with the name of the thread that printed it, such as “Thread-1: 3”.

# 3.Write a Python program in which a thread accepts two integer arguments,
# computes their sum, prints the result from inside the thread, and ensures that
# the main thread waits until the worker thread completes execution.

# 4.Write a Python program where two threads increment a shared variable named
# counter exactly 100000 times each without using any synchronization mechanism,
# and print the final value of the counter to demonstrate inconsistent or
# incorrect results caused by a race condition.

# 5.Modify the previous program so that the shared variable counter is updated
# in a thread-safe manner using threading.Lock, and ensure that the final printed
# value of the counter is always correct.

# 6.Write a Python program where one thread prints “A started” and then sleeps
# for two seconds, another thread prints “B started”, and the execution order is
# controlled in such a way that the second thread starts only after the first
# thread has completely finished.

# 7.Write a Python program in which three worker threads wait until a
# synchronization signal is received, the main thread sleeps for two seconds and
# then signals all waiting threads using an event, after which each worker thread
# prints a message indicating that it has started execution.

# 8.Write a Python program that creates five threads competing for a shared
# resource, restricts access so that only two threads can enter the critical
# section at the same time using a semaphore, and prints a message whenever a
# thread enters and exits the critical section.

# 9.Write a Python program that starts a daemon thread running an infinite
# loop which repeatedly prints “Running in background”, while the main thread
# sleeps for two seconds and then exits, and observe what happens to the daemon
# thread when the main program terminates.

# 10. Write a Python program using ThreadPoolExecutor with three worker threads
# that submits tasks to compute the square of numbers from 1 to 5 and prints each
# result as soon as the corresponding task completes