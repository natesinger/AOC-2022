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
            print(f"{n} {current_monkey} [{line}]")
            monkeys.append(Monkey())
        
        # starting items
        elif n % 7 == 1:
            current_monkey = n // 7
            monkeys[current_monkey].items = [int(i.strip()) for i in line.split(':')[1].strip().split(',')] or []
            
            print(f"items {current_monkey}: {monkeys[current_monkey].items}")

        # operation
        elif n % 7 == 2:
            current_monkey = n // 7
            monkeys[current_monkey].operation = re.findall(r"old.*", line)[0]
            
            print(f"operation {current_monkey}: {monkeys[current_monkey].operation}")
            
        # test div int
        elif n % 7 == 3:
            current_monkey = n // 7
            monkeys[current_monkey].test_div_int = re.findall(r"[0-9]{1,2}", line)[0]
            
            print(f"div int {current_monkey}: {monkeys[current_monkey].test_div_int}")
        
        # test true
        elif n % 7 == 4:
            current_monkey = n // 7
            monkeys[current_monkey].true_target = int(re.findall(r"[0-9]", line)[0])
            
            print(f"true target {current_monkey}: {monkeys[current_monkey].true_target}")
        
        # test false
        elif n % 7 == 5:
            current_monkey = n // 7
            monkeys[current_monkey].false_target = int(re.findall(r"[0-9]", line)[0])
            
            print(f"false target {current_monkey}: {monkeys[current_monkey].false_target}")

ROUNDS = 20
for round in range(ROUNDS):
    for n,monkey in enumerate(monkeys):
        print(f"Monkey {n}:")
        for item in monkeys[n].items:
            monkey.inspected += 1
            print(f"  Monkey inspects an item with a worry level of {item}.")
            
            worry_level = monkey.evaluate_operation(item)
            print(f"    Worry level is {monkey.operation} to {worry_level}.")
            
            worry_level = math.floor(worry_level/3)
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")
                    
            if worry_level % int(monkey.test_div_int) == 0:
                print(f"    Current worry level is divisible by {monkey.test_div_int}.")
                
                monkeys[n].items = monkeys[n].items[1:]
                monkeys[monkey.true_target].items.append(worry_level)
                print(f"    Item with worry level {worry_level} is thrown to monkey {monkey.true_target}.")

            else:
                print(f"    Current worry level is not divisible by {monkey.test_div_int}.")

                monkeys[n].items = monkeys[n].items[1:]
                monkeys[monkey.false_target].items.append(worry_level)
                print(f"    Item with worry level {worry_level} is thrown to monkey {monkey.false_target}.")
            
    for monkey in monkeys:
        print(monkey.items)

inspected_totals = []
for n,monkey in enumerate(monkeys):
    inspected_totals.append(monkey.inspected)
    print(f"Monkey {n} inspected items {monkey.inspected} times.")

print(sorted(set(inspected_totals))[-2:][0] * sorted(set(inspected_totals))[-2:][1])