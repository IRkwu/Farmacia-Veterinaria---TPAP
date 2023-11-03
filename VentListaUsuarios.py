import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QDialog, QTableWidgetItem
from PyQt5.QtGui import QIntValidator, QIcon
from VentEditarUsuario import VentEditarUsuario

class VentListaUsuarios(object):
    def setupUi(self, VentListaUsuarios):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')

        VentListaUsuarios.setWindowIcon(IconoTitulo)
        
        VentListaUsuarios.resize(855, 565)
        VentListaUsuarios.setMinimumSize(QtCore.QSize(855, 565))
        VentListaUsuarios.setMaximumSize(QtCore.QSize(855, 565))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentListaUsuarios)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 855, 96))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(855, 96))

        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentListaUsuarios)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentListaUsuarios.close)
        
        # Tabla con columnas y filas y que sean 9 columnas [ID, Nombres, Apellidos, Genero, Fecha_Nacimiento, Rut, Telefono, Email, Domicilio]
        self.tableWidget = QtWidgets.QTableWidget(VentListaUsuarios)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 835, 342))
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setColumnHidden(6, True)
        
        # Para que no se puedan editar a no ser que se de click en el boton editar
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Boton editar y accion al pulsar
        self.btnEditar = QtWidgets.QPushButton(VentListaUsuarios)
        self.btnEditar.setGeometry(QtCore.QRect(20, 500, 121, 50))
        self.btnEditar.clicked.connect(self.onActionBtnEditar)
        
        # Boton eliminar y accion al pulsar
        self.btnEliminar = QtWidgets.QPushButton(VentListaUsuarios)
        self.btnEliminar.setGeometry(QtCore.QRect(160, 500, 121, 50))
        self.btnEliminar.clicked.connect(self.onActionBtnEliminar)
        
        # Etiqueta de instruccion para editar Usuarios
        self.mensajeEditarLabel = QtWidgets.QLabel(VentListaUsuarios)
        self.mensajeEditarLabel.setGeometry(QtCore.QRect(14, 94, 865, 50))
        
        # Etiqueta de instruccion para eliminar Usuarios
        self.mensajeEliminarLabel = QtWidgets.QLabel(VentListaUsuarios)
        self.mensajeEliminarLabel.setGeometry(QtCore.QRect(450, 94, 865, 50))
        
        self.retranslateUi(VentListaUsuarios)
        QtCore.QMetaObject.connectSlotsByName(VentListaUsuarios)
        
        # Cargar Usuarios del CSV
        self.cargarUsuarioCSV()
        
    # Metodo definir textos
    def retranslateUi(self, VentListaUsuarios):
        # Fuente de texto
        fuenteEstado = QtGui.QFont()
        fuenteEstado.setPointSize(9)
        fuenteEstado.setBold(True)
        self.mensajeEditarLabel.setFont(fuenteEstado)
        
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentListaUsuarios.setWindowTitle(_translate("VentListaUsuarios", "Listas de Usuarios"))
        self.btnEditar.setText(_translate("VentListaUsuarios", "Editar"))
        self.btnEliminar.setText(_translate("VentListaUsuarios", "Eliminar"))
        self.mensajeEditarLabel.setText(_translate("VentListaUsuarios", "Para editar el Usuario seleccione una fila y haga click en Editar"))
        self.mensajeEditarLabel.setFont(fuenteEstado)
        self.mensajeEliminarLabel.setText(_translate("VentListaUsuarios", "Para eliminar el Usuario seleccione una ID y haga click en Eliminar"))
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
                self.guardarUsuarios()
        else:
            self.alertBox("Por seguridad, debe seleccionar la ID para eliminar al Usuario", "Instrucciones para borrar")
        
    
    # Accion al clickear boton editar
    # Dentro del método onActionBtnEditar()
    def onActionBtnEditar(self):
        celda = self.tableWidget.currentItem() 
        if celda is None:
            self.alertBox("Debe seleccionar una celda", "Instrucciones para editar")
        else:
            columna = self.tableWidget.currentColumn()
            fila = self.tableWidget.currentRow()
            dialog = VentEditarUsuario(nombres=self.tableWidget.item(fila, 1).text(),
                                       apellidos=self.tableWidget.item(fila, 2).text(),
                                       genero=self.tableWidget.item(fila, 3).text(),
                                       telefono=self.tableWidget.item(fila, 8).text(),
                                       email=self.tableWidget.item(fila, 5).text(),
                                       domicilio=self.tableWidget.item(fila, 9).text(),
                                       cargo=self.tableWidget.item(fila, 10).text())
            if dialog.exec_() == QDialog.Accepted:
                nombres = dialog.get_nombres()
                apellidos = dialog.get_apellidos()
                genero = dialog.get_genero()
                telefono = dialog.get_telefono()
                email = dialog.get_email()
                domicilio = dialog.get_domicilio()
                password = dialog.get_password()
                cargo = dialog.get_cargo()
                
                # Asignar los nuevos valores a la fila seleccionada en la tabla
                self.tableWidget.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(nombres)))
                self.tableWidget.setItem(fila, 2, QtWidgets.QTableWidgetItem(apellidos))
                self.tableWidget.setItem(fila, 3, QtWidgets.QTableWidgetItem(genero))
                self.tableWidget.setItem(fila, 5, QtWidgets.QTableWidgetItem(email))
                self.tableWidget.setItem(fila, 8, QtWidgets.QTableWidgetItem(telefono))
                self.tableWidget.setItem(fila, 9, QtWidgets.QTableWidgetItem(domicilio))
                self.tableWidget.setItem(fila, 6, QtWidgets.QTableWidgetItem(password))
                self.tableWidget.setItem(fila, 10, QtWidgets.QTableWidgetItem(cargo))
                self.guardarUsuarios()
            
    # Accion al clickear boton guardar
    def guardarUsuarios(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Usuario.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Escribe los encabezados de las columnas
            encabezados = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
            writer.writerow(encabezados)
            # Sobreescribe los datos de los Usuarios con los nuevos valores (Usuario editado o eliminado)
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

    # Metodo para que cargue los Usuarios desde el archivo CSV
    def cargarUsuarioCSV(self):
        # Abre el archivo CSV con codificación UTF-8
        with open('ArchivosCSV/Usuario.csv', newline='') as csvfile:
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

        # Ajusta el tamaño de las celdas automáticamente
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