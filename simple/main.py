import schedule
import time
import requests

def job():
    print("Learning Scheduler...")
def coding():
    print("Programming time ...")
    
def playing():
    print("Playing time....")   
    
# creating time schedule example

schedule.every(10).seconds.do(job)
schedule.every(20).seconds.do(coding)

## creating time schedule in everytime example
schedule.every().day.at("11:40").do(playing)

while True:
    schedule.run_pending()
    time.sleep(1)