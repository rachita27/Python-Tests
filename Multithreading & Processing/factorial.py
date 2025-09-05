import math
from datetime import datetime
import time
import sys

from concurrent.futures import ProcessPoolExecutor

sys.set_int_max_str_digits(12000000)

def fact(numb):
    time.sleep(2)
    return math.factorial(numb)

lst = [800,197, 9000, 2000, 40000,60000]

if __name__ == "__main__":
    st = datetime.now()

    for i in lst:
        print(fact(i))

    print(f"Total Time take is {(datetime.now() - st).total_seconds()}")

