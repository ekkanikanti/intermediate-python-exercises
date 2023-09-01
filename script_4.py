sum = 0
i = 0
while i < 5:
    try:
        number = int(input('Enter int #' + str(i+1) + ": "))
    except ValueError:
        print('Invalid input. Please enter an int.')
        i -= 1
        sum -= number
    sum += number
    i += 1

print(f"Your sum is {sum}")
# https://realpython.com/python-input-integer/