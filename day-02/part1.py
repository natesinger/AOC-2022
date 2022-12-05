#!/usr/bin/python3
with open("input.txt","r") as fio:
    total = 0
    
    for l in fio:
        opponent = l[0]
        me = l[2]
        
        score = {'X':1, 'Y':2, 'Z':3}[me]
        
        if opponent == 'A': #rock
            score += {'X':3, 'Y':6, 'Z':0}[me]
            
        elif opponent == 'B': #paper
            score += {'X':0, 'Y':3, 'Z':6}[me]
            
        elif opponent == 'C': #scissors
            score += {'X':6, 'Y':0, 'Z':3}[me]
        
        total += score
    
    print(total)