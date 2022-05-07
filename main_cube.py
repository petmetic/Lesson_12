def calculate_cube():
    new_x = []
    for num in x:
        num.split()
        new_x = num.replace(",", ".")
    result = float(new_x) ** 3
    return result


x = input("Please write number: ")

print(f"The result of your numbers is: {calculate_cube()}")
