# Simple Finders
def simple_word_finder(string, find):
    return "Palabra encontrada" if find in string else "Palabra no encontrada"


def simple_word_finder_plus(string, find):
    start = string.find(find)
    stop = string.find(find) + len(find) + 1

    return (
        f"palabra encontrada en índices del {start} al {stop-1}"
        if start != -1
        else "Sin resultados"
    )


# Semi-Complex finder
def hidden_word_finder(words_soup, hidden_word):
    words_soup, hidden_word = words_soup.lower(), hidden_word.lower()
    find = words_soup[
        words_soup.find(hidden_word[0]) : words_soup.find(hidden_word[-1]) + 1
    ]
    confirm = "".join([char for char in hidden_word if char in find])

    return f"{hidden_word} Si está" if hidden_word == confirm else "Sin resultados"


"""The name of the main functions indicates whether 
it calls the simple or hidden words search engine"""
def not_hidden_wrd(string, find):
    # string = input("Texto: ").replace(" ", "")
    # find = input(f"Palabra a buscar en {string}: ").replace(" ", "")
    string = string.replace(" ", "")
    find = find.replace(" ", "")
    # return simple_word_finder(string, find)
    return simple_word_finder_plus(string, find)


def hidden_word(word_soup, hidden):
    # words_soup = "Nabucodonosor"
    # hidden = "nar"

    return hidden_word_finder(word_soup, hidden)


# TESTS
print("==============SIMPLE TEST==================")
string = ["hello world", "hello friend", "python is cool"]
find = ["low", "low", "onis"]
for test in range(3):
    print(not_hidden_wrd(string[test], find[test]))


print("============HIDDEN WORDS TEST==============")
words_soups = ["pefkejew", "pefeikihhn", "pbfomsms"]
hidden = ["peace", "pekin", "boss"]
for test2 in range(3):
    print(hidden_word(words_soups[test2], hidden[test2]))
