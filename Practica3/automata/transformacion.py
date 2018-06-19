from automata.automatas import AFDDefiner

# Clase para poder etiquetar los nuevos estados de manera más facil
class SubSet:
    def __init__(self, states, label):
        self.states = states
        self.label = label


class TransformToAFD:
    def __init__(self, AFN):
        self.lista = list()
        self.AFN = AFN
        self.AFD = AFDDefiner()
        self.label = 'A' 
        # Para etiquetar los estados AFD

    def Convert(self):
        self.AFD.alfabeto = self.AFN.alfabeto
        self.AFD.alfabeto.remove('e')
        estado = self.EpsilonClosure(self.AFN.initialState)
        actual = SubSet(estado, self.label)
        self.lista.append(actual)
        pendants = list()
        pendants.append(actual)
        add = True
        self.label = chr(ord(self.label) + 1)
        new = None
        while len(pendants) > 0:
            actual = pendants.pop()
            for simbolo in self.AFD.alfabeto:
                estados = self.EpsilonClosure(self.Move(actual.states, simbolo))
                add = True
                for i in self.lista:
                    if i.states == estados:
                        add = False
                        new  = i
                        break
                if add:
                    new = SubSet(estados, self.label)
                    pendants.append(new)
                    self.lista.append(new)
                    self.label = chr(ord(self.label) + 1)
                print("Transicion %s -> %s con: %s" % (actual.states, new.states, simbolo))
                self.AFD.AddTransition(actual.label, new.label, simbolo)
        
        # Obtenemos los estados finales e inicial
        for elemento in self.lista:
            if self.AFN.initialState in elemento.states:
                self.AFD.initialState = elemento.label
            for final in self.AFN.finalStates: 
                if final in elemento.states:
                    self.AFD.finalStates.add(elemento.label)

    # recibe un solo elemento o un conjunto de estados
    def EpsilonClosure(self, estados):
        EpsilonStates = set()
        aux = list()
        if type(estados) is set:
            aux.extend(estados)
        else:
            aux.append(estados)
        for state in aux:
            for t in self.AFN.transiciones:
                if t.caracter == 'e' and t.actual == state and (t.siguiente not in aux):
                    aux.append(t.siguiente)

        EpsilonStates.update(aux)
        return EpsilonStates

    # Obtiene los siguientes estados con base en un simbolo y un conjunto de entrada
    def Move(self, estados, simbolo):
        auxStates = set()
        for state in estados:
            for t in self.AFN.transiciones:
                if simbolo != 'e' and state == t.actual and t.caracter == simbolo:
                    auxStates.add(t.siguiente)
        return auxStates