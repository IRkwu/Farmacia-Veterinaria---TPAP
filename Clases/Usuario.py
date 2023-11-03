
from datetime import date #esto es para la fecha
import random
import csv

class Usuario:
    def __init__(self,id:int,nombres:str,apellidos:str,genero:str,fecha_nacimiento:str,email:str,password:str,rut:str,telefono:str,domicilio:str,cargo:str):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__genero = genero
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email
        self.__password = password
        self.__rut = rut
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.__cargo = cargo

    # Getters
    def get_id(self) -> int:
        return self.__id

    def get_nombres(self) -> str:
        return self.__nombres

    def get_apellidos(self) -> str:
        return self.__apellidos

    def get_genero(self) -> str:
        return self.__genero

    def get_fecha_nacimiento(self) -> str:
        return self.__fecha_nacimiento

    def get_email(self) -> str:
        return self.__email
    
    def get_password(self) -> str:
        return self.__password

    def get_rut(self) -> str:
        return self.__rut

    def get_telefono(self) -> str:
        return self.__telefono

    def get_domicilio(self) -> str:
        return self.__domicilio

    def get_cargo(self) -> str:
        return self.__cargo

    # Setters
    def set_id(self):
        self.__id = random.randint(1000, 9999)

    def set_nombres(self, nombres:str):
        self.__nombres = nombres

    def set_apellidos(self, apellidos:str):
        self.__apellidos = apellidos

    def set_genero(self, genero:str):
        self.__genero = genero

    def set_fecha_nacimiento(self, fecha_nacimiento:str):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_email(self, email:str):
        self.__email = email
        
    def set_password(self, password:str):
        self.__password = password

    def set_rut(self, rut:str):
        self.__rut = rut

    def set_telefono(self, telefono:str):
        self.__telefono = telefono

    def set_domicilio(self, domicilio:str):
        self.__domicilio = domicilio

    def set_cargo(self, cargo:str):
        self.__cargo = cargo


    def agregar_usuario(nombres, apellidos, domicilio, genero, fecha_nacimiento, rut, email, password, telefono, cargo):
        # Crea una lista para almacenar los objetos Usuario
        usuarios = []
        # Pide al usuario que ingrese los datos de los usuarios
        for i in range(1):
            usuario = Usuario(id=int,nombres=str,apellidos=str,genero=str,fecha_nacimiento=str,email=str,password=str,rut=str,telefono=str,domicilio=str,cargo=str)
            usuario.set_id()    #se le setea un numero random, porque llamamos a la funcion set_id()
            usuario.set_nombres(nombres)
            usuario.set_apellidos(apellidos)
            usuario.set_genero(genero)
            usuario.set_fecha_nacimiento(fecha_nacimiento)
            usuario.set_email(email)
            usuario.set_password(password)
            usuario.set_rut(rut)
            usuario.set_telefono(telefono)
            usuario.set_domicilio(domicilio)
            usuario.set_cargo(cargo)

            # Verifica que el ID no se repita
            while any(usuario.get_id() == c.get_id() for c in usuarios): 
              usuario.set_id()  #Cada vez que un ID se repita a otro, entonces, entrara en este ciclo y no saldra hasta que el id setiado no se a = otro

            usuarios.append(usuario)

        #Sirve para crear los encabezados solo cuando se crea el archivo por primera vez
        try:
            with open ('ArchivosCSV/Usuario.csv', mode ='x', newline='') as file:
                escritor_csv= csv.writer(file)
                escritor_csv.writerow(['ID', 'Nombres', 'Apellidos', 'Genero', 'Fecha de Nacimiento', 'Correo Electronico', 'Contraseña', 'RUT', 'Telefono', 'Domicilio', 'Cargo'])
        except FileExistsError:
                pass
            
        # Abre el archivo CSV en modo de escritura
        with open('ArchivosCSV/Usuario.csv', mode='a', newline='') as file:
        
          # Crea el objeto writer
          writer = csv.writer(file)

          # Escribe los encabezados 
          #writer.writerow(['ID', 'Nombres', 'Apellidos', 'Genero', 'Fecha de Nacimiento', 'Correo Electronico', 'RUT', 'Telefono', 'Domicilio', 'Cargo'])

          # Escribe los datos de los usuarios
          for usuario in usuarios:
              writer.writerow([usuario.get_id(), usuario.get_nombres(), usuario.get_apellidos(), usuario.get_genero(), usuario.get_fecha_nacimiento(), usuario.get_email(), usuario.get_password(), usuario.get_rut(), usuario.get_telefono(), usuario.get_domicilio(), usuario.get_cargo()])

    def cargarUsuarioCSV():
        try:
            with open('ArchivosCSV/Usuario.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Omite la primera línea que contiene los encabezados
                for row in reader:
                    id, nombres, apellidos, genero, fecha_nacimiento, email, password, rut, telefono, domicilio, cargo = row[:11]
                    usuario = Usuario(int(id), nombres, apellidos, genero, fecha_nacimiento, email, password, rut, telefono, domicilio, cargo)
                    usuarios.append(usuario)
        except FileNotFoundError:
            print("El archivo CSV no existe.")

    def editar_usuario(id_usuario, nuevos_datos):
        # Buscar el usuario por su ID
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.get_id() == id_usuario:
                usuario_encontrado = usuario
                break
            
        if usuario_encontrado:
            # Actualizar los atributos del usuario con los nuevos datos
            if 'nombres' in nuevos_datos:
                usuario_encontrado.set_nombres(nuevos_datos['nombres'])
            if 'apellidos' in nuevos_datos:
                usuario_encontrado.set_apellidos(nuevos_datos['apellidos'])
            if 'genero' in nuevos_datos:
                usuario_encontrado.set_genero(nuevos_datos['genero'])
            if 'fecha_nacimiento' in nuevos_datos:
                usuario_encontrado.set_fecha_nacimiento(nuevos_datos['fecha_nacimiento'])
            if 'email' in nuevos_datos:
                usuario_encontrado.set_email(nuevos_datos['email'])
            if 'password' in nuevos_datos:
                usuario_encontrado.set_password(nuevos_datos['password'])
            if 'rut' in nuevos_datos:
                usuario_encontrado.set_rut(nuevos_datos['rut'])
            if 'telefono' in nuevos_datos:
                usuario_encontrado.set_telefono(nuevos_datos['telefono'])
            if 'domicilio' in nuevos_datos:
                usuario_encontrado.set_domicilio(nuevos_datos['domicilio'])
            if 'cargo' in nuevos_datos:
                usuario_encontrado.set_cargo(nuevos_datos['cargo'])

            # Guardar los cambios en el archivo CSV
            guardar_usuarios_csv()

            print("Usuario actualizado correctamente.")
        else:
            print("No se encontró ningún usuario con el ID especificado.")
            
    def guardar_usuarios_csv():
        with open('ArchivosCSV/Usuario.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nombres', 'Apellidos', 'Genero', 'Fecha de Nacimiento', 'Correo Electronico', 'Contraseña', 'RUT', 'Telefono', 'Domicilio', 'Cargo'])
            for usuario in usuarios:
                writer.writerow([usuario.get_id(), usuario.get_nombres(), usuario.get_apellidos(), usuario.get_genero(), usuario.get_fecha_nacimiento(), usuario.get_email(), usuario.get_password(), usuario.get_rut(), usuario.get_telefono(), usuario.get_domicilio(), usuario.get_cargo()])
    
# Crea una lista para almacenar los objetos Usuario
usuarios = []
