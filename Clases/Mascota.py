
#Clase Mascota revisada

class Mascota:
    def __init__(self, id:int, nombre:str,Especie:str, Fecha_Nacimiento:int, sexo:str, peso:str,LxAxAl:str):
        self.__id=id
        self.__nombre=nombre
        self.__Especie=Especie
        self.__Fecha_Nacimiento=Fecha_Nacimiento#Esto debe ser "DateTime"
        self.__sexo=sexo
        self.__peso=peso
        self.__LxAxAl=LxAxAl#LARGO X ANCHO X ALTO
        self.__Ficha_Medica=[]

        pass

    #Getters y Setters 
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_Especie(self):
        return self.__Especie
    def get_Fecha_Nacimiento(self):
        return self.__Fecha_Nacimiento
    def get_sexo(self):
        return self.__sexo
    def get_peso(self):
        return self.__peso
    def get_LxAxAl(self):
        return self.__LxAxAl
    def get_Ficha_Medica(self):
        return self.__Ficha_Medica

    def set_id(self,ids):
        self.__id=ids
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_Especie(self,especie):
        self.__Especie=especie
    def set_Fecha_Nacimiento(self,fecha_nacimiento):
        self.__Fecha_Nacimiento=fecha_nacimiento
    def set_sexo(self,sexo):
        self.__sexo=sexo
    def set_peso(self,peso):
        self.__peso=peso
    def set_LxAxAl(self,LxAxAl):
        self.__LxAxAl=LxAxAl
    def set_Ficha_Medica(self,ficha_medica):
        self.__Ficha_Medica=ficha_medica



#funcion main no esta definida y no existe
#getters y setters funcionan, sin embargo no guarda datos en el archivo y no se pudo llegar a la conclusion del funcionamiento de esta clase
