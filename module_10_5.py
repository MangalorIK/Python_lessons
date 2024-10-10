import multiprocessing
import os
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as f:
        all_data.append(f.readlines())


files = [f"./files/file {i}.txt" for i in range(1, 5)]


if __name__ == '__main__':
    # linear variant
    start = datetime.now()
    for file in files:
        read_info(file)
    end = datetime.now()
    print(f"Последовательное считывание заняло: {end - start}")

    # multiproc
    start = datetime.now()
    proc_count = min(os.cpu_count(), len(files))

    with multiprocessing.Pool(processes=proc_count) as pool:
        pool.map(read_info, files)
    end = datetime.now()
    print(f"Мультипросессорный({proc_count}) подход занял: {end - start}")