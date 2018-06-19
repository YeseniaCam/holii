from automata.automatas import DoTransition
from automata.automatas import AFNDefiner

class Analizer:
    def __init__(self):
        self.postfijo = list()
        self.transiciones = list()
        self.pila_transiciones = []
        self.isPositive = 0 
        self.isKleene = 1
        self.AFN = AFNDefiner()

    def ShowPostfix(self):
        print(self.postfijo)

    def ShowAutomaton(self):
        print('Inicial: %s Finales: %s' % (self.AFN.initialState, self.AFN.finalStates))
        print("Transiciones:")
        for t in self.AFN.transiciones:
            print(t)

    def ConvertToPostfix(self, cadena):
        pila = []
        punto = False
        for c in cadena:
            if c == '(':
                if punto:
                    while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*'):
                        self.postfijo.append(pila.pop())
                    pila.append('.')
                    punto = False
                pila.append(c)
            elif c == ')':
                punto = True
                while len(pila) > 0 and pila[-1] != '(':
                    self.postfijo.append(pila.pop())
                try:
                    pila.pop()
                except IndexError as e:
                    raise e
            elif c == '+' or c == '*':
                self.postfijo.append(c)
            elif c == '|':
                while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*' or pila[-1] == '.'):
                    self.postfijo.append(pila.pop())
                pila.append(c)
                punto = False
            else:
                if punto:
                    while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*'):
                        self.postfijo.append(pila.pop())
                    pila.append('.')
                punto = True
                self.postfijo.append(c)

        while len(pila) > 0:
            self.postfijo.append(pila.pop())

    def GenAutomaton(self):
        inicial = 1
        final = 2
        self.AFN.alfabeto.add('e')
        for c in self.postfijo:
            if c == '*':
                print('Cerradura Kleene: ')
                s = self.pila_transiciones.pop()
                self.Closure(s, self.isKleene)
            elif c == '+':
                print('Cerradura Positiva')
                s = self.pila_transiciones.pop()
                self.Closure(s, self.isPositive)
            elif c == '|':
                print("Union")
                s = self.pila_transiciones.pop()
                t = self.pila_transiciones.pop()
                i1 = DoTransition(s[1] + 1, s[0], 'e')
                i2 = DoTransition(s[1] + 1, t[0], 'e')
                f1 = DoTransition(s[1], s[1] + 2, 'e')
                f2 = DoTransition(t[1], s[1] + 2, 'e')
                self.pila_transiciones.append([s[1] + 1, s[1] + 2])
                self.transiciones.extend((i1, i2, f1, f2))
            elif c == '.':
                print('CONCATENACION')
                t = self.pila_transiciones.pop()
                s = self.pila_transiciones.pop()
                for aux in self.transiciones:
                    if aux.siguiente == s[1]:
                        aux.siguiente = t[0]
                self.pila_transiciones.append([s[0], t[1]])
            else:
                print('ESTADO')
                if self.pila_transiciones.__len__() > 0:
                    inicial = self.pila_transiciones[-1][1] + 1
                    final = inicial + 1
                transicion = DoTransition(inicial, final, c)
                self.pila_transiciones.append([inicial, final])
                self.transiciones.append(transicion)
                self.AFN.alfabeto.add(c)

        self.AFN.AddInitial(self.pila_transiciones[0][0])
        self.AFN.AddFinals({self.pila_transiciones[0][1]})
        self.AFN.transiciones = self.transiciones

    def Closure(self, s, tipo):
        i1 = DoTransition(s[1] + 1, s[0], 'e')
        s1 = DoTransition(s[1], s[0], 'e')
        s2 = DoTransition(s[1], s[1] + 2, 'e')
        self.pila_transiciones.append([s[1] + 1, s[1] + 2])
        self.transiciones.extend((i1, s1, s2))

        if tipo == self.isKleene:
            i2 = DoTransition(s[1] + 1, s[1] + 2, 'e')
            self.transiciones.append(i2)