import math


def count_steps():
    # code to change "," to "." goes here
    num_steps = math.ceil(distance // length_step)
    return num_steps


distance = float(input("Please write the distance walked in meters: "))
length_step = float(input("Please put the length of your step in meters: "))

print(f"You walked {distance} in {count_steps()} steps.")