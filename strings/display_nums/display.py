def patterns():
    yes, no = "#", " "
    yyy, nny, ynn, yny = yes * 3, no+no+yes, yes+no+no, yes+no+yes
    return (yyy, nny, ynn, yny)


def numbers_patterns(yyy, nny, ynn, yny):
    # List index is the number to show in displayplay
    # Index 0 to 9 is the number in displayplay (0 to 9)
    numbers = [
        [yyy, yny, yny, yny, yyy],
        [nny, nny, nny, nny, nny],
        [yyy, nny, yyy, ynn, yyy],
        [yyy, nny, yyy, nny, yyy],
        [yny, yny, yyy, nny, nny],
        [yyy, ynn, yyy, nny, yyy],
        [yyy, ynn, yyy, yny, yyy],
        [yyy, nny, nny, nny, nny],
        [yyy, yny, yyy, yny, yyy],
        [yyy, yny, yyy, nny, yyy],
    ]
    return numbers


def display(numbers, *lst):
    for row in range(5):
        for number in lst:
            print(numbers[number][row], end=" ")
        print()


while True:
    try:
        # Input
        inn = [
            int(n)
            for n in list(
                input("\nType numbers and press enter or\nPress [empty] enter to exit >")
            )
            if int(n) >= 0
        ]
        if inn == []:
            break

        # Results
        display(numbers_patterns(*patterns()), *inn)

    except ValueError:
        print("Error: Input not valid. Try again")
