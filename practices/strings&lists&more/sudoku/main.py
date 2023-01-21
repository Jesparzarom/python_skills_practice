# Transform input data to: list(list(row))
def order_data():
    with open("sudoku.txt") as f:
        lst = [
            list(line) if line.isnumeric() and "0" not in line else None
            for line in f.read().strip("\n").split("\n")
        ]
    return lst if None not in lst else None


# Check if numbers are unique
def unique_numbers(nums):
    return len(nums) == len(set(nums))


# Check if all rows and columns are correct
def check_col_row(num_list):
    columns = all(unique_numbers(col) for col in zip(*num_list))
    rows = all(unique_numbers(row) for row in num_list)
    return columns and rows  # True or False


# Check unique numbers in all quadrants
def check_quadrants(num_list):
    for rws in range(0, 9, 3):
        for cmns in range(0, 9, 3):            
            # Getting 3 x 3 quadrant values.
            quadrant = [
                val 
                for row in num_list[rws : rws + 3] 
                for val in row[cmns : cmns + 3]
            ]
            
            if len(set(quadrant)) != len(quadrant):
                return False
    return True


# Main: Sudoku checker
def sudoku_checker(lst):
    if check_col_row(lst) is True and check_quadrants(lst) is True:
        print("\nYes\n")
    else:
        print("\nNo\n")

# Test
try:
    numbers = order_data()
    sudoku_checker(numbers)
except TypeError:
    print("\nERROR IN INPUT DATA\n")
