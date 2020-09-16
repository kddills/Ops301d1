
# Script name:    OpsChallenge12.py
# Author:         Kimberly Dills
# Date of last revision: 9/15/2020
# Description of purpose: Fetch system information using psutil

import psutil

cpuInfo = str(psutil.cpu_times())

result = cpuInfo.split(", ")

print(result)

# Declaration of variables:

# Time spent by normal processes executing in user mode

print(result[0],"second")

# Time spent by processes executing in kernel mode

print(result[2],"second")

# Time when system was idle

print(result[3],"second")

# Time spent by priority processes executing in user mode

print(result[1],"second")

# Time spent waiting for I/O to complete.

print(result[4],"second")

# Time spent for servicing hardware interrupts

print(result[5],"second")

# Time spent for servicing software interrupts

print(result[6],"second")

# Time spent by other operating systems running in a virtualized environment

print(result[7],"second")

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

print(result[8],"second")
