import csv
import random

class Boleta:
    def __init__(self, numero_boleta, fecha, cliente, rut, productos, cant_productos, subtotal, descuento, costo_envio, total):
        self.numero_boleta = numero_boleta
        self.fecha = fecha
        self.cliente = cliente
        self.rut = rut
        self.productos = productos
        self.cant_productos = cant_productos
        self.subtotal = subtotal
        self.descuento = descuento
        self.costo_envio = costo_envio
        self.total = total
    
    def get_numero_boleta(self):
        return self.numero_boleta
    
    def set_numero_boleta(self, numero_boleta):
        self.numero_boleta = numero_boleta
    
    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self, fecha):
        self.fecha = fecha
    
    def get_cliente(self):
        return self.cliente
    
    def set_cliente(self, cliente):
        self.cliente = cliente
        
    def get_rut(self):
        return self.rut
    
    def set_rut(self, rut):
        self.rut = rut
    
    def get_productos(self):
        return self.productos
    
    def set_productos(self, productos):
        self.productos = productos
    
    def get_cant_productos(self):
        return self.cant_productos
    
    def set_cant_productos(self, cant_productos):
        self.cant_productos = cant_productos
    
    def get_subtotal(self):
        return self.subtotal
    
    def set_subtotal(self, subtotal):
        self.subtotal = subtotal
    
    def get_descuento(self):
        return self.descuento
    
    def set_descuento(self, descuento):
        self.descuento = descuento
    
    def get_costo_envio(self):
        return self.costo_envio
    
    def set_costo_envio(self, costo_envio):
        self.costo_envio = costo_envio
    
    def get_total(self):
        return self.total
    
    def set_total(self, total):
        self.total = total
        
    def cargarBoletasCSV(self):
        boletas = []
        try:
            with open('ArchivosCSV/Boletas.csv', 'r') as archivo:
                reader = csv.reader(archivo)
                next(reader)  # Ignorar la primera línea de encabezados
                for row in reader:
                    boleta = Boleta(
                        numero_boleta=row[0],
                        fecha=row[1],
                        cliente=row[2],
                        rut=row[3],
                        productos=row[4],
                        cant_productos=row[5],
                        subtotal=row[6],
                        descuento=row[7],
                        costo_envio=row[8],
                        total=row[9]
                    )
                    boletas.append(boleta)
        except Exception as e:
            print("Error al cargar las boletas desde el archivo CSV:", str(e))
        return boletas

    def guardarBoletasCSV(self, boletas):
        try:
            with open('ArchivosCSV/Boletas.csv', 'w', newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow([
                    "Numero Boleta",
                    "Fecha",
                    "Cliente",
                    "Rut",
                    "Productos",
                    "Cantidad Productos",
                    "Subtotal",
                    "Descuento",
                    "Costo Envio",
                    "Total"
                ])
                for boleta in boletas:
                    writer.writerow([
                        boleta.get_numero_boleta(),
                        boleta.get_fecha(),
                        boleta.get_cliente(),
                        boleta.get_rut(),
                        boleta.get_productos(),
                        boleta.get_cant_productos(),
                        boleta.get_subtotal(),
                        boleta.get_descuento(),
                        boleta.get_costo_envio(),
                        boleta.get_total()
                    ])
        except Exception as e:
            print("Error al guardar las boletas en el archivo CSV:", str(e))

    def agregarBoleta(self, fecha, cliente, rut, productos, cant_productos, subtotal, descuento, costo_envio, total):
        try:
            with open('ArchivosCSV/Boletas.csv', 'a', newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow([random.sample(range(100000000, 999999999), 1)[0] ,fecha, cliente, rut, productos, cant_productos, subtotal, descuento, costo_envio, total])
        except Exception as e:
            print("Error al agregar la boleta al archivo CSV:", str(e))

    
boletas = Boleta.cargarBoletasCSV(None)