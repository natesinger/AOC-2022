#!/usr/bin/python3

"""
Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
"""

import re, time


def print_map(formation_map, min_x, max_x, min_y, max_y):
    markers_y = [494, 500, 503]

    for i in range(3):
        print("     ", end="")
        for x_pos in range(min_x,max_x):
            if x_pos in markers_y: print(str(x_pos)[i],end="")
            else: print(" ",  end="")
        print()

    for m,y in enumerate(formation_map):
        print(f"{m:03d}  " , end="")
        for n,x in enumerate(y): print(x,end="")
        print()



# get all data
with open("input.txt", "r") as fio:
    all_data = [ line.strip() for line in fio ]


# determine minimum and maximum bounds from the input
min_x,max_x,min_y,max_y = 500,500,0,1

for line in all_data:
    points = re.findall(r"[0-9]*,[0-9]*", line)
    
    for point in points:
        tmp_x_str,tmp_y_str = point.split(",")
        
        if int(tmp_x_str) > max_x:  max_x = int(tmp_x_str)
        if int(tmp_x_str) < min_x:  min_x = int(tmp_x_str)
        
        if int(tmp_y_str) > max_y:  max_y = int(tmp_y_str)
        if int(tmp_y_str) < min_y:  min_y = int(tmp_y_str)


# add some space to the formation
max_x += 1
max_y += 1


# map the existing rock formation with minimum and maximum bounds
formation_map = [ [ '.' for x in range(min_x,max_x) ] for y in range(min_y,max_y) ]
known_formation_points = []

for line in all_data:
    # get all points in formation
    formation_points = line.strip().split(" -> ")
    
    # map formation
    i = 0
    while True:
        try:
            end_x,start_y = formation_points[i].split(",")
            start_x,end_y = formation_points[i+1].split(",")
            
            # if vertical line
            if start_x == end_x:
                x = int(start_x)
                
                if int(start_y) > int(end_y):
                    for y in range(int(end_y),int(start_y)+1):
                        known_formation_points.append((x, y))
                else:
                    for y in range(int(start_y),int(end_y)+1):
                        known_formation_points.append((x, y))
            
            # if horizontal line
            if start_y == end_y:
                y = int(start_y)
                
                if int(start_x) > int(end_x):
                    for x in range(int(end_x),int(start_x)+1):
                        known_formation_points.append((x, y))
                else:
                    for x in range(int(start_x),int(end_x)+1):
                        known_formation_points.append((x, y))
            
            i += 1
        except IndexError: break
        
known_formation_points = sorted(set(known_formation_points))

for point in known_formation_points:
    target_x, target_y = point[0]-min_x, point[1]-min_y
    formation_map[target_y][target_x] = "#"


def get_next_sand_position(current_sand_position:tuple, current_map:list) -> tuple:
    btm_lft_x,btm_lft_y = current_sand_position[0]-1,current_sand_position[1]+1
    btm_ctr_x,btm_ctr_y = current_sand_position[0]  ,current_sand_position[1]+1
    btm_rgt_x,btm_rgt_y = current_sand_position[0]+1,current_sand_position[1]+1
    
    # immediately bellow
    if current_map[btm_ctr_y][btm_ctr_x] == ".":
        return(btm_ctr_x, btm_ctr_y, False)
    
    # to the left
    elif current_map[btm_lft_y][btm_lft_x] == '.':
        return(btm_lft_x, btm_lft_y, False)
    
    # to the right
    elif current_map[btm_rgt_y][btm_rgt_x] == ".":
        return(btm_rgt_x, btm_rgt_y, False)
    
    # else settles
    else:
        return(current_sand_position[0], current_sand_position[1], True)


# solve part 1

try:
    total_sand_dropped = 0
    while True:
        total_sand_dropped += 1

        # drop a grain of sand
        sand_starting_position = (500-min_x,0)
        sand_position = sand_starting_position

        # move sand one position
        while True:
            # determine where its going
            result_x, result_y, result_settle = get_next_sand_position(sand_position,formation_map)
            
            # if the sand cant move
            if result_settle: break
            
            # else update to new position
            else: sand_position = (result_x, result_y)
            

        formation_map_with_tmp_sand = formation_map

        # print to user
        for y_pos,y in enumerate(formation_map):
            for x_pos,x in enumerate(formation_map):
                relative_x = x_pos+min_x
                
                if sand_position[0] == x_pos and sand_position[1] == y_pos:
                    formation_map_with_tmp_sand[y_pos][x_pos] = "o"


        formation_map = formation_map_with_tmp_sand
        print_map(formation_map, min_x, max_x, min_y, max_y)

# account for last drop by -1
except IndexError:
    print(f"Total sand dropped: {total_sand_dropped-1}")