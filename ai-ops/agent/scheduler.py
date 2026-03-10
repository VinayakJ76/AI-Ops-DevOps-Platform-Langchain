import time

from agent.main import run_agent


def start():

    while True:

        run_agent()

        time.sleep(60)