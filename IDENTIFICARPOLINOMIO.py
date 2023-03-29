class Polinomio:
    def __init__(self, terminos):
        # Inicializar el polinomio con una lista de términos
        self.terminos = terminos
    
    def existe_termino(self, exponente):
        for termino in self.terminos:
            if termino[1] == exponente:
                # Encontrar el término buscado
                return True
        # Si se recorren todos los términos y no se encuentra el término buscado, retornar False
        return False
