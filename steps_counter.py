import math


def count_steps():
    length = locale.atof(distance)
    step = locale.atof(length_step)
    num_steps = math.ceil(length // step)
    return num_steps


distance = float(input("Please write the distance walked in meters: "))
length_step = float(input("Please put the length of your step in meters: "))

print(f"You walked {distance} in {count_steps()} steps.")