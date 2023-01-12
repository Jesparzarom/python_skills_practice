def reorder(word):
    return sorted(list(word.lower().replace(" ", "")))


def is_anagram(wordA, wordB):
    word1, word2 = reorder(wordA), reorder(wordB)
    return (
        "Its anagram" 
        if (word1 == word2) and ([] not in (word1, word2)) 
        else "Is not an anagram"
        )


print("anagram check".upper())
wordA, wordB = input("Word one: "), input("Word two: ")
print(is_anagram(wordA, wordB))
print(is_anagram("modern", "norman"))