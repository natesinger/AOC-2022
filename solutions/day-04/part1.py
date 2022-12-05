#!/usr/bin/python3

with open("input.txt","r") as fio:
    count = 0
    
    for n,line in enumerate(fio):
        parts = [ range(int(part.split('-')[0]),int(part.split('-')[1])+1) for part in line.strip().split(',')]
        
        if all(e in parts[1] for e in parts[0]) or all(e in parts[0] for e in parts[1]):
            count +=1 
            print(f"{n} [{line.strip()}]/{parts} full contain [{count}]")
        else:
            print(f"{n} [{line.strip()}]/{parts} no complete crossover")
        
    print(count)