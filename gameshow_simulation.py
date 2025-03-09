# monty hall problem. still weird to think about.
# https://en.wikipedia.org/wiki/Monty_Hall_problem

import random

n = 1000  # total trials
num_doors = 3  # can only be >= 3
generated = [
    random.randint(0, num_doors - 1) for _ in range(n)
]  # number gives index of jackpot reward

num_wins_no_switch = 0
num_wins_with_switch = 0
for jackpot_i in generated:
    for i in range(num_doors):
        if i == jackpot_i:
            print("x", end="")
        else:
            print("-", end="")
    print()

    pick_one_i = random.randint(0, num_doors - 1)
    print(f"initial picked index: {pick_one_i}")

    can_reveal = [i for i in range(num_doors) if i != jackpot_i and i != pick_one_i]
    revealed_not_jackpot_i = random.randint(0, len(can_reveal) - 1)
    print(f"revealed index: {can_reveal[revealed_not_jackpot_i]}")
    print()

    # check initial
    initial_pick_result = pick_one_i == jackpot_i

    # check switched
    can_reveal.pop(revealed_not_jackpot_i)  # pop only revealed index
    if jackpot_i != pick_one_i:
        can_reveal.append(jackpot_i)  # adds back jackpot if is not initially picked
    switched_i = random.randint(0, len(can_reveal) - 1)
    print(f"switched index: {switched_i}")
    switch_pick_result = can_reveal[switched_i] == jackpot_i

    print("RESULTS!")
    print(f"NO SWITCH: {initial_pick_result}")
    print(f"SWITCH: {switch_pick_result}")

    if initial_pick_result:
        num_wins_no_switch += 1
    elif switch_pick_result:
        num_wins_with_switch += 1

    print("\n" + "=" * num_doors + "\n")


print(f"{n} TRIALS RESULTS!")
print(
    f"no switch success rate: {num_wins_no_switch / n}"
)  # converges to 0.333 for num_doors = 3
print(
    f"switch success rate: {num_wins_with_switch / n}\n"
)  # converges to 0.667 for num_doors = 3
