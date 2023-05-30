class Cinta:
    simbolo_enblanco = " "
    def __init__(self, cadena_cinta = ""):
        self.cinta = dict((enumerate(cadena_cinta)))
    
    def cadena(self):
        cadena = ""
        indice_min = min(self.cinta.keys())
        indice_max = max(self.cinta.keys())
        for i in range(indice_min, indice_max):
            cadena += self.cinta[i]
        return cadena

    def __getitem__(self, indice):
        if indice in self.cinta:
            return self.cinta[indice]
    
    def __setitem__(self, pos, car):
        self.cinta[pos] = car

class MT:
    def __init__(self, cinta ="", simbolo_enblanco = " ", q0 = "", qfinales = None, funcionTransicion = None):
        pass
    
    def getCinta(self):
        pass
    
    def step(self):
        pass
    
    def final(self):
        pass
