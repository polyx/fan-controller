#!/usr/bin/env python3
import subprocess
import sys

if len(sys.argv) > 1:
    input = sys.argv[1]
    print("setting fan speed...")
    mycmd = subprocess.getoutput("echo level {}| sudo tee /proc/acpi/ibm/fan".format(input))
    print("Return from acpi-driver:")
    print(mycmd)
else:
    print("fan status is:")
    status = subprocess.getoutput("cat /proc/acpi/ibm/fan")
    print(status, "\n")