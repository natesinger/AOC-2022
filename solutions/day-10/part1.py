#!/usr/bin/python3

cycle_number = 0
register_value = 0

signal_strengths = []
positions = []

def verify_at_cycle():
    #print(register_value)
    if (cycle_number) % 40 == 20:
        print(f"hit at cycle {cycle_number} {register_value}")
        signal_strengths.append((cycle_number)*(register_value+1))
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

print(signal_strengths)
print(sum(signal_strengths))