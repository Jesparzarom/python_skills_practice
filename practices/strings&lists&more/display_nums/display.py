# Defining the values for the number pattern
def patterns():
    yes, no = "#", " "
    yyy, nny, ynn, yny = yes * 3, no+no+yes, yes+no+no, yes+no+yes
    return (yyy, nny, ynn, yny)


def numbers_patterns(yyy, nny, ynn, yny):
    # List index is the number to show in displayplay
    # Index 0 to 9 is the number in displayplay (0 to 9)
    numbers = [
        [yyy, yny, yny, yny, yyy], # num 0 pattern
        [nny, nny, nny, nny, nny], # num 1 pattern
        [yyy, nny, yyy, ynn, yyy], # num 2 pattern
        [yyy, nny, yyy, nny, yyy], # num 3 pattern
        [yny, yny, yyy, nny, nny], # num 4 pattern
        [yyy, ynn, yyy, nny, yyy], # num 5 pattern 
        [yyy, ynn, yyy, yny, yyy], # num 6 pattern
        [yyy, nny, nny, nny, nny], # num 7 pattern
        [yyy, yny, yyy, yny, yyy], # num 8 pattern
        [yyy, yny, yyy, nny, yyy], # num 9 pattern
    ]
    return numbers

# Print the patterns of numbers given in display.
def display(numbers, *lst):
    for row in range(5):
        for number in lst:
            print(numbers[number][row], end=" ")
        print()


# Test program
while True:
    try:
        # Input list whit numbers to transform in display.
        # In this case, input must be greater than 0
        inn = [
            int(n)
            for n in list(
                input("\nType numbers and press enter or\nPress [empty] enter to exit >")
            )
            if int(n) >= 0
        ]
        if inn == []: # If input is empty, break program.
            break

        # Results
        display(numbers_patterns(*patterns()), *inn)

    except ValueError:
        print("Error: Input not valid. Try again")
