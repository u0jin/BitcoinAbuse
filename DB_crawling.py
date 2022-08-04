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


#schedule.every().thursday.at("17:50").do(DB)

def backgroundScheduler():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.start()
    scheduler.add_job(DB, 'cron', hour=20)

if __name__ == '__main__':
    backgroundScheduler()

