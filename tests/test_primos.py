"""Pruebas unitarias para el módulo de números primos."""

import pytest
from app.primos import es_primo, generar_primos

@pytest.fixture(name="primos_conocidos")
def fixture_primos_conocidos():
    return [2, 3, 5, 7, 11, 13, 17, 19]

def test_generar_primos(primos_conocidos):
    assert generar_primos(10) == primos_conocidos[:4]
    assert generar_primos(2) == primos_conocidos[:1]
    assert generar_primos(1) == []
    assert generar_primos(20) == primos_conocidos