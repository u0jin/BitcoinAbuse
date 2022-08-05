import requests
from urllib.request import urlretrieve
import time
from apscheduler.schedulers.background import BlockingScheduler


def DB():
    url = "https://www.bitcoinabuse.com/api/download/1d?api_token=9GyW3puHaW635XsQgeNlvIJaSohBDD20xqpTSu2w"

    resp = requests.get(url)

    if resp.status_code == 200 : 
        print("hi")
        urlretrieve(url, "./BC_DB.csv")



def backgroundScheduler():
    scheduler = BlockingScheduler(timezone='Asia/Seoul')
    scheduler.add_job(DB, 'cron', hour=20)
    scheduler.start()

if __name__ == '__main__':
    backgroundScheduler()

