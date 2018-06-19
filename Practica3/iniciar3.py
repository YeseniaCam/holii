from automata.automatas import AFDDefiner, AFNDefiner
from automata.transformacion import TransformToAFD
from expresiones.analizador import Analizer

class Inicio:
    def init_analizer(self):
        print("Generando el automata de la expresion: (a|b)*abb ...")
        analizer = Analizer()
        # Transformamos la expresion a postfijo
        analizer.ConvertToPostfix('(a|b)*abb')
        analizer.ShowPostfix()
        # Creamos el AFN a partir de la expresion en postfijo
        analizer.GenAutomaton()
        analizer.ShowAutomaton()
        # Probamos nuestro automata con algunas cadenas
        print("Pruebas sobre el automata generado...")
        AFN = analizer.AFN
        for n in range(5):
            cadena = input("-Ingresa una cadena: ")
            print("La cadena es:")
            if AFN.Validate(cadena):
                print("Valida") 
            else:
                print("No valida")

Inicio = Inicio()
Inicio.init_analizer()