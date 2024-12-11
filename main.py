"""Ce module contient les fonctions pour la suite de Syracuse."""

from plotly.graph_objects import Scatter, Figure

def syr_plot(lsyr):
    """Affiche le graphe de la suite de Syracuse."""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text':"x"}},
            'yaxis': {'title': {'text':"y"}},
        }
    })

    x = list(range(len(lsyr)))  
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    

def syracuse_l(n):
    """Génère la liste des valeurs de la suite de Syracuse.

    Args:
        n (int): La source de la suite.

    Returns:
        list: La liste des valeurs de la suite de Syracuse.
    """
    l = [n]
    while n != 1:
        if n % 2 == 0:  # Si n est pair
            n //= 2
        else:  # Si n est impair
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol : correspond apparemment à la longueur totale de la liste."""
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude : nombre de termes consécutifs ≥ source."""
    source = l[0]
    altitude = 0
    for x in l:
        if x >= source:
            altitude += 1
        else:
            break
    return altitude

def altitude_maximale(l):
    """Retourne l'altitude maximale atteinte dans la liste de Syracuse.

    Args:
        l (list): La liste de Syracuse.

    Returns:
        int: L'altitude maximale atteinte.
    """
    return max(l)

def main():
    """Fonction principale qui vérifie le bon fonctionnement des fonctions secondaires."""
    # Exemple : Générer la suite de Syracuse pour n = 15
    n = 15
    lsyr = syracuse_l(n)
    syr_plot(lsyr)
    # Afficher les résultats
    print("Suite de Syracuse :", lsyr)
    print("Temps de vol :", temps_de_vol(lsyr))
    print("Temps de vol en altitude :", temps_de_vol_en_altitude(lsyr))
    print("Altitude maximale :", altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
