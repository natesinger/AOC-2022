#!/usr/bin/python3

import os

deleteable_dirs = []

total_disk = 70000000
required_free = 30000000
current_use = 40358913
current_free = total_disk-current_use

amount_to_clear = required_free - current_free

for subdir, dirs, files in os.walk("/Users/nsinger/Desktop/code/aoc-2022/solutions/day-07/puzzle_40358913"):
    dir_size = int(subdir.split("/")[-1].split("_")[1])
    
    if dir_size >= amount_to_clear: deleteable_dirs.append(dir_size)

print(min(deleteable_dirs))
