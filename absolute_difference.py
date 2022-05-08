def absolute_num():
    new_x = []
    new_y = []
    for num in x:
        num.split()
        new_x = num.replace(",", ".")
    for num in y:
        num.split()
        new_y = num.replace(",", ".")
    dif = abs(float(new_x) - float(new_y))
    return dif


x = input("Please write number: ")
y = input("Please write number: ")
print(f"The absolute difference between number {x} and {y} is {absolute_num()}")
