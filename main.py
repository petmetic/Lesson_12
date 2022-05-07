def calculate_sum():
    new_x = []
    new_y = []
    for num in x:
        num.split()
        new_x = num.replace(",", ".")
    for num in y:
        num.split()
        new_y = num.replace(",", ".")

    result = float(new_x) + float(new_y)
    return result


x = input("Please write number: ")
y = input("Please write number: ")

print(f"The result of your numbers is: {calculate_sum()}")
