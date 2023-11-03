import csv

class Medicamentos:
    def __init__(self, ID: str, Nombre_Medicamento: str, Precio: int, Stock: int, Descripcion: str, Lote1: int, caducidadLote1: str, Lote2: int, caducidadLote2: str, tipo:str, fecha_entrega:str):
        self.__ID = ID
        self.__Nombre_Medicamento = Nombre_Medicamento
        self.__Precio = Precio
        self.__Stock = Stock
        self.__Descripcion = Descripcion
        self.__Lote1 = Lote1
        self.__caducidadLote1 = caducidadLote1
        self.__Lote2 = Lote2
        self.__caducidadLote2 = caducidadLote2
        self.__tipo = tipo
        self.__fecha_entrega = fecha_entrega
    # Getters
    def get_id(self):
        return self.__ID

    def get_nombre(self):
        return self.__Nombre_Medicamento

    def get_precio(self):
        return self.__Precio

    def get_stock(self):
        return self.__Stock

    def get_descripcion(self):
        return self.__Descripcion

    def get_lote1(self):
        return self.__Lote1

    def get_vencL1(self):
        return self.__caducidadLote1

    def get_lote2(self):
        return self.__Lote2

    def get_vencL2(self):
        return self.__caducidadLote2
    
    def get_tipo(self):
        return self.__tipo
    
    def get_fecha_entrega(self):
        return self.__fecha_entrega

    # Setters
    def set_id(self, ID):
        self.__ID = ID

    def set_nombre(self, Nombre_Medicamento):
        self.__Nombre_Medicamento = Nombre_Medicamento

    def set_precio(self, Precio):
        self.__Precio = Precio

    def set_stock(self, Stock):
        self.__Stock = Stock

    def set_descripcion(self, Descripcion):
        self.__Descripcion = Descripcion

    def set_lote1(self, Lote1):
        self.__Lote1 = Lote1

    def set_vencL1(self, caducidadLote1):
        self.__caducidadLote1 = caducidadLote1

    def set_lote2(self, Lote2):
        self.__Lote2 = Lote2

    def set_vencL2(self, caducidadLote2):
        self.__caducidadLote2 = caducidadLote2
        
    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def set_fecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = fecha_entrega
             
    def guardar_medicamentos_CSV(self, lista_medicamentos):
        with open('ArchivosCSV/Medicamentos.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['ID', 'Nombre', 'Precio', 'Stock', 'Descripcion', 'Lote 1', 'Caducidad Lote 1', 'Lote 2', 'Caducidad Lote 2', "Tipo de Medicamento"])
            for medicamento in lista_medicamentos:
                writer.writerow([medicamento.ID, medicamento.Nombre_Medicamento, medicamento.Precio, medicamento.Stock, medicamento.Descripcion,
                                 medicamento.Lote1, medicamento.caducidadLote1, medicamento.Lote2, medicamento.caducidadLote2, medicamento.tipo, medicamento.fecha_entrega])
                
    def cargar_medicamentos_CSV(self):
        lista_medicamentos = []
        with open('ArchivosCSV/Medicamentos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                ID, Nombre_Medicamento, Precio, Stock, Descripcion, Lote1, caducidadL1, Lote2, caducidadLote2, tipo, fecha_entrega = row
                medicamento = Medicamentos(ID, Nombre_Medicamento, Precio, Stock, Descripcion, Lote1, caducidadL1, Lote2, caducidadLote2, tipo, fecha_entrega)
                lista_medicamentos.append(medicamento)
                
        ultimo_id = max(int(medicamento.get_id()) for medicamento in lista_medicamentos)
        return lista_medicamentos, ultimo_id
    
    def agregar_medicamentos(nombre, precio, descripcion, tipo):
        lista_medicamentos, ultimo_id = Medicamentos.cargar_medicamentos_CSV(None)

        # Si hay una id disponible antes de la ultima utiliza el slot libre
        id_disponible = None
        for i in range(1, ultimo_id+2):
            if not any(int(medicamento.get_id()) == i for medicamento in lista_medicamentos):
                id_disponible = str(i)
                break

        if id_disponible is None:
            id_disponible = str(ultimo_id + 1)

        medicamento = Medicamentos(id_disponible, nombre, precio, 0, descripcion, 0, "", 0, "", tipo, fecha_entrega)
        medicamento.Nombre_Medicamento = nombre
        medicamento.Precio = precio
        medicamento.Descripcion = descripcion
        medicamento.Tipo = tipo
        medicamento.Fecha_Entrega = fecha_entrega

        lista_medicamentos.append(medicamento)

        # Guarda solo el medicamento agregado en el archivo CSV
        with open('ArchivosCSV/Medicamentos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([medicamento.get_id(), medicamento.get_nombre(), medicamento.get_precio(), medicamento.get_stock(), medicamento.get_descripcion(), medicamento.get_lote1(), medicamento.get_vencL1(), medicamento.get_lote2(), medicamento.get_vencL2(), medicamento.get_tipo(), medicamento.get_fecha_entrega()])
    
# Inicializar la lista de medicamentos

lista_medicamentos = Medicamentos.cargar_medicamentos_CSV(None)
