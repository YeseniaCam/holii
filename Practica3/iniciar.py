
from automata.automatas import AFDDefiner, AFNDefiner
from automata.transformacion import TransformToAFD
from expresiones.analizador import Analizer
class Inicio:
    def TransformAFNtoAFD(self):
        print('Transformando AFN a AFD')
        afn = AFNDefiner()
        afn.AddAlphabet({'a', 'b'})
        afn.AddState(0)
        afn.AddState(1)
        afn.AddState(2)
        afn.AddState(3)
        afn.AddState(4)
        afn.AddState(5)
        afn.AddState(6)
        afn.AddState(7)
        afn.AddState(8)
        afn.AddState(9)
        afn.AddState(10)
        afn.AddInitial(0)
        afn.AddFinals({10})

        afn.AddTransition(0, 1, 'e')
        afn.AddTransition(1, 2, 'e')
        afn.AddTransition(1, 4, 'e')
        afn.AddTransition(0, 7, 'e')
        afn.AddTransition(2, 3, 'a')

        afn.AddTransition(4, 5, 'b')
        afn.AddTransition(3, 6, 'e')
        afn.AddTransition(5, 6, 'e')
        afn.AddTransition(6, 1, 'e')
        afn.AddTransition(6, 7, 'e')
        afn.AddTransition(7, 8, 'a')
        afn.AddTransition(8, 9, 'b')
        afn.AddTransition(9, 10, 'b')

        newAFD = TransformToAFD(afn)
        print('Transformando el automata AFN a AFD')
        newAFD.Convert()
        print()
        print('-Automata deterministico final:')
        print("Estado inicial %s" % newAFD.AFD.initialState)
        print("Estados finales %s" % newAFD.AFD.finalStates)
        print("Transiciones")
        for t in newAFD.AFD.transiciones:
            print(t)

        print('Evaluacion de cadenas:')
        for n in range(5):
            cadena = input("Validar cadena: ")
            print("La cadena es:")
            if newAFD.AFD.Validate(cadena):
                print("Valida")
            else:
                print("No valida")

inicio = Inicio()
inicio.TransformAFNtoAFD()