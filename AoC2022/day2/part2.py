'''
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
'''

import os
import sys
from itertools import groupby

score_dict = {"rock": 1, "paper": 2, "scissors": 3}
round_outcome = {"lost": 0, "draw": 3, "won": 6}
elf_dict = {"A": "rock", "B": "paper", "C": "scissors"}
my_dict = {"X": "lost", "Y": "draw", "Z": "won"}

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    
new_lines = [x.replace('\n', '') for x in lines]

#split each string in new_lines by space
strategy_guide = [x.split(' ') for x in new_lines]

def get_my_strategy_score(expect_outcome, elf):
    if expect_outcome == "won":
        if elf_dict[elf] == "rock":
            return "paper"
        elif elf_dict[elf] == "paper":
            return "scissors"
        elif elf_dict[elf] == "scissors":
            return "rock"
        
    elif expect_outcome == "draw":
        return elf_dict[elf]
    
    elif expect_outcome == "lost":
        if elf_dict[elf] == "rock":
            return "scissors"
        elif elf_dict[elf] == "paper":
            return "rock"
        elif elf_dict[elf] == "scissors":
            return "paper"

final_score = 0 
for strategy in strategy_guide:
    elf = strategy[0]
    round_ = strategy[1]
    print("elf: ", elf, "round: ", round_)
    print(my_dict[round_], " ", get_my_strategy_score(my_dict[round_], elf))
    print(score_dict[get_my_strategy_score(my_dict[round_], elf)], " ", round_outcome[my_dict[round_]])
    final_score += score_dict[get_my_strategy_score(my_dict[round_], elf)] + round_outcome[my_dict[round_]]

print(final_score)