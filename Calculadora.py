def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
def potencia(a, b):
    return a ** b
def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz cuadrada de número negativo"
    return a ** 0.5
def raiz_cubica(a):
    if a < 0:
        return -(-a) ** (1/3)
    return a ** (1/3)
def logaritmo(a, base=10):
    import math
    if a <= 0:
        return "Error: Logaritmo de número no positivo"
    return math.log(a, base)
def porcentaje(a, b):
    return (a / 100) * b
def factorial(n):
    if n < 0:
        return "Error: Factorial de número negativo"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result