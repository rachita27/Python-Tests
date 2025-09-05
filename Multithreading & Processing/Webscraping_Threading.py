import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup 
import time 
from datetime import datetime

from concurrent.futures import ThreadPoolExecutor

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'

]


def reading(url):
    response=requests.get(url)
    time.sleep(3)
    soup=BeautifulSoup(response.content,'html.parser')
    time.sleep(1)
    return (f'Fetched {len(soup.text)} characters from {url}')


if __name__ == "__main__":
    st = datetime.now()

    with ThreadPoolExecutor(max_workers= 3) as executors:
        results = executors.map(reading,urls) ##func, argument

    for res in results:
        print(res)


    print(f"Total time take: {(datetime.now() - st).total_seconds()}")



