#!/usr/bin/python3

with open("input.txt", 'rb') as fio:
    for m, line in enumerate(fio):
        for n, char in enumerate(line):
            group = sorted(set(line[n:n+14]))
            if len(group) == 14:
                print(f"{n} {group}, should be {n+14}")
                exit()
