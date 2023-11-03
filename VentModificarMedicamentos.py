from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox, QDialog
import csv, datetime
from VentAgregarStock import AgregarStockDialog
from VentAgregarMedicamento import AgregarMedicamentos


class VentModificarMedicamentos(object):
    def __init__(self):
        self.carrito = []  # Lista para almacenar los medicamentos del carrito
    
    def setupUi(self, VentModificarMedicamentos):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_modificar_stock.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentModificarMedicamentos.setWindowIcon(IconoTitulo)
        
        VentModificarMedicamentos.resize(1048, 631)
        VentModificarMedicamentos.setMinimumSize(QtCore.QSize(1048, 631))
        VentModificarMedicamentos.setMaximumSize(QtCore.QSize(1048, 631))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentModificarMedicamentos)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 1048, 100))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(1048, 100))
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentModificarMedicamentos)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentModificarMedicamentos.close)

        # Tabla con columnas y filas y que sean 10 columnas
        self.tableWidget = QtWidgets.QTableWidget(VentModificarMedicamentos)
        self.tableWidget.setGeometry(QtCore.QRect(10, 166, 844, 450))
        self.tableWidget.setColumnCount(11)
                
        # Ocultar columnas
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnHidden(5, True)
        self.tableWidget.setColumnHidden(6, True)
        self.tableWidget.setColumnHidden(7, True)
        self.tableWidget.setColumnHidden(8, True)
        
        # Para que no se puedan editar los medicamentos de la lista de medicamentos
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Boton informacion y accion al pulsar
        self.btnInfo = QtWidgets.QPushButton(VentModificarMedicamentos)
        self.btnInfo.setGeometry(QtCore.QRect(861, 166, 180, 60))
        self.btnInfo.clicked.connect(self.onActionBtnInfo)
        
        # Boton agregar medicamentos y accion al pulsar
        self.btnAgregar = QtWidgets.QPushButton(VentModificarMedicamentos)
        self.btnAgregar.setGeometry(QtCore.QRect(861, 246, 180, 60))
        self.btnAgregar.clicked.connect(self.onActionBtnAgregar)
        
        # Boton borrar medicamentos y accion al pulsar
        self.btnBorrar = QtWidgets.QPushButton(VentModificarMedicamentos)
        self.btnBorrar.setGeometry(QtCore.QRect(861, 326, 180, 60))
        self.btnBorrar.clicked.connect(self.onActionBtnBorrar)
        
        # Boton revisar medicamentos experimentales y accion al pulsar
        self.btnRevisarTipo = QtWidgets.QPushButton(VentModificarMedicamentos)
        self.btnRevisarTipo.setGeometry(QtCore.QRect(861, 406, 180, 60))
        self.btnRevisarTipo.clicked.connect(self.onActionBtnRevisarTipo)
        
        # Barra de busqueda y accion al actualizar el texto
        self.buscarLineEdit = QtWidgets.QLineEdit(VentModificarMedicamentos)
        self.buscarLineEdit.setGeometry(QtCore.QRect(10, 106, 1030, 50))
        self.buscarLineEdit.setPlaceholderText("Ingrese el nombre, tipo o ID del medicamento")
        self.buscarLineEdit.setStyleSheet("font-size: 16px;")
        self.buscarLineEdit.textChanged.connect(self.buscarMedicamentos)

        self.retranslateUi(VentModificarMedicamentos)
        QtCore.QMetaObject.connectSlotsByName(VentModificarMedicamentos)
        
        # Cargar lista de medicamentos del CSV y actualiar datos (subtotal, total, entre otros)
        self.cargarMedicamentosCSV()
        
    # Metodo definir textos
    def retranslateUi(self, VentModificarMedicamentos):
        _translate = QtCore.QCoreApplication.translate
        VentModificarMedicamentos.setWindowTitle(_translate("VentModificarMedicamentos", "Modificar Medicamentos"))
        self.btnAgregar.setText(_translate("VentModificarMedicamentos", "Agregar Nuevo\nMedicamento (+)"))
        self.btnBorrar.setText(_translate("VentModificarMedicamentos", "Borrar Medicamento (-)"))
        self.btnInfo.setText(_translate("VentModificarMedicamentos", "Instrucciones (!)"))
        self.btnRevisarTipo.setText(_translate("VentModificarMedicamentos", "Revisar Medicamentos\nExperimentales (!!!)"))

    # Metodo para que cargue los clientes desde el archivo CSV
    def cargarMedicamentosCSV(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Medicamentos.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            #  Lee la primera fila como los encabezados de las columnas y los posiciona en el tableWidget
            encabezados = next(reader)
            self.tableWidget.setHorizontalHeaderLabels(encabezados)
            # Recorre las filas para obtener los datos que se muestran en el tableWidget
            for fila in reader:
                posicionFila = self.tableWidget.rowCount()
                self.tableWidget.insertRow(posicionFila)
                # Recorre las columnas para obtener los datos que se muestran en el tableWidget
                for columna, value in enumerate(fila):
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tableWidget.setItem(posicionFila, columna, item)
                    
        self.ajustarCeldas()
        
    # Mensajes de alerta, Vent emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()

    # Metodo para la barra de busqueda
    def buscarMedicamentos(self):
        # Busca los medicamentos que coinciden con la búsqueda y los muestra en la tabla
        texto = self.buscarLineEdit.text().strip().lower()
        if texto:
            for i in range(self.tableWidget.rowCount()):
                found = False
                id_medicamento = self.tableWidget.item(i, 0)
                nombre_medicamento = self.tableWidget.item(i, 1)
                tipo_medicamento = self.tableWidget.item(i, 9)
                # Si la id del medicamento existe la muestra
                if id_medicamento and texto in id_medicamento.text().lower():
                    found = True
                # Si el nombre del medicamento existe la muestra
                elif nombre_medicamento and texto in nombre_medicamento.text().lower():
                    found = True
                elif tipo_medicamento and texto in tipo_medicamento.text().lower():
                    found = True
                # Oculta los elementos que no tengan texto o numeros similares a los ingresados
                self.tableWidget.setRowHidden(i, not found)
        else:
            # Muestra todas las filas si no se ha ingresado ningún texto
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(i, False)
                
    # Accion al pulsar boton agregar, agrega medicamentos a la tableWidget de medicamentos
    def onActionBtnAgregar(self):
        dialog = AgregarMedicamentos()
        if dialog.exec_() == QDialog.Accepted:
            id = dialog.get_id()
            nombre = dialog.get_nombre()
            precio = dialog.get_precio()
            descripcion = dialog.get_descripcion()
            tipo = dialog.get_tipo()
            fecha_entrega = dialog.get_fecha_entrega()
            lote_inicial = dialog.get_lote_inicial()
            fecha_caducidad = dialog.get_fecha_caducidad()

            # Crea una nueva fila en la tabla
            posicionFila = self.tableWidget.rowCount()
            self.tableWidget.insertRow(posicionFila)

            # Agrega los datos a las celdas de la nueva fila
            self.tableWidget.setItem(posicionFila, 0, QTableWidgetItem(id))
            self.tableWidget.setItem(posicionFila, 1, QTableWidgetItem(nombre))
            self.tableWidget.setItem(posicionFila, 2, QTableWidgetItem(precio))
            self.tableWidget.setItem(posicionFila, 4, QTableWidgetItem(descripcion))
            self.tableWidget.setItem(posicionFila, 5, QTableWidgetItem(lote_inicial))
            self.tableWidget.setItem(posicionFila, 6, QTableWidgetItem(fecha_caducidad))
            self.tableWidget.setItem(posicionFila, 7, QTableWidgetItem("0"))
            self.tableWidget.setItem(posicionFila, 3, QTableWidgetItem(lote_inicial))
            self.tableWidget.setItem(posicionFila, 9, QTableWidgetItem(tipo))
            self.tableWidget.setItem(posicionFila, 10, QTableWidgetItem(fecha_entrega))
            
            self.ajustarCeldas()
            self.guardarMedicamentos()

    # Accion al pulsar boton borrar, elimina medicamentos de la tableWidget
    def onActionBtnBorrar(self):
        fila_seleccionada = self.tableWidget.currentRow()
        columna = self.tableWidget.currentColumn()
        
        if fila_seleccionada == -1:
            self.alertBox("Debe seleccionar un medicamento para borrarlo", "Borrar Medicamento")
        
        # Si se ha seleccionado un medicamento
        if columna == 0:
            if fila_seleccionada != -1:
                medicamento = self.tableWidget.item(fila_seleccionada, 1).text()

                # Eliminar el medicamento de la lista
                self.tableWidget.removeRow(fila_seleccionada)

                self.guardarMedicamentos()
                self.alertBox("Se ha eliminado el medicamento correctamente", "Eliminar Medicamento")
        else:
            self.alertBox("Debe seleccionar la 'ID' para borrar el medicamento", "Instrucciones para borrar")
            
    def onActionBtnInfo(self):
        self.alertBox("- Para agregar nuevo medicamento debe hacer click en Agregar Nuevo Medicamento\n\n"
                      "- Para borrar un medicamento debe seleccionar su ID desde la lista de medicamentos y hacer click en Borrar Medicamento\n\n"
                      "- Para ver los medicamentos experimentales y su fecha de entrega debe hacer click en Revisar Medicamentos Experimentales", "Lista de Instrucciones")
        
    def onActionBtnRevisarTipo(self):
        medicamentos_experimentales = []
    
        # Recorre las filas de la tabla
        for fila in range(self.tableWidget.rowCount()):
            tipo_medicamento = self.tableWidget.item(fila, 9).text()
            fecha_entrega = self.tableWidget.item(fila, 10).text()  # Obtener la fecha de entrega
    
            # Si el tipo de medicamento es Experimental lo añade al arreglo
            if tipo_medicamento == "Experimental":
                medicamento = self.tableWidget.item(fila, 1).text()
                medicamentos_experimentales.append((medicamento, fecha_entrega))  # Agregar tupla (medicamento, fecha_entrega)
    
        # Muestra los medicamentos experimentales en un alertbox
        if medicamentos_experimentales:
            mensaje = "> Medicamentos Experimentales <\n\n"
            for medicamento, fecha_entrega in medicamentos_experimentales:
                mensaje += "- " + medicamento.ljust(30) + fecha_entrega.rjust(10) + "\n"  # Alinear nombre y fecha
            self.alertBox(mensaje, "Medicamentos Experimentales")
        else:
            self.alertBox("No se encontraron medicamentos del tipo Experimentales", "Medicamentos Experimentales")

            
    def guardarMedicamentos(self):
        # Abre el archivo CSV para guardar los datos
        with open('ArchivosCSV/Medicamentos.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Escribe los encabezados de las columnas
            encabezados = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
            writer.writerow(encabezados)
            # Sobreescribe los datos de los medicamentos con los nuevos valores
            for fila in range(self.tableWidget.rowCount()):
                datos_de_la_fila = []
                for columna in range(self.tableWidget.columnCount()):
                    celda = self.tableWidget.item(fila, columna)
                    if celda is not None:
                        datos_de_la_fila.append(celda.text())
                    else:
                        datos_de_la_fila.append('')
                writer.writerow(datos_de_la_fila)
                
    def ajustarCeldas(self):
        # Ajusta el tamaño de las celdas automaticamente
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnWidth(4, 272)        
        for fila in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(fila, 34)