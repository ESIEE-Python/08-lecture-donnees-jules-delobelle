"Un module permettant de lire et manipuler les données d'un csv"

#### Imports et définition des variables globales

# Importation du module `csv` pour lire et écrire des fichiers CSV
# Importation du module `random` (bien que non utilisé ici, pourrait être utile pour des ajouts
# futurs)
import csv

# Définition d'une variable globale contenant le nom du fichier CSV à lire
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    Lit le contenu du fichier CSV spécifié et convertit chaque élément en un entier.
    Les lignes du fichier sont interprétées comme des listes d'entiers séparés par 
    des points-virgules.

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: une liste de listes contenant les données converties en entiers
    """
    with open(filename, "r", encoding="utf-8") as file:
        # Utilisation de `csv.reader` pour lire le fichier avec `;` comme délimiteur
        # Conversion de chaque élément en entier
        return [[int(chiffre) for chiffre in sous_liste]
                for sous_liste in list(csv.reader(file, delimiter=";"))]

def get_list_k(data, k):
    """
    Récupère la k-ième liste de données.

    Args:
        data (list): liste principale contenant des sous-listes
        k (int): index de la liste à récupérer

    Returns:
        list: la k-ième liste de `data`
    """
    return data[k]

def get_first(l):
    """
    Récupère le premier élément d'une liste.

    Args:
        l (list): liste dont on veut le premier élément

    Returns:
        any: le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """
    Récupère le dernier élément d'une liste.

    Args:
        l (list): liste dont on veut le dernier élément

    Returns:
        any: le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """
    Trouve le plus grand élément dans une liste.

    Args:
        l (list): liste d'éléments

    Returns:
        any: le plus grand élément de la liste
    """
    return max(l)

def get_min(l):
    """
    Trouve le plus petit élément dans une liste.

    Args:
        l (list): liste d'éléments

    Returns:
        any: le plus petit élément de la liste
    """
    return min(l)

def get_sum(l):
    """
    Calcule la somme des éléments dans une liste.

    Args:
        l (list): liste d'éléments numériques

    Returns:
        int/float: somme des éléments de la liste
    """
    return sum(l)


#### Fonction principale

def main():
    """
    Fonction principale du programme.
    - Lit les données à partir du fichier CSV spécifié par `FILENAME`.
    - Affiche chaque liste de données avec son index.
    - Récupère et affiche une liste spécifique basée sur l'index défini dans `k`.
    """
    # Lecture des données du fichier CSV
    data = read_data(FILENAME)

    # Affichage de chaque sous-liste avec son index
    for i, l in enumerate(data):
        print(i, l)

    # Index de la liste que l'on veut afficher
    k = 37
    # Affichage de la k-ième liste de données
    print(k, get_list_k(data, 37))


# Point d'entrée du programme
if __name__ == "__main__":
    # Exécution de la fonction principale si le fichier est exécuté directement
    main()
