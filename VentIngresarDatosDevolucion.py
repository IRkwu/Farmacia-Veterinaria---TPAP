from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QMessageBox, QLabel, QSpinBox, QDateEdit, QDialog, QPushButton
from Clases.Cliente import Cliente
from Clases.NotasDeCredito import NotasDeCredito
from PyQt5.QtCore import Qt, QDate
import datetime
import csv


class VentIngresarDatosDevolucion(QDialog):
    def __init__(self, medicamento='', precio='', stock_lote_2='', parent=None):
        super(VentIngresarDatosDevolucion, self).__init__(parent)
        self.medicamento = medicamento
        self.precio = precio
        self.stock_lote_2 = stock_lote_2
        
        self.setupUi(self)

        # Elimina el botón ? de la barra de titulo
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def setupUi(self, VentIngresarDatosDevolucion):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentIngresarDatosDevolucion.setWindowIcon(IconoTitulo)
        
        VentIngresarDatosDevolucion.resize(400, 366)
        VentIngresarDatosDevolucion.setMinimumSize(QtCore.QSize(400, 366))
        VentIngresarDatosDevolucion.setMaximumSize(QtCore.QSize(400, 366))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentIngresarDatosDevolucion)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(-200, 0, 801, 91))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(801, 91))
        
        # Etiqueta numero boleta y LineEdit
        self.numero_boletaLabel = QtWidgets.QLabel(VentIngresarDatosDevolucion)
        self.numero_boletaLabel.setGeometry(QtCore.QRect(14, 122, 100, 50))
        self.numero_boletaLineEdit = QtWidgets.QLineEdit(VentIngresarDatosDevolucion)
        self.numero_boletaLineEdit.setGeometry(QtCore.QRect(106, 122, 260, 50))
        self.numero_boletaLineEdit.setValidator(QIntValidator())
        self.numero_boletaLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.numero_boletaLineEdit.setPlaceholderText("Ingrese el numero de Boleta")
        
        # Etiqueta lote y ComboBox
        self.loteLabel = QtWidgets.QLabel(VentIngresarDatosDevolucion)
        self.loteLabel.setGeometry(QtCore.QRect(14, 214, 100, 50))
        self.loteComboBox = QtWidgets.QComboBox(VentIngresarDatosDevolucion)
        self.loteComboBox.setGeometry(QtCore.QRect(106, 214, 260, 50))
        self.loteComboBox.setMinimumSize(QtCore.QSize(260, 50))
        self.loteComboBox.setEditable(False)
        self.loteComboBox.addItem("Lote 1")
        if self.stock_lote_2 != 0:
            self.loteComboBox.addItem("Lote 2")
        
        # Btoton ingresar y accion al pulsar
        self.btnIngresar = QtWidgets.QPushButton(VentIngresarDatosDevolucion)
        self.btnIngresar.setGeometry(QtCore.QRect(20, 296, 360, 40))
        self.btnIngresar.clicked.connect(self.onActionBtnIngresar)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentIngresarDatosDevolucion)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentIngresarDatosDevolucion.close)
        
        # Definir textos
        self.retranslateUi(VentIngresarDatosDevolucion)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentIngresarDatosDevolucion)
        
    # Metodo definir textos
    def retranslateUi(self, VentIngresarDatosDevolucion):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentIngresarDatosDevolucion.setWindowTitle(_translate("VentIngresarDatosDevolucion", "Ingresar Datos Boleta"))
        self.numero_boletaLabel.setText(_translate("VentIngresarDatosDevolucion", "Numero Boleta"))
        self.loteLabel.setText(_translate("VentIngresarDatosDevolucion", "Lote a Agregar"))
        self.btnIngresar.setText(_translate("VentIngresarDatosDevolucion", "Confirmar Datos"))
        
    # Mensajes de alerta, Vent emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()
        
    # Accion al clickear boton ingresar
    def onActionBtnIngresar(self):
        if self.verificarNumeroBoletaExistente(self.numero_boletaLineEdit.text()):
            self.alertBox("La compra había sido efectuada\nLa devolución es correcta","Devolución Correcta")
            NotasDeCredito.agregarNotasDeCredito(self, datetime.datetime.now().strftime("%d/%m/%Y"), self.cliente, self.rut, self.medicamento, self.precio)
            self.accept()
        else:
            self.alertBox("El numero de boleta no existe, no se puede hacer una devolución","Devolución Invalida")
    
    # Verificar si ya existe el numero de boleta
    def verificarNumeroBoletaExistente(self, numero_boleta):
        with open('ArchivosCSV/Boletas.csv', 'r') as file:
            encabezados = csv.reader(file)
            for fila in encabezados:
                if fila[0] == numero_boleta:
                    self.cliente = fila[2]
                    self.rut = fila[3]
                    return True
        return False
    
    # Getters
    def get_lote(self):
        return self.loteComboBox.currentText()