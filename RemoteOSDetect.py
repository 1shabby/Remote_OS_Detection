# Author: Greg Schabert
# CS 4312 - Operating systems

import subprocess
import re

print("This script utilizes the ttl from a ping to determine the OS of a remote machine.\n"
      "While this implementation does work for a good number of cases, it is by no means perfect.\n"
      "This is however the best implementation I could think of to determine OS without NMAP.\n")


response = input(
    "Please enter the domain name or IP that you would like to find the OS of.\n")

print('Pinging ....')
p = subprocess.Popen(["ping", response], stdout=subprocess.PIPE)

res = p.communicate()[0]


if p.returncode > 0:
    print('Server error')
else:
    pattern = re.compile(r'TTL=(?P<number>\d*)', re.I | re.M)
    reg_found = pattern.findall(str(res))
    ttl = int(reg_found[0])
    print(str(ttl))
    if ttl <= 254 and ttl > 128:
        print("OS: Solaris/ AIX")
    elif ttl <= 128 and ttl > 64:
        print("OS: Windows")
    elif ttl == 64:
        print("OS: Linux/ Unix")
    elif ttl == 60:
        print("OS: Mac OS")
    else:
        print("OS unable to be confirmed. Potentially Linux based.")
response = input("press any button to quit.")
