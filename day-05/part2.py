#!/usr/bin/python3

"""
[T]     [D]         [L]            
[R]     [S] [G]     [P]         [H]
[G]     [H] [W]     [R] [L]     [P]
[W]     [G] [F] [H] [S] [M]     [L]
[Q]     [V] [B] [J] [H] [N] [R] [N]
[M] [R] [R] [P] [M] [T] [H] [Q] [C]
[F] [F] [Z] [H] [S] [Z] [T] [D] [S]
[P] [H] [P] [Q] [P] [M] [P] [F] [D]
 0   1   2   3   4   5   6   7   8 
"""

stacks = [ [] for i in range(9)]

stacks[0] = ['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T']
stacks[1] = ['H', 'F', 'R']
stacks[2] = ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D']
stacks[3] = ['Q', 'H', 'P', 'B', 'F', 'W', 'G']
stacks[4] = ['P', 'S', 'M', 'J', 'H']
stacks[5] = ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L']
stacks[6] = ['P', 'T', 'H', 'N', 'M', 'L']
stacks[7] = ['F', 'D', 'Q', 'R']
stacks[8] = ['D', 'S', 'C', 'N', 'L', 'P', 'H']


def rearrange(source_stack:list, destination_stack:list, quantity:int) -> tuple:
    # remove crates from source stack
    new_from_stack = source_stack[0:-quantity]
    
    # add crates to destination stack, importantly inverted
    new_to_stack = destination_stack + source_stack[-quantity:]
    
    return new_from_stack, new_to_stack


with open("input-modified.txt","r") as fio:

    for n,line in enumerate(fio):
        line_split = line.strip().split(" ")
        
        quantity = int(line_split[1])
        src_stack_id = int(line_split[3])-1
        dst_stack_id = int(line_split[5])-1
        
        new_src_stack, new_dst_stack = rearrange(
            stacks[src_stack_id], 
            stacks[dst_stack_id],
            quantity
        )
        
        stacks[src_stack_id] = new_src_stack
        stacks[dst_stack_id] = new_dst_stack

print(''.join([stack[-1:][0] for stack in stacks]))