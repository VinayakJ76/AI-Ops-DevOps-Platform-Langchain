import time

def run_forever(task, interval):

    while True:
        task()
        time.sleep(interval)