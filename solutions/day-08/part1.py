#/usr/bin/python3

LINE_LEN = 99
# tree_grid[y][x]

total_edge_trees = ( (LINE_LEN-2) * 4 ) + 4
total_interior_trees = 0

tree_grid = [ [ item for item in line.strip() ] for line in open("input.txt", "r") ]

def determine_visible(x,y):
    tree_height = int(tree_grid[y][x])
    
    position_to_top    = max([ int(tree_grid[index][x]) for index in range(y) ])
    position_to_bottom = max([ int(tree_grid[index][x]) for index in range(y+1,LINE_LEN) ])
    position_to_left   = max([ int(tree_grid[y][index]) for index in range(x) ])
    position_to_right  = max([ int(tree_grid[y][index]) for index in range(x+1,LINE_LEN) ])
        
    if (
        tree_height > position_to_top or
        tree_height > position_to_bottom or
        tree_height > position_to_left or
        tree_height > position_to_right
    ): return True
    else: return False

for y in range (1,LINE_LEN-1):
    for x in range(1,LINE_LEN-1):
        if determine_visible(x,y):
            total_interior_trees += 1
    
print(total_edge_trees+total_interior_trees)