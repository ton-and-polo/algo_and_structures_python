"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit
import cProfile


prime_index = 10


def prime_num_1(index):

    def sieve_of_eratosthenes(n):
        prime_numbers = []
        for possible_prime in range(2, n):
            is_prime = True
            for num in range(2, possible_prime):
                if possible_prime % num == 0:
                    is_prime = False

            if is_prime:
                prime_numbers.append(possible_prime)

        return prime_numbers

    i = 1
    while len(sieve_of_eratosthenes(i)) < index:
        i += 1

    return sieve_of_eratosthenes(i)[-1]


def prime_num_2(index):

    def sieve_of_eratosthenes(n):
        return [num for num in range(2, n) if all(num % i != 0 for i in range(2, num))]

    i = 1
    while len(sieve_of_eratosthenes(i)) < index:
        i += 1

    return sieve_of_eratosthenes(i)[-1]


def main():
    prime_num_1(prime_index)
    prime_num_2(prime_index)

    return 'End of main()'


# Execution time:
print(timeit.timeit('prime_num_1(prime_index)', globals=globals(), number=1000))
print(timeit.timeit('prime_num_2(prime_index)', globals=globals(), number=1000))

"""
0.441493436
0.5511465019999999
"""

# Execution report:
print(cProfile.run('main()'))

"""
         2771 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 2.py:13(prime_num_1)
       31    0.000    0.000    0.000    0.000 2.py:15(sieve_of_eratosthenes)
        1    0.000    0.000    0.001    0.001 2.py:35(prime_num_2)
       31    0.000    0.000    0.001    0.000 2.py:37(sieve_of_eratosthenes)
     1997    0.000    0.000    0.000    0.000 2.py:38(<genexpr>)
       31    0.001    0.000    0.001    0.000 2.py:38(<listcomp>)
        1    0.000    0.000    0.002    0.002 2.py:47(main)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
      434    0.000    0.000    0.001    0.000 {built-in method builtins.all}
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
       60    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      181    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
