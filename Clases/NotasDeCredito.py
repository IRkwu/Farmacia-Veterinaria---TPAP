import csv
import random

class NotasDeCredito:
    def __init__(self, numero_nota, fecha, cliente, rut, producto, precio):
        self.numero_nota = numero_nota
        self.fecha = fecha
        self.cliente = cliente
        self.rut = rut
        self.producto = producto
        self.precio = precio
    
    def get_numero_nota(self):
        return self.numero_nota
    
    def set_numero_nota(self, numero_nota):
        self.numero_nota = numero_nota
    
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
    
    def get_producto(self):
        return self.producto
    
    def set_producto(self, producto):
        self.producto = producto
    
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio
        
    def cargarNotasDeCreditosCSV(self):
        nota_de_creditos = []
        try:
            with open('ArchivosCSV/NotasDeCreditos.csv', 'r') as archivo:
                reader = csv.reader(archivo)
                next(reader)  # Ignorar la primera línea de encabezados
                for row in reader:
                    nota_de_credito = NotasDeCredito(
                        numero_nota=row[0],
                        fecha=row[1],
                        cliente=row[2],
                        rut=row[3],
                        producto=row[4],
                        precio=row[5],
                    )
                    nota_de_creditos.append(nota_de_credito)
        except Exception as e:
            print("Error al cargar las nota_de_creditos desde el archivo CSV:", str(e))
        return nota_de_creditos

    def guardarNotasDeCreditosCSV(self, nota_de_creditos):
        try:
            with open('ArchivosCSV/NotasDeCreditos.csv', 'w', newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow([
                    "Numero NotasDeCredito",
                    "Fecha",
                    "Cliente",
                    "Rut",
                    "Producto",
                    "Precio",
                ])
                for nota_de_credito in nota_de_creditos:
                    writer.writerow([
                        nota_de_credito.get_numero_nota(),
                        nota_de_credito.get_fecha(),
                        nota_de_credito.get_cliente(),
                        nota_de_credito.get_rut(),
                        nota_de_credito.get_producto(),
                        nota_de_credito.get_precio(),
                    ])
        except Exception as e:
            print("Error al guardar las nota_de_creditos en el archivo CSV:", str(e))

    def agregarNotasDeCredito(self, fecha, cliente, rut, producto, precio):
        try:
            with open('ArchivosCSV/NotasDeCreditos.csv', 'a', newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow([random.sample(range(100000000, 999999999), 1)[0] ,fecha, cliente, rut, producto, precio])
        except Exception as e:
            print("Error al agregar la nota_de_credito al archivo CSV:", str(e))

    
#notas_de_credito = NotasDeCredito.cargarNotasDeCreditosCSV(None)
#if len(notas_de_credito) > 0:
#    for i, nota_de_credito in enumerate(notas_de_credito):
#        print("Nota de Credito número", i + 1, ":")
#        print("Fecha:", nota_de_credito.get_fecha())
#        print("Rut:",nota_de_credito.get_rut())
#        print("Cliente:", nota_de_credito.get_cliente())
#        print("Producto:", nota_de_credito.get_producto())
#        print("Precio:", nota_de_credito.get_precio())
#        print()  # Agregar una línea en blanco entre nota_de_creditos
#else:
#    print("No hay nota_de_creditos cargadas en el archivo CSV.")
#    
#NotasDeCredito.agregarNotasDeCredito(None, "30/07/2003", "Alvaro", "21.354.784-4", "Lomper", "$20900")