#!/usr/bin/python3
import string

with open("input.txt","r") as fio:
    total = 0
    group = []
    priorities = { x:n+1 for n,x in enumerate(string.ascii_lowercase + string.ascii_uppercase) }
    
    for n, line in enumerate(fio):
        line = line.strip()        
        group.append(line)
        
        if (n % 3) == 2:
            matches = []
            
            for i in group[0]:
                if i in group[1]:
                    if i in group[2]:        
                        matches.append(i)
                                   
            group = []
            total += priorities[matches[0]]
    
    print(total)