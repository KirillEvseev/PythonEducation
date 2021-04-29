
import csv
import datetime
import time
import os
import multiprocessing
import random
from collections import defaultdict
from threading import Thread
from itertools import repeat

def getstuff(filename, day):
    merchant_aggregated_orders = defaultdict(int)
    with open(filename) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        next(datareader, None)
        for row in datareader:
            timestamp, _, merchant_name, order_cost, is_success = row
            if (datetime.datetime.strptime(timestamp[:-16] , "%Y-%m-%d") == day) and (is_success == "false"):  
                merchant_aggregated_orders[merchant_name] += int(order_cost)
    return merchant_aggregated_orders

def fake(merchant_name):
    time.sleep(5)
    return [merchant_name, random.uniform(0.1, 0.9)]

if __name__ == '__main__':

    day = datetime.datetime.strptime(input("Write datetime yyyy-mm-dd: "), "%Y-%m-%d")
    files = []

    for file in os.listdir("./"):
        if file.endswith(".csv"):
            files.append(file)

    start_processing = time.time()

    pool_processes = multiprocessing.Pool(processes=len(files))
    data = pool_processes.starmap(getstuff, zip(files, repeat(day)))

    pool_processes.close()
    pool_processes.join() 

    result = defaultdict(int)

    for dict in data:
        for key, value in dict.items():
            result[key] += value
    
    finish_processing = time.time()

    print("time of parallel processes: ", finish_processing - start_processing)
    print("result before inflation: ", result)

    start_threading = time.time()

    pool_threads = multiprocessing.pool.ThreadPool(processes=len(result))
    data = pool_threads.starmap(fake, zip(result.keys()))

    pool_threads.close()
    pool_threads.join()

    result_inflation = {x[0]:x[1] for x in data}

    for key, value in result.items():
        result[key] = result[key] * (1 + result_inflation[key])

    finish_threading = time.time()
    print("time of parallel threading: ", finish_threading - start_threading)
    print("inflation: ", result_inflation)
    print("result after inflation: ", result)

