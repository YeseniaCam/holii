from automata.automatas import AFDDefiner, AFNDefiner
from automata.transformacion import TransformToAFD
from expresiones.analizador import Analizer

class Inicio:

    def NonDeterministicAutomaton(self):
        print("Automata no determinista")
        afn = AFNDefiner()
        afn.AddAlphabet({'a', 'b'})
        afn.AddState(0)
        afn.AddState(1)
        afn.AddState(2)
        afn.AddState(3)

        afn.AddInitial(0)
        afn.AddFinals({3})

        afn.AddTransition(0, 1, 'a')
        afn.AddTransition(1, 2, 'b')
        afn.AddTransition(2, 3, 'b')
        afn.AddTransition(0, 0, 'a')
        afn.AddTransition(0, 0, 'b')
        for n in range(5):
            cadena = input("Validar cadena: ")
            print("La cadena es:")
            if afn.Validate(cadena):
                print("Valida")
            else:
                print("No valida")
inicio = Inicio()
inicio.NonDeterministicAutomaton()