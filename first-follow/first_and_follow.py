#Modulo re que proporciona soporte para expresiones regulares.
#Permite buscar, dividir, y manipular texto de manera eficiente usando estos pratones de expresiones regulares.
import re
from pathlib import Path

def print_grammar(productions):
    """
    Imprime la gramática cargada en un formato legible.

    @param productions: Diccionario que contiene las producciones de la gramática.
    """
    print("*****GRAMÁTICA*****")
    for lhs, rhs in productions.items():
        right_hand = [" ".join(prod) for prod in rhs]
        print(f"{lhs} -> {' | '.join(right_hand)}")
    print("")

def cal_follow(s, productions, first, follow=None, visited=None):
    """
    Calcula el conjunto FOLLOW de un símbolo no terminal.

    @param s: El símbolo para el que se calculará el FOLLOW.
    @param productions: Un diccionario que contiene las producciones de la gramática.
    @param first: Un diccionario que contiene los conjuntos FIRST de los símbolos.
    @param follow: Un diccionario que almacena los conjuntos FOLLOW de los símbolos.
    @param visited: Un conjunto para evitar recursión infinita.
    @return: El conjunto FOLLOW del símbolo s.
    """
    if follow is None:
        follow = {key: set() for key in productions}
    if visited is None:
        visited = set()

    # Evitar recursión infinita
    if s in visited:
        return follow[s]

    visited.add(s)  # Marca el símbolo como visitado

    # Agrega '$' al FOLLOW del símbolo inicial de la gramática
    if s == list(productions.keys())[0]:
        follow[s].add('$')

    # Itera sobre todas las producciones para encontrar dónde aparece el símbolo s
    for head, bodies in productions.items():
        for body in bodies:
            for i, symbol in enumerate(body):
                if symbol == s:
                    # Si hay un símbolo a la derecha de 's'
                    if i + 1 < len(body):
                        next_symbol = body[i + 1]
                        if next_symbol.isupper():  # Es un no terminal
                            # Añadir FIRST(next_symbol) excepto 'ε'
                            follow[s].update(first[next_symbol] - {'ε'})
                            if 'ε' in first[next_symbol]:
                                # Si 'ε' está en FIRST(next_symbol), añadir FOLLOW(head)
                                follow[s].update(cal_follow(head, productions, first, follow, visited))
                        else:  # Es un terminal
                            follow[s].add(next_symbol)
                    else:
                        # Si 's' está al final de la producción, añadir FOLLOW(head)
                        if head != s:  # Evitar ciclos directos
                            follow[s].update(cal_follow(head, productions, first, follow, visited))

    visited.remove(s)  # Desmarca el símbolo al terminar
    return follow[s]


def cal_first(s, productions, visited=None):
    """
    Calcula el conjunto FIRST de un símbolo no terminal.

    @param s: El símbolo para el que se calculará el FIRST.
    @param productions: Un diccionario que contiene las producciones de la gramática.
    @param visited: Un conjunto para rastrear los símbolos ya visitados y evitar recursión infinita.
    @return: El conjunto FIRST del símbolo s.
    """
    # Inicializa el conjunto de símbolos visitados si no se proporciona
    if visited is None:
        visited = set()
    
    # Evita bucles en gramáticas recursivas
    if s in visited:
        return set()

    visited.add(s)  # Marca el símbolo como visitado
    first = set()  # Inicializa el conjunto FIRST vacío

    # Recorre las producciones del símbolo s
    for production in productions.get(s, []):
        for i, c in enumerate(production):
            if c.isupper():  # Si el símbolo es no terminal
                # Calcula el FIRST del símbolo recursivamente
                f = cal_first(c, productions, visited)
                first.update(f - {'ε'})  # Añade todo excepto ε

                if 'ε' not in f:
                    break  # Si ε no está, detén el bucle
            else:  # Si el símbolo es terminal
                first.add(c)
                break
        else:
            # Si se recorrieron todos los símbolos y todos contienen ε
            first.add('ε')

    visited.remove(s)  # Desmarca el símbolo al terminar
    return first


# Función principal
def main():
    """
    Función principal que lee la gramática desde un archivo, calcula los conjuntos
    FIRST y FOLLOW y los muestra por pantalla.
    """
    productions = {}  # Diccionario para almacenar las producciones de la gramática.
    grammar_path = Path(__file__).parent / "examples" / "grammar5.txt"
    grammar = grammar_path.open("r", encoding="utf-8")  # Abre el archivo de gramática.
    
    first = {}  # Diccionario para almacenar los conjuntos FIRST.
    follow = {}  # Diccionario para almacenar los conjuntos FOLLOW.
    
    # Lee cada línea del archivo y construye las producciones.
    #re.split divide una cadena (prod) en partes usadando una expresion regular como delimitador
    #El patron ( /->/\n/)* intenta dvidir el texto utilizando ->, saltos de linea o espacios
    #Como ibjetivo tiene separar la produccion de la gramatica en el lado izquierdo y derecho, facilitando el procesamiento de las reglas
    for prod in grammar:
        l = re.split("( /->/\n/)*", prod)  # Divide la producción en partes usando regex.
        m = []
        for i in l:
            # Filtra los caracteres innecesarios.
            if (i == "" or i is None or i == '\n' or i == " " or i == "-" or i == ">"):
                pass
            else:
                m.append(i)
        
        left_prod = m.pop(0)  # Lado izquierdo de la producción.
        right_prod = []
        t = []
        
        # Construye la lista de producciones para cada lado derecho.
        for j in m:
            if j != '|':
                t.append(j)
            else:
                right_prod.append(t)
                t = []
        
        right_prod.append(t)
        productions[left_prod] = right_prod
    
    # Imprime la gramática antes de calcular FIRST y FOLLOW
    print_grammar(productions)
    # Calcula los conjuntos FIRST para cada símbolo no terminal.
    for s in productions.keys():
        first[s] = cal_first(s, productions)
    print("*****FIRST*****")
    for lhs, rhs in first.items():
        print(lhs, ":", rhs)
    
    print("")
    
    # Inicializa el conjunto FOLLOW de cada no terminal como vacío.
    for lhs in productions:
        follow[lhs] = set()
    
    # Calcula los conjuntos FOLLOW.
    for s in productions.keys():
        follow[s] = cal_follow(s, productions, first)
    
    print("*****FOLLOW*****")
    for lhs, rhs in follow.items():
        print(lhs, ":", rhs)
    
    grammar.close()

# Ejecuta la función principal si el archivo se ejecuta directamente.
if __name__ == "__main__":
    main()
