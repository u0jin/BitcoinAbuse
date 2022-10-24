import requests
from urllib.request import urlretrieve
import time
import sys
from apscheduler.schedulers.background import BlockingScheduler
import csv 
import pandas as pd

import shutil


def DB():
    url = "https://www.bitcoinabuse.com/api/download/1d?api_token=9GyW3puHaW635XsQgeNlvIJaSohBDD20xqpTSu2w"
    resp = requests.get(url)

    if resp.status_code == 200 : 

        print("1")
        urlretrieve(url, "./BC_DB.csv")
        
        from_file_path = './BC_DB.csv' # 복사할 파일
        to_file_path = './abuse_DB.csv' # 복사 위치 및 파일 이름 지정
        shutil.copyfile(from_file_path, to_file_path) 

        print("2")


def backgroundScheduler():
    scheduler = BlockingScheduler(timezone='Asia/Seoul')
    scheduler.add_job(DB, 'cron', second=10)
    scheduler.start()

if __name__ == '__main__':
    print("0")
    backgroundScheduler()
    
