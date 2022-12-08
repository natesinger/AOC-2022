#/usr/bin/python3

LINE_LEN = 99

# tree_grid[y][x]
tree_grid = [ [ item for item in line.strip() ] for line in open("input.txt", "r") ]

def get_view_score(x,y):
    tree_height = int(tree_grid[y][x])
    
    view_to_top    = [ int(tree_grid[index][x]) for index in range(y) ][::-1]
    view_to_bottom = [ int(tree_grid[index][x]) for index in range(y+1,LINE_LEN) ]
    view_to_left   = [ int(tree_grid[y][index]) for index in range(x) ][::-1]
    view_to_right  = [ int(tree_grid[y][index]) for index in range(x+1,LINE_LEN) ]
    
    score_to_top = 0
    if view_to_top[0] >= tree_height: score_to_top = 1
    else:
        for i in view_to_top:
            if i < tree_height: score_to_top+=1
            else:
                score_to_top+=1
                break
    
    score_to_bottom = 0
    if view_to_bottom[0] >= tree_height: score_to_bottom = 1
    else:
        for i in view_to_bottom:
            if i < tree_height: score_to_bottom+=1
            else:
                score_to_bottom+=1
                break
            
    score_to_left = 0
    if view_to_left[0] >= tree_height: score_to_left = 1
    else:
        for i in view_to_left:
            if i < tree_height: score_to_left+=1
            else:
                score_to_left+=1
                break
            
    score_to_right = 0
    if view_to_right[0] >= tree_height: score_to_right = 1
    else:
        for i in view_to_right:
            if i < tree_height: score_to_right+=1
            else:
                score_to_right+=1
                break

    return score_to_top * score_to_bottom * score_to_left * score_to_right


top_score = 0

for y in range (1,LINE_LEN-1):
    for x in range(1,LINE_LEN-1):
        if get_view_score(x,y) > top_score: top_score = get_view_score(x,y)

print(top_score)