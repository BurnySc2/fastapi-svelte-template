import time


def test_boolean():
    time.sleep(0.3)
    assert True


def test_boolean_benchmark(benchmark):
    benchmark(test_boolean)
