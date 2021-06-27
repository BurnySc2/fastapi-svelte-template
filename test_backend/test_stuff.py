def test_boolean():
    assert True


def test_boolean_benchmark(benchmark):
    benchmark(test_boolean)
