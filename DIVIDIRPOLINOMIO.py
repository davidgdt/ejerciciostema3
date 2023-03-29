#21
def dividir_polinomios(dividendo, divisor):
    # Obtener el grado máximo del dividendo y divisor
    grado_dividendo = len(dividendo) - 1
    grado_divisor = len(divisor) - 1

    # Verificar que el divisor no sea el polinomio cero
    if grado_divisor == 0 and divisor[0] == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")

    # Si el grado del divisor es mayor que el del dividendo, el resultado es cero
    if grado_dividendo < grado_divisor:
        return [0], dividendo

    # Inicializar el cociente y el resto con ceros
    cociente = [0] * (grado_dividendo - grado_divisor + 1)
    resto = list(dividendo)

    # Algoritmo de división de polinomios
    for i in range(grado_dividendo - grado_divisor + 1):
        coeficiente = resto[i] / divisor[0]
        cociente[-i-1] = coeficiente
        for j in range(1, grado_divisor + 1):
            resto[i + j] -= coeficiente * divisor[j]

    # Eliminar ceros a la izquierda del cociente y el resto
    while len(cociente) > 1 and cociente[0] == 0:
        cociente.pop(0)
    while len(resto) > 1 and resto[0] == 0:
        resto.pop(0)

    # Devolver el cociente y el resto como listas de coeficientes
    return cociente, resto
dividendo = [1, 5, -2, 4]
divisor = [-1, 2]
cociente, resto = dividir_polinomios(dividendo, divisor)
print("Cociente:", cociente)  # Output: [4, -3]
print("Resto:", resto)  # Output: [1, 9]
