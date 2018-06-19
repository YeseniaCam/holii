class DoTransition:
    def __init__(self, actual, siguiente, caracter):
        self.actual = actual
        self.siguiente = siguiente
        self.caracter = caracter

    # Metodo para poder imprimir de forma legible una instancia de esta clase
    
    def __str__(self):
        return '{}->{}: {}'.format(self.actual, self.siguiente, self.caracter)


class AFNDefiner:
    def __init__(self):
        self.alfabeto = set()
        self.finalStates = set()
        self.initialState = 0
        self.actualStates = list()
        self.transiciones = list()
        self.estados = set()
        self.errorState = -1

    def AddTransition(self, actual, siguiente, caracter):
        self.transiciones.append(DoTransition(actual, siguiente, caracter))

    def AddFinals(self, estados):
        self.finalStates = estados

    def AddAlphabet(self, alfabeto): 
        self.alfabeto = alfabeto
        self.alfabeto.add('e')

    def AddInitial(self, estado):
        self.initialState = estado

    def AddState(self, estado):
        if estado in self.estados:
            print("Estado repetido")
        else:
            self.estados.add(estado)

    def Validate(self, cadena):
        self.actualStates = self.EpsilonStates(self.initialState)
        for caracter in cadena:
            if caracter not in self.alfabeto:
                return False
            nextStates = self.GetNext(caracter)
            self.actualStates = []
            for e in nextStates:
                self.actualStates.extend(self.EpsilonStates(e))

        for estado in self.actualStates:
            if estado in self.finalStates:
                return True
        return False

    def GetNext(self, caracter):
        siguientes = list()
        for estado in self.actualStates:
            for transicion in self.transiciones:
                if estado == transicion.actual and transicion.caracter == caracter:
                    siguientes.append(transicion.siguiente)
        return siguientes

    def EpsilonStates(self, estados):
        epsilon = list()
        epsilon.append(estados)
        for estado in epsilon:
            for t in self.transiciones:
                if t.caracter == 'e' and t.actual == estado and (t.siguiente not in epsilon):
                    epsilon.append(t.siguiente)
        return epsilon


class AFDDefiner(AFNDefiner):
    def AddAlphabet(self, alfabeto):
        self.alfabeto = alfabeto

    def Validate(self, cadena):
        self.actualStates.append(self.initialState)
        continues = True
        for caracter in cadena:
            if caracter not in self.alfabeto:
                return False
            for transicion in self.transiciones:
                if transicion.actual == self.actualStates[0]:
                    if transicion.caracter == caracter:
                        self.actualStates[0] = transicion.siguiente
                        continues = True
                        break
                else:
                    continues = False
            if not continues:
                self.actualStates[0] = self.errorState

        return self.actualStates[0] in self.finalStates