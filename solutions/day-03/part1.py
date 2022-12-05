#!/usr/bin/python3
import string

with open("input.txt","r") as fio:
    total = 0
    priorities = { x:n+1 for n,x in enumerate(string.ascii_lowercase + string.ascii_uppercase) }
    
    for line in fio:
        line = line.strip()
        line_half_point = int(len(line.strip())/2)
        
        matches = [ i for i in line[:line_half_point] if i in line[line_half_point:] ]
        total += priorities[matches[0]]
                
    print(total)