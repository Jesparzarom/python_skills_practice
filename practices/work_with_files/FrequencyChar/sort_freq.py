from freq import char_counter


def sort_frequency_values(chars_dict):
    # Reorder key-values
    sorted_dict = dict(
        sorted(chars_dict.items(), key=lambda key0_value1: key0_value1[1], reverse=True)
    )
    return sorted_dict


def to_hist(name, frequency):
    # Opening file to save changes with ".hist" extension.
    with open(name + ".hist", "w") as save:
        # Key, Values list
        to_list = [[key, str(value)] for key, value in frequency.items()]
        # Transforming Key, Value in strings with others char's.
        hist = "".join(i[0]+":"+i[1]+"\n" for i in to_list)
        # Saving changes
        save.write(hist)
    # Success
    return "¡Your new file is saved!"


try:
    # File to read and write
    filename = "example2"
    
    # returning a dict with frequency's from freq module
    chars_dict = char_counter(filename)
    
    # Reordering data, saving and printing
    frequency = sort_frequency_values(chars_dict)
    result = to_hist(filename, frequency)
    print(result)
    
except FileNotFoundError as e:
    print(e.__str__())
    