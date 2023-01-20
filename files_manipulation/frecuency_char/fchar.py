def char_counter(file_name):
    # Opening and reading text file
    with open("./" + file_name + ".txt") as f:
        stream = f.read()
    
    # Dict whit character repetition's count: Key=char, Value=count
    chars_dict = {key: stream.count(key) for key in stream}
    return chars_dict

try:
    filename = input("text filename ► ")
    for key, value in char_counter(filename).items():
        print(key, "->", value)
        
except FileNotFoundError as e:
    print(e._str())
    