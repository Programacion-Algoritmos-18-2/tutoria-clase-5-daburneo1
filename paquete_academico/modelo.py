class Ciudad(object):
    def __init__(self):
        self.nombre_ciudad = "" #ATRIBUTOS DE CIUDAD
        self.poblacion = 0

    def agregar_nombre_ciudad(self, nciudad):
        self.nombre_ciudad = nciudad

    def obtener_nombre(self):
        return self.nombre_ciudad

    def agregar_poblacion(self, p):
        self.poblacion = p

    def obtener_poblacion(self):
        return self.poblacion

class Persona(object):
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.ciudad = "" #tipo de dato ciudad, creada una clase para este dato

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, a):
        self.apellido = a

    def obtener_apellido(self):
        return self.apellido

    def agregar_ciudad(self, c):
        self.ciudad = c

    def obtener_ciudad(self):
        return self.ciudad 

    def presentar_datos(self):
        return "%s-%s-%s" % (self.obtener_nombre(), self.obtener_apellido(), self.ciudad) 

class Estudiante(Persona):
    def __init__(self):
        super(Estudiante, self).__init__()
        self.ID_estudiante = 0
    
    def agregar_ID_estudiante(self, ID):
        self.ID_estudiante = ID
    
    def obtener_ID_estudiante(self):
        return self.ID_estudiante

    def presentar_datos(self):
        cadena = "%s \n ID_estudiante: %s" % (super(Estudiante, self).presentar_datos(), self.obtener_ID_estudiante())
        return cadena

class EstPresencial(Estudiante):
    def __init__(self):
        super(EstPresencial, self).__init__()
        self.ciclo = 0
        self.numero_creditos = 0

    def agregar_ciclo(self, ci):
        self.ciclo = ci

    def obtener_ciclo(self):
        return self.ciclo

    def agregar_numero_creditos(self, nc):
        self.numero_creditos = nc

    def obtener_numero_creditos(self):
        return self.numero_creditos
    
    def presentar_datos(self):
        cadena = "%s %s -- %d\n ciclo: %d \n numero_creditos: %d\nPertenece a la ciudad de %s, con poblacion de %s\n" % (self.obtener_nombre(),self.obtener_apellido(),
             self.obtener_ciclo(),self.obtener_numero_creditos(), self.obtener_numero_creditos(),self.obtener_ciudad().obtener_nombre(),self.obtener_ciudad().obtener_poblacion())
        
        return cadena

class EstDistancia(Estudiante):
    def __init__(self):
        super(EstDistancia, self).__init__()
        self.modulo = 0
        self.num_materias = 0

    def agregar_modulo(self, m):
        self.modulo = m

    def obtener_modulo(self):
        return self.modulo

    def agregar_num_materias(self, nm):
        self.num_materias = nm

    def obtener_num_materias(self):
        return self.num_materias

    def presentar_datos(self):
        cadena = "%s \n modulo: %s \n num_materias: %s" % (super(EstDistancia, self).presentar_datos(), self.obtener_modulo(), self.obtener_num_materias())
        return cadena
        