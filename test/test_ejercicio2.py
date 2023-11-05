
from src.ejercicio2 import Yo_Estudio_X

def test_Yo_Estudio_X():
    assert Yo_Estudio_X(["Matemáticas", "Física", "Química", "Historia", "Lengua"], []) == "Yo estudio Matemáticas\nYo estudio Física\nYo estudio Química\nYo estudio Historia\nYo estudio Lengua"