#19
class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def sumar(self, otro_polinomio):
        coef1 = self.coeficientes + [0] * (len(otro_polinomio.coeficientes) - len(self.coeficientes))
        coef2 = otro_polinomio.coeficientes + [0] * (len(self.coeficientes) - len(otro_polinomio.coeficientes))
        coeficientes_suma = [c1 + c2 for c1, c2 in zip(coef1, coef2)]
        return Polinomio(coeficientes_suma)

    def restar(self, otro_polinomio):
        coef1 = self.coeficientes + [0] * (len(otro_polinomio.coeficientes) - len(self.coeficientes))
        coef2 = [-c for c in otro_polinomio.coeficientes] + [0] * (len(self.coeficientes) - len(otro_polinomio.coeficientes))
        coeficientes_resta = [c1 + c2 for c1, c2 in zip(coef1, coef2)]
        return Polinomio(coeficientes_resta)

    def evaluar(self, x):
        return sum(c * x ** i for i, c in enumerate(self.coeficientes))
p1 = Polinomio([1, 2, 3])
p2 = Polinomio([1, 0, -4, 2])
p3 = p1.restar(p2)
print(p3.coeficientes)  # Output: [-1, 2, 7, -2]
