import multiprocessing
from multiprocessing import Pool
import multiprocessingExample.functions as f
print("Number of cpu : ", multiprocessing.cpu_count())



tasks = [1,2,3,4,5,6,7,8]
concurrent_processes = multiprocessing.cpu_count()


def pool_handler():
    p = Pool(concurrent_processes)
    p.map(f.processing_function, tasks)


pool_handler()