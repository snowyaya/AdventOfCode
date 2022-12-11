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

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    blocks = f.read().strip().split("\n\n")

start_items = {}
operation = {}
div_test = {}
div_test_true = {}
div_test_false = {}
n_handle_items = {}

m_number = 0
modd = 1
for monkey in blocks:
    monkey_data = monkey.split("\n")
    n_handle_items[m_number] = 0
    for mdata in monkey_data:
        if 'Operation' in mdata:
            operation[m_number] = mdata[23:]
        elif 'Starting' in mdata:
            start_items[m_number] = re.findall(r'\d+', mdata)
        elif 'Test' in mdata:
            div_test[m_number] = int(re.findall(r'\d+', mdata)[0])
        elif 'true' in mdata:
            div_test_true[m_number] = int(re.findall(r'\d+', mdata)[0])
        elif 'false' in mdata:
            div_test_false[m_number] = int(re.findall(r'\d+', mdata)[0])
    modd *= div_test[m_number]     
    m_number += 1
    

n_round = 10000
live_items = start_items
for i in range(n_round):
    for m in range(m_number):
        worry_op = operation[m]
        div_test_val = div_test[m]
        div_test_true_val = div_test_true[m]
        div_test_false_val = div_test_false[m]
        for t in live_items[m]:
            if '+' in worry_op and 'old' not in worry_op:
                t_new = int(t) + int(re.findall(r'\d+', worry_op)[0])
            elif '+' in worry_op and 'old' in worry_op:
                t_new = int(t) * 2
            elif '*' in worry_op and 'old' not in worry_op:
                t_new = int(t) * int(re.findall(r'\d+', worry_op)[0])
            elif '*' in worry_op and 'old' in worry_op:
                t_new = int(t) ** 2
            # t_new //= 3
            t_new %= modd 
            if t_new % div_test_val == 0:
                live_items[div_test_true_val].append(t_new)
            else:
                live_items[div_test_false_val].append(t_new)
            # print("live_items", live_items)
            n_handle_items[m] += len(live_items[m])
            live_items[m] = []
# print("n_handle_items", n_handle_items)
  
n_handles = list(n_handle_items.values())
print(n_handles)
n1 = max(n_handles)
n_handles.remove(n1)
n2 = max(n_handles)
monkey_business = n1 * n2
print("Part 1: ", monkey_business)
        