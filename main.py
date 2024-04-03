from src.claim import claim
from src.helper import read_profiles
from threading import Thread
import numpy
import settings
import time


profiles = read_profiles()
chunks = numpy.array_split(profiles, settings.thread_count)
threads = list()


for thread_profiles_list in chunks:
    threads.append(Thread(target=claim, args=(thread_profiles_list,)))
for th in threads:
    th.start()
    time.sleep(2)

for th in threads:
    th.join()
    time.sleep(2)
