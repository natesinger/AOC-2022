#!/usr/bin/python3

head_pos_x,head_pos_y = 0,0
tail_pos_x,tail_pos_y = 0,0

head_positions = []
tail_positions = []

with open("input.txt", "r") as fio:
    for line in fio:
        direction, value = line.strip().split(' ')
        
        # gotta move one at a time
        for i in range(int(value)):
            if   direction == 'U': head_pos_y += 1
            elif direction == 'D': head_pos_y -= 1
            elif direction == 'L': head_pos_x -= 1
            elif direction == 'R': head_pos_x += 1
            head_positions.append(f"{head_pos_x},{head_pos_y}")
            
            if tail_pos_y == head_pos_y -2: # bottom
                tail_pos_x,tail_pos_y = head_pos_x,head_pos_y-1
            elif tail_pos_x == head_pos_x -2: # left
                tail_pos_x,tail_pos_y = head_pos_x-1,head_pos_y
            elif tail_pos_y == head_pos_y +2: #top
                tail_pos_x,tail_pos_y = head_pos_x,head_pos_y+1
            elif tail_pos_x == head_pos_x +2: #right
                tail_pos_x,tail_pos_y = head_pos_x+1,head_pos_y
            
            tail_positions.append(f"{tail_pos_x},{tail_pos_y}")
            
    
print(len(sorted(set(tail_positions))))