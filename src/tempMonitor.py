#!/usr/bin/env python3

import subprocess
from time import sleep

import fan

#fan.get_fan_status()


def control():
    while True:
        temprature = int(subprocess.getoutput("sensors").split('\n')[6][17:19])
        if 40 < temprature < 50:
            print("Temprature is > 40")
            print('setting fan to 1')
            fan.set_fan(1)
        elif 50 < temprature < 60:
            print("Temprature is between 50 and 60")
            print('setting fan to 1')
            fan.set_fan(4)
        elif 60 < temprature:
            print("Temprature is over 60")
            print('setting fan to 7')
            fan.set_fan(7)

        sleep(1)


if __name__ == '__main__':
    control()
    # stat = subprocess.getoutput("sensors")
    # print(stat)
    # print(subprocess.getoutput("sensors").split('\n')[6][17:19])
