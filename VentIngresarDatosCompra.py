from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QMessageBox, QLabel, QSpinBox, QDateEdit, QDialog, QPushButton
from Clases.Cliente import Cliente
from PyQt5.QtCore import Qt, QDate
import csv
from VentAgregarClienteCarrito import VentAgregarClienteCarrito


class VentIngresarDatosCompra(QDialog):
    def __init__(self, nombres='', apellidos='', rut='', parent=None):
        super(VentIngresarDatosCompra, self).__init__(parent)
        self.nombres = nombres
        self.apellidos = apellidos
        self.rut = rut
        
        self.setupUi(self)

        # Elimina el botón ? de la barra de titulo
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def setupUi(self, VentIngresarDatosCompra):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentIngresarDatosCompra.setWindowIcon(IconoTitulo)
        
        VentIngresarDatosCompra.resize(400, 440)
        VentIngresarDatosCompra.setMinimumSize(QtCore.QSize(400, 440))
        VentIngresarDatosCompra.setMaximumSize(QtCore.QSize(400, 440))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentIngresarDatosCompra)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(-200, 0, 801, 91))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(801, 91))
        
        # Etiqueta nombres y LineEdit
        self.nombresLabel = QtWidgets.QLabel(VentIngresarDatosCompra)
        self.nombresLabel.setGeometry(QtCore.QRect(14, 122, 100, 50))
        self.nombresLineEdit = QtWidgets.QLineEdit(VentIngresarDatosCompra)
        self.nombresLineEdit.setGeometry(QtCore.QRect(106, 122, 260, 50))
        self.nombresLineEdit.setPlaceholderText("Ingrese primer y segundo nombre")
        self.nombresLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.nombresLineEdit))
        
        # Etiqueta apellidos y LineEdit
        self.apellidosLabel = QtWidgets.QLabel(VentIngresarDatosCompra)
        self.apellidosLabel.setGeometry(QtCore.QRect(14, 214, 100, 50))
        self.apellidosLineEdit = QtWidgets.QLineEdit(VentIngresarDatosCompra)
        self.apellidosLineEdit.setGeometry(QtCore.QRect(106, 214, 260, 50))
        self.apellidosLineEdit.setPlaceholderText("Ingrese apellido paterno y materno")
        self.apellidosLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.apellidosLineEdit))
        
        # Etiqueta rut y LineEdit
        self.rutLabel = QtWidgets.QLabel(VentIngresarDatosCompra)
        self.rutLabel.setGeometry(QtCore.QRect(14, 306, 17, 50))
        self.rutLineEdit = QtWidgets.QLineEdit(VentIngresarDatosCompra)
        self.rutLineEdit.setGeometry(QtCore.QRect(106, 306, 200, 50))
        self.rutLineEdit.setMaxLength(8)
        self.rutLineEdit.setValidator(QIntValidator())
        self.rutLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.rutLineEdit.setPlaceholderText("Ingrese rut sin puntos")
        
        # Etiqueta digito_verificador y LineEdit
        self.digito_verificadorLabel = QtWidgets.QLabel(VentIngresarDatosCompra)
        self.digito_verificadorLabel.setGeometry(QtCore.QRect(312, 306, 17, 50))
        self.digito_verificadorLineEdit = QtWidgets.QLineEdit(VentIngresarDatosCompra)
        self.digito_verificadorLineEdit.setGeometry(QtCore.QRect(326, 306, 40, 50))
        self.digito_verificadorLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9Kk]")))
        self.digito_verificadorLineEdit.setMaxLength(1)
        self.digito_verificadorLineEdit.setPlaceholderText("0-9 | K")
        
        # Btoton ingresar y accion al pulsar
        self.btnIngresar = QtWidgets.QPushButton(VentIngresarDatosCompra)
        self.btnIngresar.setGeometry(QtCore.QRect(20, 380, 360, 40))
        self.btnIngresar.clicked.connect(self.onActionBtnIngresar)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentIngresarDatosCompra)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentIngresarDatosCompra.close)
        
        # Definir textos
        self.retranslateUi(VentIngresarDatosCompra)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentIngresarDatosCompra)
        
    # Metodo definir textos
    def retranslateUi(self, VentIngresarDatosCompra):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentIngresarDatosCompra.setWindowTitle(_translate("VentIngresarDatosCompra", "Ingresar Datos Cliente"))
        self.nombresLabel.setText(_translate("VentIngresarDatosCompra", "Nombres"))
        self.apellidosLabel.setText(_translate("VentIngresarDatosCompra", "Apellidos"))
        self.rutLabel.setText(_translate("VentIngresarDatosCompra", "Rut"))
        self.digito_verificadorLabel.setText(_translate("VentAgregarCliente", "-"))
        self.btnIngresar.setText(_translate("VentIngresarDatosCompra", "Confirmar Datos"))
        
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
        nombres = self.nombresLineEdit.text()
        apellidos = self.apellidosLineEdit.text()
        rut = self.rutLineEdit.text()
        digito_verificador = self.digito_verificadorLineEdit.text()
        # Convertir la k minuscula en mayuscula
        if digito_verificador == "k":
            digito_verificador = digito_verificador.replace("k", "K")
        # Pasar el rut al formato "xx.xxx.xxx-x"
        if len(rut) > 0:
            rutFormatted = "{:,}".format(int(rut)).replace(",", ".")
            self.rut_con_digito_verificador = rutFormatted + "-" + digito_verificador
        else:
            self.rut_con_digito_verificador = ""
        # El .strip es para verificar que tenga datos
        if nombres.strip() == "":
            self.alertBox("Falta ingresar el nombre", "Falta un dato")
        elif apellidos.strip() == "":
            self.alertBox("Falta ingresar el apellido", "Falta un dato")
        elif len(rut) < 7 or len(digito_verificador) != 1:
            self.alertBox("Faltan números en el rut o el dígito verificador", "Falta un dato")
        elif self.verificarRutExistente(self.rut_con_digito_verificador):
            self.alertBox("Gracias por la compra :D\nEl cliente ya está registrado como:\n"+self.nombres+" "+self.apellidos, "Cliente Registrado")
            self.accept()
        else:
            respuesta = QMessageBox.question(None, "Cliente Nuevo", "¿Quiere registrarse como cliente?", QMessageBox.Yes | QMessageBox.No)
            
            if respuesta == QMessageBox.Yes:
                dialog = VentAgregarClienteCarrito(nombres=nombres,
                                            apellidos=apellidos,
                                            rut=self.rutLineEdit.text(),
                                            rut_con_digito_verificador=self.digito_verificadorLineEdit.text())
                if dialog.exec_() == QDialog.Accepted:
                    self.accept()
            else:
                self.accept()
    
    # Getters
    def get_nombres(self):
        return self.nombresLineEdit.text()

    def get_apellidos(self):
        return self.apellidosLineEdit.text()

    def get_rut(self):
        return self.rut_con_digito_verificador
    
    # Verificar si ya existe el rut
    def verificarRutExistente(self, rut):
        with open('ArchivosCSV/Cliente.csv', 'r') as file:
            encabezados = csv.reader(file)
            for fila in encabezados:
                if fila[6] == rut:
                    self.nombres=fila[1]
                    self.apellidos=fila[2]
                    return True
        return False