#!/usr/bin/python3

import os

total = 0

os.system("mkdir puzzle")

with open("input.txt","r") as fio:
    for n, line in enumerate(fio):
        if line.strip()[0] == '$':
            command = line.strip()[2:].split(" ")
            if command[0] == "cd":
                if command[1] == "/":
                    os.chdir("/Users/nsinger/Desktop/code/aoc-2022/solutions/day-07/puzzle")
                    
                elif command[1] == "..":
                    current_dir = os.system("pwd")
                    os.chdir("..")
                    
                else:
                    os.system(f"mkdir {command[1]}")
                    os.chdir(f"{command[1]}")
            
        else: 
            response = line.strip().split()
            if response[0] == "dir":
                directory = response[1]
                os.system(f"mkdir {directory}")
            else:
                size = response[0]
                filename = response[1]
                os.system(f"touch {filename}_{size}")


for i in range(10):
    for subdir, dirs, files in os.walk("/Users/nsinger/Desktop/code/aoc-2022/solutions/day-07/puzzle"):
    
        files = os.listdir(subdir)
        
        directory_total = 0
        dont_set = False
        for file in files:
            if not "_" in file: #its a dir, skip it
                dont_set = True
            else: # add to total
                directory_total += int(file.split("_")[1])
        
        if not dont_set:
            if not "_" in subdir:
                os.system(f"mv {subdir} {subdir}_{directory_total}")


for subdir, dirs, files in os.walk("/Users/nsinger/Desktop/code/aoc-2022/solutions/day-07/puzzle_40358913"):
    dir_size = int(subdir.split("/")[-1].split("_")[1])
    
    if dir_size <= 100000: total += dir_size
    
print(total)