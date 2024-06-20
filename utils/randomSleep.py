import time
import random

def randomSleeper(max=0,min=2):
    sleepCounter=random.uniform(max, min)
    time.sleep(sleepCounter)
