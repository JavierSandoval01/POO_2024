#clase padre
#Clase Principal y Abstracta 
class Lectores:
    def __init__(self,nombre,direccion,tel):
       self.nombre=nombre
       self.direccion=direccion
       self.tel=tel 

    def reservar(self):
        print (f"Reserva")

    def entregar(self):
        print (f"Listo para entrega")


    #Metodos de gettes y Setters faltantes

    def setnombre(self,nombre):
        self.nombre=nombre

    def setdireccion(self,direccion):
        self.direccion=direccion
        
    def settel(self,tel):
        self.tel=tel

    def getnombre(self):
       return self.nombre

    def getdireccion(self):
        return self.direccion  
    
    def gettel(self):
        return self.tel     

#Clases Scuendiarias
#Estudiantes

class Estudiantes(Lectores):
    def __init__(self,nombre,direccion,tel,carrera,matricula):
        super().__init__(nombre,direccion,tel)
        self._carrera=carrera
        self._matricula=matricula
        
    def reservar(self):
        print(f"La reserva se hizo a nombre: {self.getnombre()}, con matricula{self.getmatricula()} de la carrera de {self.getcarrera()}, numero de telefono: {self.gettel()}. Direccion correspondiente: {self.getdireccion()}")
        return super().reservar()
    
    def entregar(self):
        return super().entregar()
    
    #metodos get y set
    def getcarrera(self):
        return self._carrera

    def getmatricula(self):
        return self._matricula

    def setAlto(self,carrera):
        self._carrera=carrera

    def setmatricula(self,matricula):
        self.__matricula=matricula    
        
        
        
#Clases Scuendiarias
#docentes

class Docentes(Lectores):
    def __init__(self,nombre,direccion,tel,modalidad,num_empleado):
        super().__init__(nombre,direccion,tel)
        self.__modalidad=modalidad
        self.__num_empleado=num_empleado
        
    def reservar(self):
        print(f"La reserva se hizo a nombre: {self.getnombre()}, de la modalidad de {self.getmodalidad()}, numero de telefono: {self.gettel()}. Direccion correspondiente: {self.getdireccion()}")
        return super().reservar()
    
    def entregar(self):
        return super().entregar()
    
    #metodos get y set
    def getmodalidad(self):
        return self.__modalidad

    def getAncho(self):
        return self.__num_empleado

    def setAlto(self,modalidad):
        self.__modalidad=modalidad

    def setAncho(self,num_empleado):
        self.___num_empleado=num_empleado    