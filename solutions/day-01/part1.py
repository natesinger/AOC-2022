#!/usr/bin/python3
with open("input.txt","r") as fio:
    totals = []
    current = 0
    
    for line in fio:
        if line == "\n":
            totals.append(current)
            current = 0
            
        else: current += int(line)
            
    print(max(totals))