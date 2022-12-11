'''
1. Monkey inspects the first item
2. Get the worry level
3. Worry level divided by 3
4. Test-> go to next monkey
5. Repeat until all items are inspected
'''
import sys
import os 
import re

with open(os.path.join(sys.path[0], "input0.txt"), "r") as f:
    blocks = f.read().strip().split("\n\n")

'''
monkeys_info = [{
    "id": 0,
    "items": [79, 98],
    "operation": ["multiply", "19"],
    "test": ["divide", "13"],
    "true": 2,
    "false": 3
}]
'''
monkeys_info = []

for block in blocks:
    lines = block.split("\n")
    # print(lines)
    monkey_dict = {
        "id": -1,
        "items": [],
        "operation": [],
        "test": [],
        "true": -1,
        "false": -1,
        "inspect_times": 0
    }
    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            monkey_dict["id"] = re.findall(r"\d+", line)[0]
            
        elif line.startswith("Starting items:"):
            monkey_dict["items"]= [int(i) for i in re.findall(r"\d+", line)]

        elif line.startswith("Operation:"):
            monkey_dict["operation"] = line.split(":")[1].strip().split(" ")[-2:]

        elif line.startswith("Test:"):
            monkey_dict["test"] = line.split(":")[1].strip().split(" ")[-1:]
            
        elif line.startswith("If true:"):
            monkey_dict["true"] = int(re.findall(r"\d+", line)[0])
        
        elif line.startswith("If false:"):
            monkey_dict["false"] = int(re.findall(r"\d+", line)[0])
    # print(monkey_dict)
    monkeys_info.append(monkey_dict)
# print(monkeys_info)

operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}

def play(curr_monkey):
    id_ = curr_monkey["id"]
    items = curr_monkey["items"]
    test = int(curr_monkey["test"][0])
    for i_ in range(len(items)):
        item = items.pop(0)
        if curr_monkey["operation"][1] == "old":
            another_item = item
        else:
            another_item = int(curr_monkey["operation"][1])
        worry_level = operations[curr_monkey["operation"][0]](item, another_item)
        # print("new_worry_level", worry_level)
        
        # curr_worry_level = worry_level // 3
        if worry_level % test == 0:
            to_money = curr_monkey["true"]
        else:
            to_money = curr_monkey["false"]
        monkeys_info[to_money]["items"].append(worry_level)
        curr_monkey["inspect_times"] += 1

print("🐒 Before playing: ")
for info in monkeys_info:
    print(info)

round_ = 1
while round_ <= 10000:
    # print(f"🟢 Round {round_}")
    for monkey in monkeys_info:
        play(monkey)
    # print("✅ After round:", round_)
    # for info in monkeys_info:
    #     print(info)
    round_ += 1
print("🟪 Rounds all played:")
times = []
for info in monkeys_info:
    times.append(info["inspect_times"])
    # print(info)
print("Part 2:", sorted(times)[-1] * sorted(times)[-2])   