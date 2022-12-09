#!/usr/bin/python3

ROPE_LEN = 10
knot_pos_x,knot_pos_y = [0 for len in range(ROPE_LEN)],[0 for len in range(ROPE_LEN)]

tail_positions = []

def tail_from_head(head_pos_x,head_pos_y, tail_pos_x,tail_pos_y):       
    if (tail_pos_x == head_pos_x -2) and (tail_pos_y == head_pos_y -2): # bottom left
        tail_pos_x,tail_pos_y = head_pos_x-1,head_pos_y-1
    elif (tail_pos_x == head_pos_x -2) and (tail_pos_y == head_pos_y +2): # top left
        tail_pos_x,tail_pos_y = head_pos_x-1,head_pos_y+1
    elif (tail_pos_x == head_pos_x +2) and (tail_pos_y == head_pos_y -2): # bottom right
        tail_pos_x,tail_pos_y = head_pos_x+1,head_pos_y-1
    elif (tail_pos_x == head_pos_x +2) and (tail_pos_y == head_pos_y +2): # top right
        tail_pos_x,tail_pos_y = head_pos_x+1,head_pos_y+1
    
    elif tail_pos_y == head_pos_y -2: # bottom
        tail_pos_x,tail_pos_y = head_pos_x,head_pos_y-1
    elif tail_pos_x == head_pos_x -2: # left
        tail_pos_x,tail_pos_y = head_pos_x-1,head_pos_y
    elif tail_pos_y == head_pos_y +2: #top
        tail_pos_x,tail_pos_y = head_pos_x,head_pos_y+1
    elif tail_pos_x == head_pos_x +2: #right
        tail_pos_x,tail_pos_y = head_pos_x+1,head_pos_y
    
    return tail_pos_x,tail_pos_y 

with open("input.txt", "r") as fio:
    for line in fio:
        direction, value = line.strip().split(' ')
        
        # gotta move one at a time
        for i in range(int(value)):
            if   direction == 'U': knot_pos_y[0] += 1
            elif direction == 'D': knot_pos_y[0] -= 1
            elif direction == 'L': knot_pos_x[0] -= 1
            elif direction == 'R': knot_pos_x[0] += 1
            
            for index in range(ROPE_LEN-1): #account for head
                knot_pos_x[index+1],knot_pos_y[index+1] = tail_from_head(
                    knot_pos_x[index],
                    knot_pos_y[index],
                    knot_pos_x[index+1],
                    knot_pos_y[index+1]
                )
                
            tail_positions.append(f"{knot_pos_x[ROPE_LEN-1]},{knot_pos_y[ROPE_LEN-1]}")
                

print(len(sorted(set(tail_positions))))