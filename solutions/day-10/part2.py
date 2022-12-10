#!/usr/bin/python3
cycle_number = 0
register_value = 0

positions = []

def verify_at_cycle():
    positions.append(register_value+1)

with open("input.txt", "r") as fio:
    for line in fio:
        line = line.strip().split(' ')
        
        if line[0] == "addx":
            cycle_number += 1
            verify_at_cycle()
            
            
            cycle_number += 1
            verify_at_cycle()
            register_value += int(line[1])
            
            
        elif line[0] == "noop":
            cycle_number += 1
            verify_at_cycle()
        
        else:
            print("something weird happened")
            exit()

for position,register in enumerate(positions):
    if position % 40 == 0: print()
    
    if position % 40 == register or (position % 40)+1 == register or (position % 40)-1 == register:
        print("#",end='')
    else:
        print("-",end='')
    