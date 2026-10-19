# Toolkit de Lenguajes Formales

Colección de implementaciones en Python sobre conceptos fundamentales de lenguajes formales y construcción de compiladores: autómatas finitos, reconocimiento de tokens, conjuntos FIRST/FOLLOW y análisis sintáctico shift-reduce.

Este repositorio consolida cuatro proyectos académicos en un solo toolkit organizado. Cada módulo se puede ejecutar de manera independiente e incluye entradas de ejemplo.

## Módulos incluidos

| Módulo | Concepto demostrado | Punto de entrada |
| --- | --- | --- |
| [Conversión de AFN a AFD](./automata-conversion/) | Clausura-épsilon y construcción de subconjuntos | `automata-conversion/main.py` |
| [Reconocimiento de tokens](./token-recognition/) | Reconocimiento mediante autómatas de palabras reservadas y operadores seleccionados de C | `token-recognition/main.py` |
| [Conjuntos FIRST y FOLLOW](./first-follow/) | Cálculo de FIRST/FOLLOW para gramáticas simples independientes del contexto | `first-follow/first_and_follow.py` |
| [Parser shift-reduce](./shift-reduce-parser/) | Operaciones de desplazamiento y reducción basadas en una pila y archivos de gramática | `shift-reduce-parser/sr.py` |

## Requisitos

- Python 3.8 o posterior.
- No requiere dependencias externas.

## Inicio rápido

Clona el repositorio:

```bash
git clone https://github.com/dev1206al/formal-languages-toolkit.git
cd formal-languages-toolkit
```

Ejecuta cualquiera de los módulos desde la raíz del repositorio:

```bash
python3 automata-conversion/main.py
python3 token-recognition/main.py
python3 first-follow/first_and_follow.py
python3 shift-reduce-parser/sr.py
```

El parser shift-reduce solicitará la ruta de un archivo de gramática. Por ejemplo:

```text
shift-reduce-parser/examples/gram1.txt
```

## Descripción de los módulos

### 1. Conversión de AFN a AFD

Implementa el algoritmo de construcción de subconjuntos, incluyendo clausuras-épsilon, para transformar un autómata finito no determinista en uno determinista. Los ejemplos incluidos muestran tablas de transición, estados iniciales, estados finales y transiciones hacia estados sumidero.

### 2. Reconocimiento de tokens

Construye un autómata finito que reconoce un conjunto reducido de tokens del lenguaje C:

- Palabras reservadas: `if`, `int`, `else`, `while`.
- Operadores o expresiones: `i`, `i++`.

El programa de ejemplo evalúa cadenas válidas e inválidas e indica si cada una fue aceptada.

### 3. Conjuntos FIRST y FOLLOW

Carga una gramática independiente del contexto desde un archivo de texto y calcula los conjuntos FIRST y FOLLOW de sus símbolos no terminales. Hay diez gramáticas disponibles en [`first-follow/examples`](./first-follow/examples/).

De manera predeterminada, el programa utiliza `grammar5.txt`. Se puede seleccionar otro ejemplo desde `first_and_follow.py`.

### 4. Parser shift-reduce

Demuestra el análisis sintáctico ascendente mediante una pila y dos operaciones centrales:

- **Shift (desplazamiento):** mueve el siguiente token de la entrada hacia la pila.
- **Reduce (reducción):** sustituye un lado derecho coincidente por el lado izquierdo de su producción.

Se incluyen seis gramáticas de ejemplo en [`shift-reduce-parser/examples`](./shift-reduce-parser/examples/).

## Estructura del repositorio

```text
formal-languages-toolkit/
├── automata-conversion/
│   ├── logic.py
│   └── main.py
├── token-recognition/
│   ├── af.py
│   └── main.py
├── first-follow/
│   ├── examples/
│   ├── notes/
│   └── first_and_follow.py
├── shift-reduce-parser/
│   ├── examples/
│   └── sr.py
├── docs/images/
└── README.md
```

## Alcance

Estas implementaciones son demostraciones educativas de los algoritmos correspondientes. Se mantienen deliberadamente compactas y no pretenden sustituir generadores de analizadores léxicos o sintácticos para producción.

## Autor

**Luis Enrique Alvarez Segura**  
Egresado de Ingeniería en Computación, Universidad Autónoma Metropolitana (UAM)

- [GitHub](https://github.com/dev1206al)
- [LinkedIn](https://www.linkedin.com/in/luis-enrique-alvarez-segura/)
