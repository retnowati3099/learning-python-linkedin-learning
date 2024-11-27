def main():
    x = 0

    # TODO: define a while loop
    while(x < 5):
        print(x)
        x = x + 1

    # TODO: define a for loop
    for x in range(5, 10):
        print(x)

    # TODO: use a for loop over a colleaction
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # TODO: use the break and continue statements
    for x in range(5, 10):
        if x == 7:
            break
        print(x)

    for x in range(5, 10):
        if x % 2 == 0:
            continue
        print(x)

    # TODO: using the enumerate() function to get index
    rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    for index, value in enumerate(rainbow_colors):
        print(index, value)

if __name__ == "__main__":
    main()