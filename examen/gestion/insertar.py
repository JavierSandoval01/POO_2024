from conexionBD import *

class insertar:
    def __init__(self, matricula,marca,modelo,color,nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif
        

    
    def registrarauto(self):
        try:
            cursor.execute(
                "insert into autos values(%s,%s,%s,%s,%s)",
            (self.matricula,self.marca,self.modelo,self.color,self.nif)
            )
            conexion.commit()
            print("Auto registrado correctamente")
            return True
            
        except:
            print("Ocurrio un error con el registro")
            return None