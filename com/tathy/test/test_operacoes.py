def func(x):
	return x + 5

def test_zero():
	assert func(-4) == 1

def test_positivo():
	assert func(-1) == 4

def test_negativo():
	assert func(-6) == -1