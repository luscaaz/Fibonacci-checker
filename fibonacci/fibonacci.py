import math

def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def is_fibonacci_number(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

# Entrada usuário
number = int(input("Digite um número: "))

# Resultado
if is_fibonacci_number(number):
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")
