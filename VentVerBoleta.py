from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, QDate
import csv

class VentVerBoleta(QDialog):
    def __init__(self, numero_boleta='', fecha='', cliente='', rut='', medicamentos='', cant_medicamentos='', subtotal='', descuento='', costo_envio='', total='', parent=None):
        super(VentVerBoleta, self).__init__(parent)
        self.numero_boleta = numero_boleta
        self.fecha = fecha
        self.cliente = cliente
        self.rut = rut
        self.medicamentos = medicamentos
        self.cant_medicamentos = cant_medicamentos
        self.subtotal = subtotal
        self.descuento = descuento
        self.costo_envio = costo_envio
        self.total = total
        
        self.setupUi(self)

        # Elimina el botón ? de la barra de titulo
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def setupUi(self, VentVerBoleta):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_ver_medicamentos.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentVerBoleta.setWindowIcon(IconoTitulo)
        
        VentVerBoleta.resize(800, 540)
        VentVerBoleta.setMinimumSize(QtCore.QSize(800, 540))
        VentVerBoleta.setMaximumSize(QtCore.QSize(800, 540))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentVerBoleta)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 800, 135))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(800, 135))
        
        # Etiqueta nombre cliente y LineEdit
        self.clienteLabel = QtWidgets.QLabel(VentVerBoleta)
        self.clienteLabel.setGeometry(QtCore.QRect(30, 150, 350, 13))
        self.clienteLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.clienteLineEdit.setGeometry(QtCore.QRect(30, 170, 350, 41))
        self.clienteLineEdit.setReadOnly(True)

        # Etiqueta numero_boleta y LineEdit
        self.numero_boletaLabel = QtWidgets.QLabel(VentVerBoleta)
        self.numero_boletaLabel.setGeometry(QtCore.QRect(30, 225, 150, 13))
        self.numero_boletaLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.numero_boletaLineEdit.setGeometry(QtCore.QRect(30, 245, 150, 41))
        self.numero_boletaLineEdit.setReadOnly(True)
        
        # Etiqueta rut y LineEdit
        self.rutLabel = QtWidgets.QLabel(VentVerBoleta)
        self.rutLabel.setGeometry(QtCore.QRect(220, 225, 150, 13))
        self.rutLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.rutLineEdit.setGeometry(QtCore.QRect(220, 245, 150, 41))
        self.rutLineEdit.setReadOnly(True)
        
        # Etiqueta fecha y DateEdit
        self.fechaLabel = QtWidgets.QLabel(VentVerBoleta)
        self.fechaLabel.setGeometry(QtCore.QRect(30, 300, 150, 13))
        self.fechaDateEdit = QtWidgets.QDateEdit(VentVerBoleta)
        self.fechaDateEdit.setGeometry(QtCore.QRect(30, 320, 150, 41))
        self.fechaDateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.fechaDateEdit.setReadOnly(True)
        
        # Etiqueta cantidad_medicamentos y LineEdit
        self.cant_medicamentosLabel = QtWidgets.QLabel(VentVerBoleta)
        self.cant_medicamentosLabel.setGeometry(QtCore.QRect(220, 300, 150, 13))
        self.cant_medicamentosLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.cant_medicamentosLineEdit.setGeometry(QtCore.QRect(220, 320, 150, 41))
        self.cant_medicamentosLineEdit.setReadOnly(True)
        
        # Etiqueta descuento_envio y LineEdit
        self.costo_envioLabel = QtWidgets.QLabel(VentVerBoleta)
        self.costo_envioLabel.setGeometry(QtCore.QRect(30, 375, 150, 13))
        self.costo_envioLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.costo_envioLineEdit.setGeometry(QtCore.QRect(30, 395, 150, 41))
        self.costo_envioLineEdit.setReadOnly(True)
        
        # Etiqueta descuento y LineEdit
        self.descuentoLabel = QtWidgets.QLabel(VentVerBoleta)
        self.descuentoLabel.setGeometry(QtCore.QRect(220, 375, 150, 13))
        self.descuentoLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.descuentoLineEdit.setGeometry(QtCore.QRect(220, 395, 150, 41))
        self.descuentoLineEdit.setReadOnly(True)
        
        # Etiqueta subtotal y LineEdit
        self.subtotalLabel = QtWidgets.QLabel(VentVerBoleta)
        self.subtotalLabel.setGeometry(QtCore.QRect(30, 450, 150, 13))
        self.subtotalLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.subtotalLineEdit.setGeometry(QtCore.QRect(30, 470, 150, 41))
        self.subtotalLineEdit.setReadOnly(True)
        
        # Etiqueta total y LineEdit
        self.totalLabel = QtWidgets.QLabel(VentVerBoleta)
        self.totalLabel.setGeometry(QtCore.QRect(220, 450, 150, 13))
        self.totalLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.totalLineEdit.setGeometry(QtCore.QRect(220, 470, 150, 41))
        self.totalLineEdit.setReadOnly(True)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentVerBoleta)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentVerBoleta.close)
        
        # Barra de busqueda y accion al actualizar el texto
        self.buscarLineEdit = QtWidgets.QLineEdit(VentVerBoleta)
        self.buscarLineEdit.setGeometry(QtCore.QRect(410, 150, 380, 50))
        self.buscarLineEdit.setPlaceholderText("Ingrese el nombre de medicamento")
        self.buscarLineEdit.setStyleSheet("font-size: 16px;")
        self.buscarLineEdit.textChanged.connect(self.buscarMedicamentos)
        
        # tableWidget para lista de medicamentos
        self.tableWidget = QtWidgets.QTableWidget(VentVerBoleta)
        self.tableWidget.setGeometry(QtCore.QRect(410, 210, 370, 310))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Nombres", "Precio", "Lote"])
        
        # Separar la cadena en elementos para integrarlos en un tableWidget
        self.arreglo_medicamentos = [tuple(cadena.strip("()").split(", ")) for cadena in self.medicamentos.strip("[]").split(", ")]
        
        # Rellenar las tablas
        self.rellenarFilas()
        self.rellenarDatos()
        
        # Para que no se puedan editar las tablas
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Definir textos
        self.retranslateUi(VentVerBoleta)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentVerBoleta)
        
    # Metodo definir textos
    def retranslateUi(self, VentVerBoleta):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentVerBoleta.setWindowTitle(_translate("VentVerBoleta", "Boleta - "+self.cliente))
        self.numero_boletaLabel.setText(_translate("VentVerBoleta", "Numero Boleta:"))
        self.clienteLabel.setText(_translate("VentVerBoleta", "Nombre Cliente:"))
        self.cant_medicamentosLabel.setText(_translate("VentVerBoleta", "Cantidad de Medicamentos:"))
        self.fechaLabel.setText(_translate("VentVerBoleta", "Fecha:"))
        self.rutLabel.setText(_translate("VentVerBoleta", "Rut Cliente:"))
        self.costo_envioLabel.setText(_translate("VentVerBoleta", "Costo Envio:"))
        self.descuentoLabel.setText(_translate("VentVerBoleta", "Descuento:"))
        self.subtotalLabel.setText(_translate("VentVerBoleta", "Subtotal:"))
        self.totalLabel.setText(_translate("VentVerBoleta", "Total:"))
        
    # Metodo para la barra de busqueda
    def buscarMedicamentos(self):
        # Busca los medicamentos que coinciden con la búsqueda y los muestra en la tabla
        texto = self.buscarLineEdit.text().strip().lower()
        if texto:
            for i in range(self.tableWidget.rowCount()):
                found = False
                nombre_medicamento = self.tableWidget.item(i, 0)
                # Si el nombre del medicamento existe la muestra
                if nombre_medicamento and texto in nombre_medicamento.text().lower():
                    found = True
                # Oculta los elementos que no tengan texto o numeros similares a los ingresados
                self.tableWidget.setRowHidden(i, not found)
        else:
            # Muestra todas las filas si no se ha ingresado ningún texto
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(i, False)
    
    # Configura la cantidad de filas y las rellena con los datos
    def rellenarFilas(self):
        self.tableWidget.setRowCount(len(self.arreglo_medicamentos) // 3)
        for fila, elemento in enumerate(self.arreglo_medicamentos):
            columna = fila % 3 
            fila = fila // 3
            self.tableWidget.setItem(fila, columna, QTableWidgetItem(str(elemento)))
        self.tableWidget.setColumnWidth(0, 180)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 80)
        self.eliminarCaracteres()
    
    # Rellena los datos de la boleta expectuando los productos
    def rellenarDatos(self):
        self.numero_boletaLineEdit.setText(self.numero_boleta)
        self.clienteLineEdit.setText(self.cliente)
        self.fechaDateEdit.setDate(QDate.fromString(self.fecha, "dd/MM/yyyy"))
        self.cant_medicamentosLineEdit.setText(self.cant_medicamentos)
        self.rutLineEdit.setText(self.rut)
        self.costo_envioLineEdit.setText(self.costo_envio)
        self.descuentoLineEdit.setText(self.descuento)
        self.subtotalLineEdit.setText(self.subtotal)
        self.totalLineEdit.setText(self.total)
        
    # Eliminar los simbolos en la tableWidget del Historial de Medicamentos comprados
    def eliminarCaracteres(self):
        caracteres_eliminar = ['[', ']', '(', ',', ')', "'", '"']
        for fila in range(self.tableWidget.rowCount()):
            for columna in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(fila, columna)
                if item:
                    texto = item.text()
                    texto_sin_caracteres = texto
                    for caracter in caracteres_eliminar:
                        texto_sin_caracteres = texto_sin_caracteres.replace(caracter, '')
                    item.setText(texto_sin_caracteres)