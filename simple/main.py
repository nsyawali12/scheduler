import schedule
import time

def job():
    print("Learning Scheduler...")
def coding():
    print("Programming time ...")
# creating time schedule example

schedule.every(10).seconds.do(job)
schedule.every(20).seconds.do(coding)

while True:
    schedule.run_pending()
    time.sleep(1)