def soma(x, y):
    return x + y

def test_soma_benchmark(benchmark):
    """Teste de performance simples."""
    result = benchmark(soma, 10, 20)
    assert result == 30
