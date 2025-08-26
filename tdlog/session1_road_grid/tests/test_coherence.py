from tdlog.session1_road_grid.src.coherence import random_coherent_grid, is_coherent
from tdlog.session1_road_grid.src.display import render_grid


def test_random_coherent_grid_small():
    # Générer une petite grille cohérente
    g = random_coherent_grid(3, 3, prob=0.7)

    # Vérifier que la grille est bien cohérente
    assert is_coherent(g)

    # Rendu ASCII pour inspection visuelle
    s = render_grid(g, p=2, q=1, r=2, s=1)
    print("\nGrille 3x3 cohérente :")
    print(s)

    # Vérifier que toutes les lignes ont la même longueur
    lines = s.splitlines()
    width = len(lines[0])
    assert all(len(line) == width for line in lines)
