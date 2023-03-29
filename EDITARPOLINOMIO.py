class Polinomio:
    def __init__(self, terminos):
        # Inicializar el polinomio con una lista de términos
        self.terminos = terminos
    
    def editar_termino(self, exponente, coeficiente):
        for i, termino in enumerate(self.terminos):
            if termino[1] == exponente:
                # Encontrar el término que se quiere editar
                if coeficiente == 0:
                    # Si el coeficiente es cero, eliminar el término
                    del self.terminos[i]
                else:
                    # Si el coeficiente no es cero, editar el término
                    self.terminos[i] = (coeficiente, exponente)
                # Asegurarse de que el coeficiente del término editado sea no nulo
                if exponente == 0 and self.terminos[i][0] == 0:
                    self.terminos[i] = (0, 0)
                break
        else:
            # Si el exponente no se encuentra en el polinomio, agregar el término
            if coeficiente != 0:
                self.terminos.append((coeficiente, exponente))
            else:
                raise ValueError("El coeficiente del término no puede ser cero.")
