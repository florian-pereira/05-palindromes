"""
Ce module permet de vérifier si une chaîne de caractères est un palindrome.

Un palindrome est une chaîne qui se lit de la même façon de gauche à droite et de droite à gauche,
en ignorant les accents, les espaces, la ponctuation et les différences de casse.
Le module contient une fonction `ispalindrome` et un point d'entrée principal `main` 
pour tester plusieurs cas.
"""

import string


def ispalindrome(s):
    """
    Vérifie si une chaîne de caractères est un palindrome.

    Un palindrome est un mot ou une phrase qui se lit de la même manière 
    de gauche à droite et de droite à gauche, en ignorant les accents, 
    les espaces, la ponctuation et les majuscules/minuscules.

    La fonction effectue les étapes suivantes :
    1. Crée une table de correspondance pour transformer les lettres accentuées 
       en lettres non accentuées (par exemple, é devient e, à devient a, etc.).
    2. Remplace les lettres accentuées par des lettres sans accent dans `s` et 
       met toutes les lettres en minuscules pour ignorer les différences de casse.
    3. Supprime les caractères non alphanumériques comme la ponctuation et les espaces.
    4. Compare la chaîne de caractères avec sa version inversée pour vérifier 
       si elle est identique dans les deux sens.

    Paramètres :
    ----------
    s : str
        La chaîne de caractères à vérifier.

    Retourne :
    -------
    bool
        Renvoie True si `s` est un palindrome, sinon False.
    """
    accents = "áàâäãåéèêëíìîïóòôöõúùûüñç"
    sans_accents = "aaaaaaeeeeiiiiooooouuuunc"
    caracteres_a_supprimer = string.punctuation + " "
    table = str.maketrans(
        accents + accents.upper(),
        sans_accents + sans_accents.upper(),
        caracteres_a_supprimer,
    )
    s = s.translate(table).lower()
    return s == s[::-1]


def main():
    """
    Fonction principale qui teste la fonction ispalindrome() avec différents exemples.

    Cette fonction appelle ispalindrome() pour plusieurs chaînes de caractères 
    et affiche le résultat pour chacun, indiquant si la chaîne est un palindrome ou non.
    """
    exemples = [
        "radar",
        "kayak",
        "level",
        "rotor",
        "civique",
        "deifie",
        "Élu par cet acte, crapule",
        "A man, a plan, a canal: Panama",
        "Bonjo  urrUOJ NOB",
    ]
    for s in exemples:
        print(f"'{s}' : {ispalindrome(s)}")


if __name__ == "__main__":
    main()
