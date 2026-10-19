class AFN:
    """
    Clase para representar un Autómata Finito No Determinista (AFN).
    Permite agregar estados, transiciones y simular cadenas de entrada para encontrar
    la palabra más larga aceptada por el autómata.
    """

    def __init__(self):
        """
        Constructor de la clase AFN. Inicializa el autómata con:
        - Un diccionario vacío para los estados.
        - Un estado inicial no definido.
        - Un conjunto vacío de estados de aceptación.
        """
        self.estados = {}  # Diccionario para almacenar los estados y sus transiciones.
        self.estado_inicial = None  # Estado inicial del autómata.
        self.estados_aceptacion = set()  # Conjunto de estados de aceptación.

    def agregar_estado(self, estado, es_inicial=False, es_aceptacion=False):
        """
        Agrega un estado al autómata.

        :param estado: Identificador único del estado (usualmente un número o string).
        :param es_inicial: Indica si este estado es el inicial del autómata.
        :param es_aceptacion: Indica si este estado es un estado de aceptación.

        :raises ValueError: Si se intenta definir más de un estado inicial.
        """
        self.estados[estado] = {}  # Inicializa el estado con un diccionario de transiciones vacío.

        # Configurar el estado inicial si corresponde.
        if es_inicial:
            if self.estado_inicial is not None:
                raise ValueError(f"El estado inicial ya está definido como {self.estado_inicial}.")
            self.estado_inicial = estado

        # Agregar el estado a los estados de aceptación si corresponde.
        if es_aceptacion:
            self.estados_aceptacion.add(estado)

    def agregar_transicion(self, desde, hacia, simbolo):
        """
        Agrega una transición entre dos estados del autómata.

        :param desde: Estado de origen.
        :param hacia: Estado de destino.
        :param simbolo: Símbolo que activa la transición (carácter).

        :raises ValueError: Si el estado de origen no existe en el autómata.
        """
        if desde not in self.estados:
            raise ValueError(f"El estado {desde} no existe.")

        # Agregar la transición para el símbolo dado.
        if simbolo not in self.estados[desde]:
            self.estados[desde][simbolo] = []
        self.estados[desde][simbolo].append(hacia)

    def simular(self, cadena):
        """
        Simula la ejecución del AFN sobre una cadena de entrada para encontrar
        la palabra más larga aceptada por el autómata.

        :param cadena: La cadena de entrada que se desea evaluar.
        :return: Una tupla (aceptado, palabra), donde:
                 - aceptado es True si la cadena es aceptada, False en caso contrario.
                 - palabra es la palabra más larga aceptada si existe, o una cadena vacía.

        :raises ValueError: Si el estado inicial no está definido o es inválido.
        """
        # Verificar que el estado inicial esté definido y sea válido.
        if self.estado_inicial is None or self.estado_inicial not in self.estados:
            raise ValueError("El autómata no tiene un estado inicial definido o el estado inicial es inválido.")

        # Inicialización para el procesamiento.
        estado_actual = self.estado_inicial  # Comenzar desde el estado inicial.
        ultimo_estado_aceptado = None  # Almacena el último estado de aceptación alcanzado.
        posicion_ultimo_estado = -1  # Almacena la posición del último estado de aceptación en la cadena.
        i = 0  # Índice actual en la cadena de entrada.

        # Procesar la cadena carácter por carácter.
        while i < len(cadena):
            simbolo = cadena[i]

            # Verificar si el símbolo actual tiene una transición válida desde el estado actual.
            if simbolo in self.estados[estado_actual]:
                estado_actual = self.estados[estado_actual][simbolo][0]  # Mover al primer estado destino.

                # Si el nuevo estado es de aceptación, actualizar los registros.
                if estado_actual in self.estados_aceptacion:
                    ultimo_estado_aceptado = estado_actual
                    posicion_ultimo_estado = i

                # Avanzar al siguiente carácter de la cadena.
                i += 1
            else:
                # Si no hay transición válida, detener el procesamiento.
                break

        # Retroceder al último estado aceptado si es necesario.
        if ultimo_estado_aceptado is not None:
            # Validar si quedan caracteres adicionales en la cadena.
            if posicion_ultimo_estado + 1 < len(cadena):
                return False, ""  # Cadena no válida porque hay caracteres adicionales.
            return True, cadena[:posicion_ultimo_estado + 1]  # Retorna la palabra más larga aceptada.

        # Si no se alcanzó ningún estado de aceptación.
        return False, ""

    def __str__(self):
        """
        Genera una representación en formato texto del autómata, incluyendo:
        - Estado inicial.
        - Estados de aceptación.
        - Transiciones entre estados.

        :return: Una cadena descriptiva del autómata.
        """
        resultado = "AFN:\n"
        resultado += f"Estado inicial: {self.estado_inicial}\n"
        resultado += f"Estados de aceptación: {self.estados_aceptacion}\n"
        resultado += "Transiciones:\n"

        # Agregar cada transición al resultado.
        for estado, transiciones in self.estados.items():
            for simbolo, destinos in transiciones.items():
                resultado += f"  {estado} --{simbolo}--> {destinos}\n"
        return resultado
