from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QMessageBox, QLabel, QSpinBox, QDateEdit, QDialog, QPushButton
from Clases.Cliente import Cliente
from PyQt5.QtCore import Qt, QDate

class VentEditarCliente(QDialog):
    def __init__(self, nombres='', apellidos='', genero='', telefono='', email='', domicilio='', parent=None):
        super(VentEditarCliente, self).__init__(parent)
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.telefono = telefono
        self.email = email
        self.domicilio = domicilio
        
        self.setupUi(self)

        # Elimina el botón ? de la barra de titulo
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def setupUi(self, VentEditarCliente):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentEditarCliente.setWindowIcon(IconoTitulo)
        
        VentEditarCliente.resize(800, 478)
        VentEditarCliente.setMinimumSize(QtCore.QSize(800, 478))
        VentEditarCliente.setMaximumSize(QtCore.QSize(800, 478))
        
        # Etiqueta nombres y LineEdit
        self.nombresLabel = QtWidgets.QLabel(VentEditarCliente)
        self.nombresLabel.setGeometry(QtCore.QRect(14, 137, 42, 50))
        self.nombresLineEdit = QtWidgets.QLineEdit(VentEditarCliente)
        self.nombresLineEdit.setGeometry(QtCore.QRect(106, 137, 260, 50))
        self.nombresLineEdit.setPlaceholderText("Ingrese primer y segundo nombre")
        self.nombresLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.nombresLineEdit))
        
        # Etiqueta apellidos y LineEdit
        self.apellidosLabel = QtWidgets.QLabel(VentEditarCliente)
        self.apellidosLabel.setGeometry(QtCore.QRect(399, 137, 42, 50))
        self.apellidosLineEdit = QtWidgets.QLineEdit(VentEditarCliente)
        self.apellidosLineEdit.setGeometry(QtCore.QRect(504, 137, 260, 50))
        self.apellidosLineEdit.setPlaceholderText("Ingrese apellido paterno y materno")
        self.apellidosLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.apellidosLineEdit))

        # Etiqueta genero y ComboBox
        self.generoLabel = QtWidgets.QLabel(VentEditarCliente)
        self.generoLabel.setGeometry(QtCore.QRect(14, 229, 35, 50))
        self.generoComboBox = QtWidgets.QComboBox(VentEditarCliente)
        self.generoComboBox.setGeometry(QtCore.QRect(106, 229, 260, 50))
        self.generoComboBox.setMinimumSize(QtCore.QSize(260, 50))
        self.generoComboBox.setEditable(False)
        self.generoComboBox.addItem("")
        self.generoComboBox.addItem("")
        iconoHombre = QIcon("Imagenes/man.png")
        iconoMujer = QIcon("Imagenes/woman.png")
        self.generoComboBox.setItemIcon(0, iconoHombre)
        self.generoComboBox.setItemIcon(1, iconoMujer)
        
        # Etiqueta telefono y LineEdit
        self.telefonoLabel = QtWidgets.QLabel(VentEditarCliente)
        self.telefonoLabel.setGeometry(QtCore.QRect(399, 229, 50, 50))
        self.telefonoLineEdit = QtWidgets.QLineEdit(VentEditarCliente)
        self.telefonoLineEdit.setGeometry(QtCore.QRect(504, 229, 260, 50))
        self.telefonoLineEdit.setMaxLength(9)
        self.telefonoLineEdit.setValidator(QIntValidator())
        self.telefonoLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.telefonoLineEdit.setPlaceholderText("Ingrese su numero de 9 digitos")
        
        # Etiqueta email y LineEdit
        self.emailLabel = QtWidgets.QLabel(VentEditarCliente)
        self.emailLabel.setGeometry(QtCore.QRect(14, 321, 42, 50))
        self.emailLineEdit = QtWidgets.QLineEdit(VentEditarCliente)
        self.emailLineEdit.setGeometry(QtCore.QRect(106, 321, 260, 50))
        self.emailLineEdit.setPlaceholderText("Ingrese su email")
        
        # Etiqueta domicilio y LineEdit
        self.domicilioLabel = QtWidgets.QLabel(VentEditarCliente)
        self.domicilioLabel.setGeometry(QtCore.QRect(399, 321, 42, 50))
        self.domicilioLineEdit = QtWidgets.QLineEdit(VentEditarCliente)
        self.domicilioLineEdit.setGeometry(QtCore.QRect(504, 321, 260, 50))
        self.domicilioLineEdit.setPlaceholderText("Ingrese domicilio")
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentEditarCliente)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner)
        
        # Btoton ingresar y accion al pulsar
        self.btnIngresar = QtWidgets.QPushButton(VentEditarCliente)
        self.btnIngresar.setGeometry(QtCore.QRect(14, 408, 85, 50))
        self.btnIngresar.clicked.connect(self.onActionBtnIngresar)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentEditarCliente)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentEditarCliente.close)
        
        # Definir textos
        self.retranslateUi(VentEditarCliente)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentEditarCliente)
        self.rellenarDatos()
        
    # Metodo definir textos
    def retranslateUi(self, VentEditarCliente):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentEditarCliente.setWindowTitle(_translate("VentEditarCliente", "Editar Cliente"))
        self.nombresLabel.setText(_translate("VentEditarCliente", "Nombres"))
        self.apellidosLabel.setText(_translate("VentEditarCliente", "Apellidos"))
        self.generoLabel.setText(_translate("VentEditarCliente", "Genero"))
        self.generoComboBox.setItemText(0, _translate("VentEditarCliente", "Masculino"))
        self.generoComboBox.setItemText(1, _translate("VentEditarCliente", "Femenino"))
        self.generoComboBox.setPlaceholderText("Seleccione género")
        self.telefonoLabel.setText(_translate("VentEditarCliente", "Telefono"))
        self.emailLabel.setText(_translate("VentEditarCliente", "Email"))
        self.domicilioLabel.setText(_translate("VentEditarCliente", "Domicilio"))
        self.btnIngresar.setText(_translate("VentEditarCliente", "Confirmar\nCambios"))
        
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
        genero = self.generoComboBox.currentText()
        telefono =self.telefonoLineEdit.text()
        email = self.emailLineEdit.text()
        domicilio = self.domicilioLineEdit.text()
        if '@' not in email or '.' not in email:
            self.alertBox("Falta agregar '@' o '.' en el email", "Falta un dato")
        # El .strip es para verificar que tenga datos
        elif nombres.strip() == "":
            self.alertBox("Falta ingresar el nombre", "Falta un dato")
        elif apellidos.strip() == "":
            self.alertBox("Falta ingresar el apellido", "Falta un dato")
        elif len(telefono) != 9:
            self.alertBox("Faltan numeros en el telefono", "Falta un dato")
        elif '@' not in email or '.' not in email:
            self.alertBox("Falta agregar '@' o '.' en el email", "Falta un dato")
        elif domicilio.strip() == "":
            self.alertBox("Falta ingresar el domicilio", "Falta un dato")
        else:
            self.accept()
            
    def rellenarDatos(self):
        self.nombresLineEdit.setText(self.nombres)
        self.apellidosLineEdit.setText(self.apellidos)
        self.generoComboBox.setCurrentText(self.genero)
        self.telefonoLineEdit.setText(self.telefono)
        self.emailLineEdit.setText(self.email)
        self.domicilioLineEdit.setText(self.domicilio)
    
    # Getters
    def get_nombres(self):
        return self.nombresLineEdit.text()

    def get_apellidos(self):
        return self.apellidosLineEdit.text()

    def get_genero(self):
        return self.generoComboBox.currentText()

    def get_telefono(self):
        return self.telefonoLineEdit.text()

    def get_email(self):
        return self.emailLineEdit.text()

    def get_domicilio(self):
        return self.domicilioLineEdit.text()
