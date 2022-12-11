#!/usr/bin/python3
import re, math

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ''
        self.test_div_int = None
        self.true_target = -1
        self.false_target = -1
        self.inspected = 0
    
    def evaluate_operation(self, item):
        formatted = self.operation.replace('old',str(item))
        return eval(formatted)

monkeys = []

with open("input.txt", "r") as fio:
    for n,line in enumerate(fio):
        line = line.strip()
        
        # new monkey
        if n % 7 == 0:
            current_monkey = n // 7
            monkeys.append(Monkey())
        
        # starting items
        elif n % 7 == 1:
            current_monkey = n // 7
            monkeys[current_monkey].items = [int(i.strip()) for i in line.split(':')[1].strip().split(',')] or []

        # operation
        elif n % 7 == 2:
            current_monkey = n // 7
            monkeys[current_monkey].operation = re.findall(r"old.*", line)[0]

        # test div int
        elif n % 7 == 3:
            current_monkey = n // 7
            monkeys[current_monkey].test_div_int = re.findall(r"[0-9]{1,2}", line)[0]

        # test true
        elif n % 7 == 4:
            current_monkey = n // 7
            monkeys[current_monkey].true_target = int(re.findall(r"[0-9]", line)[0])
            
        # test false
        elif n % 7 == 5:
            current_monkey = n // 7
            monkeys[current_monkey].false_target = int(re.findall(r"[0-9]", line)[0])


modulo_for_later = 1
for monkey in monkeys:
    modulo_for_later *= int(monkey.test_div_int)
    
    print(modulo_for_later)
    

ROUNDS = 10_000
for round in range(ROUNDS):
    for n,monkey in enumerate(monkeys):
        
        for item in monkeys[n].items:
            monkey.inspected += 1
            worry_level = monkey.evaluate_operation(item)
            
            worry_level %= modulo_for_later
            
            if worry_level % int(monkey.test_div_int) == 0:
                monkeys[n].items = monkeys[n].items[1:]
                monkeys[monkey.true_target].items.append(worry_level)

            else:
                monkeys[n].items = monkeys[n].items[1:]
                monkeys[monkey.false_target].items.append(worry_level)
                
    if round % 1000 == 999:
        inspected_totals = []
        for n,monkey in enumerate(monkeys):
            inspected_totals.append(monkey.inspected)
            print(f"Monkey {n} inspected items {monkey.inspected} times.")
            
        print()

print(sorted(set(inspected_totals))[-2:][0] * sorted(set(inspected_totals))[-2:][1])