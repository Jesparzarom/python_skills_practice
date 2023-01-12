def is_palindrome1(text) -> str:
    return (
        "Es palíndromo" 
        if text[::-1].replace(" ", "") == text.replace(" ", "") 
        else "No es palíndromo"
        )


def is_palindrome2(text) -> str:
    fow = list(text)
    if not text.isalpha():
        fow = [char for char in fow if char != " "]
    rev = list(reversed(fow))
    return "Es palíndromo" if fow == rev else "No es palíndromo"


def is_palindrome3(text) -> str:
    text = text.replace(" ", "")
    ctrl = -1
    for index, char in enumerate(text):
        if text[index] == text[ctrl]:
            ctrl -= 1
            return "Es palíndromo"
        else:
            return "No es palíndromo"
        
        
try:
    text = input("Igresa un texto para comprobar si es palíndromo: ").lower()
    #Algorithm one
    print(is_palindrome1(text))
    #Algorithm two
    print(is_palindrome2(text))
    #Algorithm three
    print(is_palindrome3(text))
except ValueError as Error:
    print("Error: solo se admiten palabras separadas o no por un espacio")
