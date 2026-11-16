import pytest

from calculadora import somar
from calculadora import subtrair
from calculadora import multiplicar
from calculadora import dividir

def test_somar():
	assert somar(10,5) == 15

def test_subtrair():
	assert subtrair(10,5) == 5

def test_multiplicar():
	assert multiplicar(10,5) == 50

def test_dividir():
	assert dividir(10,2) == 5

def test_divisao_por_zero():
	with pytest.raises(ValueError):
		dividir(10,0)
