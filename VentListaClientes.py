import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QDialog, QTableWidgetItem
from PyQt5.QtGui import QIntValidator, QIcon
from VentEditarCliente import VentEditarCliente

class VentListaClientes(object):
    def setupUi(self, VentListaClientes):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')

        VentListaClientes.setWindowIcon(IconoTitulo)
        
        VentListaClientes.resize(865, 565)
        VentListaClientes.setMinimumSize(QtCore.QSize(865, 565))
        VentListaClientes.setMaximumSize(QtCore.QSize(865, 565))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentListaClientes)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 865, 96))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(865, 96))

        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentListaClientes)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentListaClientes.close)
        
        # Tabla con columnas y filas y que sean 9 columnas [ID, Nombres, Apellidos, Genero, Fecha_Nacimiento, Rut, Telefono, Email, Domicilio]
        self.tableWidget = QtWidgets.QTableWidget(VentListaClientes)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 845, 342))
        self.tableWidget.setColumnCount(9)
        
        # Para que no se puedan editar a no ser que se de click en el boton editar
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Boton editar y accion al pulsar
        self.btnEditar = QtWidgets.QPushButton(VentListaClientes)
        self.btnEditar.setGeometry(QtCore.QRect(20, 500, 121, 50))
        self.btnEditar.clicked.connect(self.onActionBtnEditar)
        
        # Boton eliminar y accion al pulsar
        self.btnEliminar = QtWidgets.QPushButton(VentListaClientes)
        self.btnEliminar.setGeometry(QtCore.QRect(160, 500, 121, 50))
        self.btnEliminar.clicked.connect(self.onActionBtnEliminar)
        
        # Etiqueta de instruccion para editar clientes
        self.mensajeEditarLabel = QtWidgets.QLabel(VentListaClientes)
        self.mensajeEditarLabel.setGeometry(QtCore.QRect(14, 94, 865, 50))
        
        # Etiqueta de instruccion para eliminar clientes
        self.mensajeEliminarLabel = QtWidgets.QLabel(VentListaClientes)
        self.mensajeEliminarLabel.setGeometry(QtCore.QRect(460, 94, 865, 50))
        
        self.retranslateUi(VentListaClientes)
        QtCore.QMetaObject.connectSlotsByName(VentListaClientes)
        
        # Cargar Clientes del CSV
        self.cargarClienteCSV()
        
    # Metodo definir textos
    def retranslateUi(self, VentListaClientes):
        # Fuente de texto
        fuenteEstado = QtGui.QFont()
        fuenteEstado.setPointSize(9)
        fuenteEstado.setBold(True)
        self.mensajeEditarLabel.setFont(fuenteEstado)
        
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentListaClientes.setWindowTitle(_translate("VentListaClientes", "Listas de Clientes"))
        self.btnEditar.setText(_translate("VentListaClientes", "Editar"))
        self.btnEliminar.setText(_translate("VentListaClientes", "Eliminar"))
        self.mensajeEditarLabel.setText(_translate("VentListaClientes", "Para editar el cliente seleccione una fila y haga click en Editar"))
        self.mensajeEditarLabel.setFont(fuenteEstado)
        self.mensajeEliminarLabel.setText(_translate("VentListaClientes", "Para eliminar el cliente seleccione una ID y haga click en Eliminar"))
        self.mensajeEliminarLabel.setFont(fuenteEstado)
        
        
    # Accion al clickear boton eliminar
    def onActionBtnEliminar(self):
    # Obtiene la fila y columna seleccionadas
        fila = self.tableWidget.currentRow()
        columna = self.tableWidget.currentColumn()
        if columna == 0:  # Verifica si la columna es la del ID
            if fila != -1:
                # Elimina la fila seleccionada
                self.tableWidget.removeRow(fila)
                self.guardarClientes()
        else:
            self.alertBox("Por seguridad, debe seleccionar la ID para eliminar al Cliente", "Instrucciones para borrar")
        
    
    # Accion al clickear boton editar
    def onActionBtnEditar(self):
        celda = self.tableWidget.currentItem() 
        if celda is None:
            self.alertBox("Debe seleccionar una celda", "Instrucciones para editar")
        else:
            columna = self.tableWidget.currentColumn()
            fila = self.tableWidget.currentRow()
            dialog = VentEditarCliente(nombres=self.tableWidget.item(fila, 1).text(),
                                       apellidos=self.tableWidget.item(fila, 2).text(),
                                       genero=self.tableWidget.item(fila, 3).text(),
                                       telefono=self.tableWidget.item(fila, 7).text(),
                                       email=self.tableWidget.item(fila, 5).text(),
                                       domicilio=self.tableWidget.item(fila, 8).text())
            if dialog.exec_() == QDialog.Accepted:
                nombres = dialog.get_nombres()
                apellidos = dialog.get_apellidos()
                genero = dialog.get_genero()
                telefono = dialog.get_telefono()
                email = dialog.get_email()
                domicilio = dialog.get_domicilio()
                
                # Asignar los nuevos valores a la fila seleccionada en la tabla
                self.tableWidget.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(nombres)))
                self.tableWidget.setItem(fila, 2, QtWidgets.QTableWidgetItem(apellidos))
                self.tableWidget.setItem(fila, 3, QtWidgets.QTableWidgetItem(genero))
                self.tableWidget.setItem(fila, 5, QtWidgets.QTableWidgetItem(email))
                self.tableWidget.setItem(fila, 7, QtWidgets.QTableWidgetItem(telefono))
                self.tableWidget.setItem(fila, 8, QtWidgets.QTableWidgetItem(domicilio))
                self.guardarClientes()
                
    # Accion al guardar
    def guardarClientes(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Cliente.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Escribe los encabezados de las columnas
            encabezados = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
            writer.writerow(encabezados)
            # Sobreescribe los datos de los clientes con los nuevos valores (Cliente editado o eliminado)
            for fila in range(self.tableWidget.rowCount()):
                datos_de_la_fila = []
                for columna in range(self.tableWidget.columnCount()):
                    celda = self.tableWidget.item(fila, columna)
                    if celda is not None:
                        datos_de_la_fila.append(celda.text())
                    else:
                        datos_de_la_fila.append('')
                writer.writerow(datos_de_la_fila)
        # Mensaje de que los cambios se guardaron correctamente
        self.alertBox("Se han guardado los cambios exitosamente!", "Se han completado los cambios")

    # Metodo para que cargue los clientes desde el archivo CSV
    def cargarClienteCSV(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Cliente.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            #  Lee la primera fila como los encabezados de las columnas y los posiciona en el tableWidget
            encabezados = next(reader)
            self.tableWidget.setHorizontalHeaderLabels(encabezados)
            # Recorre las filas para obtener los datos que se muestran en el tableWidget
            for fila in reader:
                posicionFila = self.tableWidget.rowCount()
                self.tableWidget.insertRow(posicionFila)
                for columna, value in enumerate(fila):
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tableWidget.setItem(posicionFila, columna, item)
                    
        # Ajusta el tamaño de las celdas automaticamente
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
    # Mensajes de alerta, Vent emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()