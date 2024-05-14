# Comparing PyPy performance with CPython and Numba

**Note**: I'm using PyPy 7.3.16 with Python 3.10.14 and comparing it with CPython
3.12.3 and Numba 0.59.1

## Installation

I'm assuming you already have installed pyenv and poetry in your system. Do it
so if you don't have them installed.

```bash
pyenv install 3.12.3
pyenv install pypy3.10.14
pyenv env use 3.12.3
poetry install --no-root
```

## Running the benchmark for PyPy

```bash
pyenv shell pypy3.10.14
poetry env use 3.10.14
poetry run ./calculate_pi.py  -n 100000000
```

With my Macbook Pro M1 Max with 10 cores and 64GB of RAM I got:
```text
Pi = 3.1420208, elapsed time = 2.217905044555664 second(s)
```

## Running the benchmark for CPython and Numba

```bash
pyenv shell 3.12.3
poetry env use 3.12.3
poetry run ./calculate_pi.py  -n 100000000 -j
```

With my Macbook Pro M1 Max with 10 cores and 64GB of RAM I got:
```text
Pi = 3.14182408, elapsed time = 0.5820541381835938 second(s)
```

## Benchmarking CPython for reference

```bash
pyenv shell 3.12.3
poetry env use 3.12.3
poetry run ./calculate_pi.py  -n 100000000
```

With my Macbook Pro M1 Max with 10 cores and 64GB of RAM I got:
```text
Pi = 3.14201936, elapsed time = 24.247615098953247 second(s)
```

## Conclusion

- PyPy performance:
  - Pi value obtained: 3.1420208
  - Elapsed time: 2.2179 seconds PyPy showed decent performance with regard to
    calculating Pi, but its execution time was slightly higher compared to
CPython and Numba.

- CPython performance:
  - Pi value obtained: 3.14182408
  - Elapsed time: 0.5820 seconds CPython outperformed PyPy in terms of both Pi
    calculation accuracy and execution speed, providing the most efficient
solution.

- Numba performance: Numba's performance results were not directly mentioned.
  However, it was included in the comparison with PyPy and CPython.

In conclusion, while PyPy offers a good balance of performance and Python
compatibility, it was slightly slower in this specific benchmark compared to
CPython. For tasks where execution speed is critical, CPython may be the
preferred choice. Numba could also be a strong contender for
performance-critical applications, leveraging JIT compilation to improve
execution speed.
