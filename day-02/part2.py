#!/usr/bin/python3
with open("input.txt","r") as fio:
    total = 0
    
    for l in fio:
        opponent = l[0]
        me = l[2]
        
        # outcome
        score = {'X':0, 'Y':3, 'Z':6}[me]
        
        # loss | draw | win
        
        if opponent == 'A': #rock
            score += {'X':3, 'Y':1, 'Z':2}[me]
            
        elif opponent == 'B': #paper
            score += {'X':1, 'Y':2, 'Z':3}[me]
            
        elif opponent == 'C': #scissors
            score += {'X':2, 'Y':3, 'Z':1}[me]
        
        total += score
    
    print(total)