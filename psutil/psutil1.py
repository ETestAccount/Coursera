#! /usr/bin/env python3
import psutil
print(psutil.cpu_times())

print("Checking the percentation of CPU Count every 2 seconds")
print(psutil.cpu_percent(2))

print("Getting the Logical cpu cores in a computer")
print(psutil.cpu_count(logical=True))

print("Checking the statistics of the computer CPU")
print(psutil.cpu_stats()
)
