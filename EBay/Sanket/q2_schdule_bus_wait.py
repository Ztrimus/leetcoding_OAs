'''
-----------------------------------------------------------------------
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
File: q2_schdule_bus_wait.py
Creation Time: Oct 31st 2023 11:54 am
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''
from datetime import datetime

# Binary Search
def solution(schedule, time):
    current_time = datetime.strptime(time, "%H:%M")
    next_bus_time = None
    
    left, right = 0, len(schedule) - 1
    while left <= right:
        mid = (left + right) // 2
        bus_time = datetime.strptime(schedule[mid], "%H:%M")

        if bus_time >= current_time:
            next_bus_time = bus_time
            right = mid - 1
        else:
            left = mid + 1

    if next_bus_time is None:
        return "-1"  # No more buses scheduled for the day
    else:
        waiting_time = next_bus_time - current_time
        hours, minutes = divmod(waiting_time.total_seconds() // 60, 60)
        return f"{int(hours):02d}:{int(minutes):02d}"

# Normal Search
def solution_n(schedule, time):
    current_time = datetime.strptime(time, "%H:%M")
    next_bus_time = None

    for bus_time in schedule:
        bus_time = datetime.strptime(bus_time, "%H:%M")
        if bus_time >= current_time:
            next_bus_time = bus_time
            break

    if next_bus_time is None:
        return "-1"  # No more buses scheduled for the day
    else:
        waiting_time = next_bus_time - current_time
        hours, minutes = divmod(waiting_time.total_seconds() // 60, 60)
        return f"{int(hours):02d}:{int(minutes):02d}"

print(solution(["12:30", "14:00", "19:55"], "14:30"))
print(solution(["12:30", "14:00", "19:55"], "20:00"))
print(solution(["12:30", "14:00", "19:55"], "14:00"))
print(solution(["12:30", "14:00", "19:55"], "12:00"))