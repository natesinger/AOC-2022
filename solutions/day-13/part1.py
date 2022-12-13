#!/usr/bin/python3
import ast

"""
What are the indices of the pairs that are already in the right order? (The first pair has index 1, the second pair has index 2, and so on.) In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.
"""

current_right = False
correct_indicies = []

done = False

def check_values(left, right, depth:int=1):
    global current_right, done
    
    if done: return False
    
    print(f"{(depth)*'  '}- Compare {left} vs {right}")
    
    if left == None:
        print(f"{(depth+1)*'  '}- Left side ran out of items, so inputs are in the right order")
        current_right = True
        done = True
        return True
    elif right == None:
        print(f"{(depth+1)*'  '}- Right side ran out of items, so inputs are not in the right order")
        done = True
        return True
        
    elif type(left) == int and type(right) == int:
        if left < right:
            print(f"{(depth+1)*'  '}- Left side is smaller, so inputs are in the right order")
            done = True
            current_right = True
            return True
        
        elif left > right:
            print(f"{(depth+1)*'  '}- Right side is smaller, so inputs are not in the right order")
            done = True
            return True
    
    elif type(left) == list and type(right) == list:
        len_left = len(left)
        len_right = len(right)
        longest_length = len_left if len_left > len_right else len_right
        
        for i in range(longest_length):
            try: tpm_left = left[i]
            except IndexError: tpm_left = None
            
            try: tmp_right = right[i]
            except IndexError: tmp_right = None
            
            if check_values(tpm_left, tmp_right, depth+1): return True
    
    # mixed case
    elif type(left) == int and type(right) == list:
        print(f"{(depth+1)*'  '}- Mixed types; convert left to [{left}] and retry comparison")
        check_values([left], right, depth+1)
        
    elif type(left) == list and type(right) == int:
        print(f"{(depth+1)*'  '}- Mixed types; convert right to [{right}] and retry comparison")
        check_values(left, [right], depth+1)
    
    return False
    

with open('input.txt','r') as fio:
    for n, line in enumerate(fio):
        set_number = n // 3
        
        if n % 3 == 0: first_line = line.strip()
        elif n % 3 == 1: second_line = line.strip()
        elif n % 3 == 2:       
            first_line = ast.literal_eval(first_line)
            second_line = ast.literal_eval(second_line)
            
            len_left = len(first_line)
            len_right = len(second_line)
            longest_length = len_left if len_left > len_right else len_right
        
            print(f"== Pair {set_number +1} ==")
            print(f"- Compare {first_line} vs {second_line}")
            
            for i in range(longest_length):
                try: left = first_line[i]
                except IndexError: left = None
                
                try: right = second_line[i]
                except IndexError: right = None
                
                if check_values(left, right): break
                
            print()
        
            if current_right == True:
                print(f"appending {set_number+1}")
                correct_indicies.append(set_number+1)
                current_right = False
            done = False

print(correct_indicies)
print(f"Answer: {sum(correct_indicies)}")