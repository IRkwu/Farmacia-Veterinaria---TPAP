from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QDialog, QComboBox
from Clases.Boleta import Boleta
from PyQt5.QtCore import QDate

import csv, datetime
from VentVerBoleta import VentVerBoleta

class VentHistorialBoletas(object):
    def __init__(self):
        self.carrito = []  # Lista para almacenar los medicamentos del carrito
        self.medicamentos_cliente = []  # Lista para almacenar los medicamentos del cliente

    
    def setupUi(self, VentHistorialBoletas):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentHistorialBoletas.setWindowIcon(IconoTitulo)
        
        VentHistorialBoletas.resize(850, 620)
        VentHistorialBoletas.setMinimumSize(QtCore.QSize(850, 620))
        VentHistorialBoletas.setMaximumSize(QtCore.QSize(850, 620))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentHistorialBoletas)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 850, 94))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(850, 94))
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentHistorialBoletas)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentHistorialBoletas.close)
        
        # Boton ver info de la boleta y accion al pulsar
        self.btnVerBoleta = QtWidgets.QPushButton(VentHistorialBoletas)
        self.btnVerBoleta.setGeometry(QtCore.QRect(730, 100, 110, 50))
        self.btnVerBoleta.clicked.connect(self.onActionBtnConfirmar)
        
        # Combobox para filtar por mes
        self.comboBoxMes = QComboBox(VentHistorialBoletas)
        self.comboBoxMes.setGeometry(QtCore.QRect(610, 100, 110, 50))
        self.comboBoxMes.addItem("Todos los meses")
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.comboBoxMes.addItems(meses)
        self.comboBoxMes.currentIndexChanged.connect(self.filtrarPorMes)
        
        # Tabla con columnas y filas y que sean 10 columnas [ID, Nombre, Precio, Stock, Descripcion], carga las demás columnas pero no las muestra, es para que al guardar no se vacien
        self.tableWidget = QtWidgets.QTableWidget(VentHistorialBoletas)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 830, 445))
        self.tableWidget.setColumnCount(10)
        
        # Para que no se puedan editar los medicamentos de la lista de medicamentos
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Ocultar de Medicamentos en el tableWidget
        self.tableWidget.setColumnHidden(4, True)

        # Barra de busqueda y accion al actualizar el texto
        self.buscarLineEdit = QtWidgets.QLineEdit(VentHistorialBoletas)
        self.buscarLineEdit.setGeometry(QtCore.QRect(10, 100, 590, 50))
        self.buscarLineEdit.setPlaceholderText("Ingrese el número de boleta o nombre del cliente")
        self.buscarLineEdit.setStyleSheet("font-size: 16px;")
        self.buscarLineEdit.textChanged.connect(self.buscarMedicamentos)
        
        self.cargarBoletasCSV()

        self.retranslateUi(VentHistorialBoletas)
        QtCore.QMetaObject.connectSlotsByName(VentHistorialBoletas)
        
    # Metodo definir textos
    def retranslateUi(self, VentHistorialBoletas):
        _translate = QtCore.QCoreApplication.translate
        VentHistorialBoletas.setWindowTitle(_translate("VentHistorialBoletas", "Historial de Boletas"))
        self.btnVerBoleta.setText(_translate("VentHistorialBoletas", "Ver Detalles de\nla Boleta"))
    
    # Metodo para que cargue los clientes desde el archivo CSV
    def cargarBoletasCSV(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Boletas.csv', newline='') as csvfile:
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
        # Busca los medicamentos que coinciden con la búsqueda y el mes del combobox y los muestra en la tabla
        texto = self.buscarLineEdit.text().strip().lower()
        mes_seleccionado = self.comboBoxMes.currentText()

        for i in range(self.tableWidget.rowCount()):
            found = False
            numero_boleta = self.tableWidget.item(i, 0)
            nombre_cliente = self.tableWidget.item(i, 2)
            fecha_venta = self.tableWidget.item(i, 1)

            if mes_seleccionado != "Todos los meses":
                mes_numero = self.comboBoxMes.currentIndex()
                if fecha_venta:
                    fecha_venta = QDate.fromString(fecha_venta.text(), "dd/MM/yyyy")
                    if fecha_venta.month() != mes_numero:
                        continue
            
            # Filtra por numero de boleta del cliente
            if numero_boleta and texto in numero_boleta.text().lower():
                found = True
            # Filtra por nombre del cliente
            elif nombre_cliente and texto in nombre_cliente.text().lower():
                found = True
                
            self.tableWidget.setRowHidden(i, not found)

                
    def ajustarCeldas(self):
        # Ajusta el tamaño de las celdas automaticamente
        self.tableWidget.resizeColumnsToContents()
        for fila in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(fila, 37)
    
    def onActionBtnConfirmar(self):
        celda = self.tableWidget.currentItem() 
        if celda is None:
            self.alertBox("Debe seleccionar una celda", "Instrucciones para editar")
        else:
            columna = self.tableWidget.currentColumn()
            fila = self.tableWidget.currentRow()
            
            dialog = VentVerBoleta(numero_boleta=self.tableWidget.item(fila, 0).text(),
                                        fecha=self.tableWidget.item(fila, 1).text(),
                                        cliente=self.tableWidget.item(fila, 2).text(),
                                        rut=self.tableWidget.item(fila, 3).text(),
                                        medicamentos=self.tableWidget.item(fila, 4).text(),
                                        cant_medicamentos=self.tableWidget.item(fila, 5).text(),
                                        subtotal=self.tableWidget.item(fila, 6).text(),
                                        descuento=self.tableWidget.item(fila, 7).text(),
                                        costo_envio=self.tableWidget.item(fila, 8).text(),
                                        total=self.tableWidget.item(fila, 9).text())

            if dialog.exec_() == QDialog.Accepted:
                pass
                
    # Ventana para agregar nuevo stock en el Lote disponible 
    def agregarStockDialog(self):
        dialog = VentVerBoleta()
        if dialog.exec_():
            pass
    
    def filtrarPorMes(self):
        mes_seleccionado = self.comboBoxMes.currentText()
        if mes_seleccionado == "Todos los meses":
            # Muestra todas las filas si se selecciona "Todos los meses"
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(i, False)
        else:
            mes_numero = self.comboBoxMes.currentIndex()
            # Itera sobre las filas de la tabla
            for i in range(self.tableWidget.rowCount()):
                found = False
                fecha_venta = self.tableWidget.item(i, 1)
                
                if fecha_venta:
                    fecha_venta = QDate.fromString(fecha_venta.text(), "dd/MM/yyyy")
                    if fecha_venta.month() == mes_numero:
                        found = True
                        
                # Oculta los elementos que no coinciden con el mes seleccionado
                self.tableWidget.setRowHidden(i, not found)