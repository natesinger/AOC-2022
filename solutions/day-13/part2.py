#!/usr/bin/python3
import ast

current_right = False
correct_indicies = []

done = False

output = []

def check_values(left, right, depth:int=1):
    global current_right, done
    
    if done: return False
    
    if left == None:
        current_right = True
        done = True
        return True
    elif right == None:
        done = True
        return True
        
    elif type(left) == int and type(right) == int:
        if left < right:
            done = True
            current_right = True
            return True
        
        elif left > right:
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
        check_values([left], right, depth+1)
        
    elif type(left) == list and type(right) == int:
        check_values(left, [right], depth+1)
    
    return False
    

with open('test-data-modified.txt','r') as fio:
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
            
            for i in range(longest_length):
                try: left = first_line[i]
                except IndexError: left = None
                
                try: right = second_line[i]
                except IndexError: right = None
                
                if check_values(left, right): break
                
        
            if current_right == True:
                correct_indicies.append(set_number+1)
                current_right = False
                
                output.append(first_line)
                output.append(second_line)
            else:
                output.append(second_line)
                output.append(first_line)
            done = False


for line_pos in range(len(output)):
    first_line = output[line_pos]
    second_line = output[line_pos+1]
    
    check_values(first_line, second_line)
    print(current_right)
    current_right = False
    #exit()
    
    

"""
for run in range(5):
    input = output
    output = []
    
    for n in range(len(input)):
        try:
            first_line = input[n]
            second_line = input[n+1] 
        except IndexError: exit()
            
        len_left = len(first_line)
        len_right = len(second_line)
        longest_length = len_left if len_left > len_right else len_right
        
        for i in range(longest_length):
            try: left = first_line[i]
            except IndexError: left = None
            
            try: right = second_line[i]
            except IndexError: right = None
            
            if check_values(left, right): break
            
    
        if current_right == True:
            current_right = False
            
            output.append(first_line)
            output.append(second_line)
        else:
            output.append(second_line)
            output.append(first_line)
    

for l in output: print(l)
print()        
    
"""

