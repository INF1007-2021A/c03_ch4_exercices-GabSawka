#!/usr/bin/env python
# -*- coding: utf-8 -*-


from unittest.signals import removeResult


def is_even_len(string: str) -> bool:
    return len(string) % 2 == 0


def remove_third_char(string: str) -> str:
    if(len(string)>=3):
        new_string =""
        for i in range(len(string)):
            if i != 3:
                new_string+=string[i]
        return new_string
    else:
        return string
        
def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string =""
    for letter in string:
        if letter == old_char:
            new_string+=new_char
        else:
            new_string+=letter
    return new_string


def get_nb_char(string: str, char: str) -> int:
    char_appearance=0
    for letter in string:
        if letter == char:
            char_appearance+=1
    return char_appearance


def get_nb_words(sentence: str) -> int:
    if len(sentence)==0:
        return 0
    nb_words=1
    for letter in sentence:
        if letter == ' ':
            nb_words+=1
    return nb_words


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")
    string = "hello"
    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
