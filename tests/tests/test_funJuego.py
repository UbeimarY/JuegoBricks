import pytest
from src.funJuego import iniciar_juego, mover_personaje, finalizar_juego

def test_iniciar_juego(capsys):
    iniciar_juego()
    captured = capsys.readouterr()
    assert "¡Iniciando juego!!!" in captured.out

def test_mover_personaje(capsys):
    mover_personaje("izquierda")
    captured = capsys.readouterr()
    assert "Moviendo personaje hacia izquierda" in captured.out

def test_finalizar_juego(capsys):
    finalizar_juego()
    captured = capsys.readouterr()
    assert "¡Fin del juego!!" in captured.out
