import pytest
import arreglo as ar

array = [5,3,4,2,1]
diccionario = [{"nombre":"Carlos","edad":23},{"nombre":"Joel","edad":15},{"nombre":"Oscar","edad":43}]

def test_arreglo():
    assert ar.acomodo(array) == [1,2,3,4,5]

def test_contar_mayores():
    assert ar.contar_mayores(diccionario) == 2
