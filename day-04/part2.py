#!/usr/bin/python3

def check_for_contains(list1:object, list2:object):
    for i in list1:
        if i in list2:
            return True
    return False

with open("input.txt","r") as fio:
    count = 0
    
    for n,line in enumerate(fio):
        parts = [ range(int(part.split('-')[0]),int(part.split('-')[1])+1) for part in line.strip().split(',')]
        
        if check_for_contains(parts[0],parts[1]) or check_for_contains(parts[1],parts[0]):
            count +=1
        
    print(count)