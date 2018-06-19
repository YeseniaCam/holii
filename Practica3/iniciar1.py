from automata.automatas import AFDDefiner, AFNDefiner
from automata.transformacion import TransformToAFD
from expresiones.analizador import Analizer
class Inicio:
    def DeterministicAutomaton(self):
        print("Automata determinista")
        afd = AFDDefiner()
        afd.AddAlphabet({'a', 'b'})
        afd.AddState(0)
        afd.AddState(1)
        afd.AddState(2)
        afd.AddState(3)

        afd.AddInitial(0)
        afd.AddFinals({3})

        afd.AddTransition(0, 1, 'a')
        afd.AddTransition(1, 2, 'b')
        afd.AddTransition(2, 3, 'b')
        afd.AddTransition(0, 0, 'b')
        afd.AddTransition(1, 1, 'a')
        afd.AddTransition(2, 1, 'a')
        afd.AddTransition(3, 1, 'a')
        afd.AddTransition(3, 0, 'b')

        for n in range(5):
            cadena = input("Validar cadena: ")
            print("La cadena es:")
            if afd.Validate(cadena):
                print("Valida")
            else:
                print("No valida")

inicio = Inicio()
inicio.DeterministicAutomaton()