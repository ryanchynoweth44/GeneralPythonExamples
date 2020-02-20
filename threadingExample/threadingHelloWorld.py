import logging
import threading
import time


# threads execute in the form of functions
# this function will run forever based off our loop but the threading library 
# has a "run_forever" function that is useful for similar situations. 
def thread_function(name, sleep_secs):
    while True:
        logging.info("Thread %s: first line", name)
        time.sleep(sleep_secs)
        logging.info("Thread %s: second line", name)



# format our logger as needed
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


logging.info("----------------------- Creating our first thread.")
x = threading.Thread(target=thread_function, args=("one",5))

logging.info("----------------------- Running our first thread")
x.start()


logging.info("----------------------- Creating our second thread")
y = threading.Thread(target=thread_function, args=("two",1))

logging.info("----------------------- Creating our second thread")
y.start()


