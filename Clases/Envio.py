
#Clase Envio Revisada

class Envio:
    def __init__(self, id_envio:int, Fecha_Compra:str, Fecha_Llegada:str):
        self.__id_envio=id_envio
        self.__Fecha_Compra=Fecha_Compra
        self.__Fecha_Llegada=Fecha_Llegada
        pass


    #Getters y Setters
    def get_idEnvio(self):
        return self.__id_envio
    def get_Fecha_Compra(self):
        return self.__Fecha_Compra
    def get_Fecha_llegada(self):
        return self.__Fecha_Llegada

    def set_idEnvio(self,id_envio):
        self.__id_envio
    def set_Fecha_Compra(self,fecha_compra):
        self.__Fecha_Compra=fecha_compra
    def set_Fecha_llegada(self,fecha_llegada):
        self.__Fecha_Llegada=fecha_llegada



#falta "herencia" con carrito para pasar las cosas que se compraron
#funcion main no esta definida y no existe
#"clase incompleta", (falta agregar algunos detalles ver problema general de farmacia veterinaria)