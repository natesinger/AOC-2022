#!/usr/bin/python3

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    
import collections


def get_solution(grid, starting_position, target_char='E') -> int:    
    queue = collections.deque()
    visited = set()
    
    # starting position
    queue.append((starting_position[1],starting_position[0],0))
    
    # define directions of movement
    directions = [(1,0), (-1,0), (0,-1), (0,1)]
    
    # iterrate on queue
    while queue:
        cur_row, cur_col, step = queue.popleft()
        
        print(f"current test: {grid[cur_row][cur_col]}")
        
        # got match
        if grid[cur_row][cur_col] == target_char:
            # account for first step and current step
            return step+2, visited
        
        # continue search
        else:
            # test in each direction
            for row_inc, col_inc in directions:
                new_row = cur_row + row_inc
                new_col = cur_col + col_inc
                
                # verify in grid
                try:
                    assert(new_row >= 0 and new_col >= 0)
                    print(f"checking new item: {grid[new_row][new_col]}")
                    
                    # verify not in already visited
                    if (new_row,new_col) not in visited:
                        
                        # also check for valid move
                        cur_value = ord(grid[cur_row][cur_col])
                        new_value = ord(grid[new_row][new_col])                        
                        
                        # if 'S' set to 'a'
                        if cur_value == 83: cur_value = 97
                        
                        
                        # can be one higher or any amount lower
                        if (cur_value -26 <= new_value <= cur_value +1) or chr(new_value) == 'E':
                            
                            print(cur_value, new_value)
                            
                            queue.append((new_row, new_col, step+1))
                            visited.add((new_row,new_col))
                    
                    
                except IndexError: pass
                except AssertionError: pass
                    
            
    print('nope')
    return -1, visited

# ingest data
with open("input.txt", "r") as fio:
    # inverted_heatmap[y][x]
    inverted_heatmap = [ [ x for x in y.strip() ] for y in fio]
    
    result, visited = get_solution(inverted_heatmap, [0,20], 'E')
    
    # draw it
    with open("input.txt", "r") as fio:
        for y,line in enumerate(fio):
            for x,c in enumerate(line.strip()):
                if (y,x) in visited: print(f"{Colors.BOLD}{Colors.GREEN}{c}{Colors.END}", end="")
                else: print(c, end="")
            print()
    
    print(result)
