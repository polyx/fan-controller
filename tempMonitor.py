#!/usr/bin/env python3

import subprocess
import sys
import re

print("fan status is:")
counter = 0
# temprature is shown on line 11
# actual value is char 17-18
temprature = int(subprocess.getoutput("sensors").split('\n')[10][17:19])
if 40<temprature<50:
    print("Temprature is > 40")
    print(temprature)
elif temprature>50:
    print("Temprature is > 50")
    print(temprature)