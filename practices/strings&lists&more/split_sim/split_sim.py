# split() metod simulator
def my_split(string="", separator=" "):

    # Output list, control-variable, modify end of string
    output, ctrl = [], ""
    string += str(separator)

    # Splitting the text
    for letter in string:
        if letter == separator:
            output.append(ctrl)
            ctrl = ""
        if "" in output:
            output.pop()
        if letter != separator:
            ctrl += letter

    # Result to list.
    return output
