
from src.ejercicio7 import abecedario, eliminar_posiciones_multiplos_de_tres

def test_eliminar_posiciones_multiplos_de_tres():
    assert eliminar_posiciones_multiplos_de_tres(abecedario) == "a, b, d, e, g, h, j, k, n, m, o, p, r, s, u, v, x, y,"