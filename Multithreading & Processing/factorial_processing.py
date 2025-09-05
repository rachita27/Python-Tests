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

    with ProcessPoolExecutor(max_workers= 3) as executor:
        results = executor.map(fact,lst)

    for i in results:
        print(i)

    print(f"Total Time take is {(datetime.now() - st).total_seconds()}")

