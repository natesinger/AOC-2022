#!/usr/bin/python3
import ast

"""
What are the indices of the pairs that are already in the right order? (The first pair has index 1, the second pair has index 2, and so on.) In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.
"""

# processor function
def process_pair(left, right, depth=0) -> str:
    #print(f"{depth * '  '}- Compare {left} vs {right}")
    
    match (left, right):
        # both ints
        case (int(), int()):
            if left > right:
                #print(f"{(depth+1)*'  '}- Right side is smaller, so inputs are not in the right order")
                return 'incorrect'
            elif left < right:
                #print(f"{(depth+1)*'  '}- Left side is smaller, so inputs are in the right order")
                return 'correct'
            elif left == right:
                return 'same'
        
        # both lists
        case (list(), list()):
            len_left,len_right = len(left),len(right)
            longer_length = len_left if len_left > len_right else len_right
            
            # start new jobs at one depth lower
            for i in range(longer_length):
                try: left[i]
                except:
                    #print(f"{(depth+1)*'  '}- Left side ran out of items, so inputs are in the right order")
                    return 'correct'
                
                try: right[i]
                except:
                    #print(f"{(depth+1)*'  '}- Right side ran out of items, so inputs are not in the right order")
                    return 'incorrect'
                
                result = process_pair(left[i], right[i], depth+1)
                
                if result == 'correct': return 'correct'
                elif result == 'incorrect': return 'incorrect'
                elif result == 'same': continue
            return 'same'
        
        # mixed types
        case (list(), int()):
            #print(f"{(depth)*'  '}- Mixed types; convert right to [{right}] and retry comparison")
            result = process_pair(left, [right], depth)
            if result == 'correct': return 'correct'
            elif result == 'incorrect': return 'incorrect'
            elif result == 'same': return 'same'
            
        case (int(), list()):
            #print(f"{(depth)*'  '}- Mixed types; convert left to [{left}] and retry comparison")
            result = process_pair([left], right, depth)
            if result == 'correct': return 'correct'
            elif result == 'incorrect': return 'incorrect'
            elif result == 'same': return 'same'


# retreive data
with open('input-modified.txt','rt') as fio:
    input_data = [ line.strip() for line in fio ]


# solve part 2
output_list = []
for n,line in enumerate(input_data):
    
    # pull three lines and if its the third line, process
    if n % 3 == 2:
        pair_count = n // 3
        first_line = ast.literal_eval(input_data[n-2])
        second_line = ast.literal_eval(input_data[n-1])
        
        # process
        #print(f"== Pair {pair_count+1} ==")
        result = process_pair(first_line, second_line)
        
        if result == 'correct': 
            output_list.append(first_line)
            output_list.append(second_line)
        elif result == 'incorrect':
            output_list.append(second_line)
            output_list.append(first_line)



start_at_0 = True

for i in range(1000):
    start_at_0 = not start_at_0
    input_list = output_list
    output_list = []

    if start_at_0:
        for n in range(0,len(input_list),2):
            first_line = input_list[n]
            second_line = input_list[n+1]
            
            result = process_pair(first_line, second_line)
            
            if result == 'correct': 
                output_list.append(first_line)
                output_list.append(second_line)
            elif result == 'incorrect':
                output_list.append(second_line)
                output_list.append(first_line)

    # offset run
    else:
        output_list.append(input_list[0])
        
        for n in range(1,len(input_list)-1,2):
            first_line = input_list[n]
            second_line = input_list[n+1]
            
            result = process_pair(first_line, second_line)
            
            if result == 'correct': 
                output_list.append(first_line)
                output_list.append(second_line)
            elif result == 'incorrect':
                output_list.append(second_line)
                output_list.append(first_line)
            
        output_list.append(input_list[-1])

indicies = []
for n,l in enumerate(output_list):
    print(l)
    if l == [[2]] or l == [[6]]:
        indicies.append(n+1)

print(f"\nAnswer: {indicies[0] * indicies[1]}")