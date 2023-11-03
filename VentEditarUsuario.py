from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QMessageBox, QLabel, QSpinBox, QDateEdit, QDialog, QPushButton
from Clases.Usuario import Usuario
from PyQt5.QtCore import Qt, QDate

class VentEditarUsuario(QDialog):
    def __init__(self, nombres='', apellidos='', genero='', telefono='', email='', domicilio='', cargo='', password='', parent=None):
        super(VentEditarUsuario, self).__init__(parent)
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.telefono = telefono
        self.email = email
        self.domicilio = domicilio
        self.cargo = cargo
        self.password = password
        
        self.setupUi(self)

        # Elimina el botón ? de la barra de titulo
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def setupUi(self, VentEditarUsuario):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentEditarUsuario.setWindowIcon(IconoTitulo)
        
        VentEditarUsuario.resize(800, 565)
        VentEditarUsuario.setMinimumSize(QtCore.QSize(800, 565))
        VentEditarUsuario.setMaximumSize(QtCore.QSize(800, 565))
        
        # Etiqueta nombres y LineEdit
        self.nombresLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.nombresLabel.setGeometry(QtCore.QRect(14, 137, 42, 50))
        self.nombresLineEdit = QtWidgets.QLineEdit(VentEditarUsuario)
        self.nombresLineEdit.setGeometry(QtCore.QRect(106, 137, 260, 50))
        self.nombresLineEdit.setPlaceholderText("Ingrese primer y segundo nombre")
        self.nombresLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.nombresLineEdit))
        
        # Etiqueta apellidos y LineEdit
        self.apellidosLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.apellidosLabel.setGeometry(QtCore.QRect(399, 137, 42, 50))
        self.apellidosLineEdit = QtWidgets.QLineEdit(VentEditarUsuario)
        self.apellidosLineEdit.setGeometry(QtCore.QRect(504, 137, 260, 50))
        self.apellidosLineEdit.setPlaceholderText("Ingrese apellido paterno y materno")
        self.apellidosLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.apellidosLineEdit))

        # Etiqueta genero y ComboBox
        self.generoLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.generoLabel.setGeometry(QtCore.QRect(14, 229, 35, 50))
        self.generoComboBox = QtWidgets.QComboBox(VentEditarUsuario)
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
        self.telefonoLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.telefonoLabel.setGeometry(QtCore.QRect(399, 229, 50, 50))
        self.telefonoLineEdit = QtWidgets.QLineEdit(VentEditarUsuario)
        self.telefonoLineEdit.setGeometry(QtCore.QRect(504, 229, 260, 50))
        self.telefonoLineEdit.setMaxLength(9)
        self.telefonoLineEdit.setValidator(QIntValidator())
        self.telefonoLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.telefonoLineEdit.setPlaceholderText("Ingrese su numero de 9 digitos")
        
        # Etiqueta email y LineEdit
        self.emailLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.emailLabel.setGeometry(QtCore.QRect(14, 321, 42, 50))
        self.emailLineEdit = QtWidgets.QLineEdit(VentEditarUsuario)
        self.emailLineEdit.setGeometry(QtCore.QRect(106, 321, 260, 50))
        self.emailLineEdit.setPlaceholderText("Ingrese su email")
        
        # Etiqueta domicilio y LineEdit
        self.domicilioLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.domicilioLabel.setGeometry(QtCore.QRect(399, 321, 42, 50))
        self.domicilioLineEdit = QtWidgets.QLineEdit(VentEditarUsuario)
        self.domicilioLineEdit.setGeometry(QtCore.QRect(504, 321, 260, 50))
        self.domicilioLineEdit.setPlaceholderText("Ingrese domicilio")
        
        # Etiqueta email y LineEdit
        self.passwordLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.passwordLabel.setGeometry(QtCore.QRect(14, 408, 80, 50))
        self.passwordLineEdit = QtWidgets.QLineEdit(VentEditarUsuario)
        self.passwordLineEdit.setGeometry(QtCore.QRect(106, 408, 260, 50))
        self.passwordLineEdit.setPlaceholderText("Ingrese su nueva contraseña")
        
        # Etiqueta genero y ComboBox
        self.cargoLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.cargoLabel.setGeometry(QtCore.QRect(399, 408, 35, 50))
        self.cargoComboBox = QtWidgets.QComboBox(VentEditarUsuario)
        self.cargoComboBox.setGeometry(QtCore.QRect(504, 408, 260, 50))
        self.cargoComboBox.setMinimumSize(QtCore.QSize(260, 50))
        self.cargoComboBox.setEditable(False)
        self.cargoComboBox.addItem("")
        self.cargoComboBox.addItem("")
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentEditarUsuario)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner)
        
        # Btoton ingresar y accion al pulsar
        self.btnIngresar = QtWidgets.QPushButton(VentEditarUsuario)
        self.btnIngresar.setGeometry(QtCore.QRect(14, 495, 85, 50))
        self.btnIngresar.clicked.connect(self.onActionBtnIngresar)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentEditarUsuario)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentEditarUsuario.close)
        
        # Definir textos
        self.retranslateUi(VentEditarUsuario)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentEditarUsuario)
        self.rellenarDatos()
        
    # Metodo definir textos
    def retranslateUi(self, VentEditarUsuario):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentEditarUsuario.setWindowTitle(_translate("VentEditarUsuario", "Editar Usuario"))
        self.nombresLabel.setText(_translate("VentEditarUsuario", "Nombres"))
        self.apellidosLabel.setText(_translate("VentEditarUsuario", "Apellidos"))
        self.generoLabel.setText(_translate("VentEditarUsuario", "Genero"))
        self.generoComboBox.setItemText(0, _translate("VentEditarUsuario", "Masculino"))
        self.generoComboBox.setItemText(1, _translate("VentEditarUsuario", "Femenino"))
        self.generoComboBox.setPlaceholderText("Seleccione género")
        self.telefonoLabel.setText(_translate("VentEditarUsuario", "Telefono"))
        self.emailLabel.setText(_translate("VentEditarUsuario", "Email"))
        self.domicilioLabel.setText(_translate("VentEditarUsuario", "Domicilio"))
        self.btnIngresar.setText(_translate("VentEditarUsuario", "Confirmar\nCambios"))
        self.cargoLabel.setText(_translate("VentAgregarUsuario", "Cargo"))
        self.passwordLabel.setText(_translate("VentEditarUsuario", "Contraseña"))
        self.cargoComboBox.setItemText(0, _translate("VentAgregarUsuario", "Gerente"))
        self.cargoComboBox.setItemText(1, _translate("VentAgregarUsuario", "Vendedor"))
        
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
        password = self.passwordLineEdit.text()
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
        elif len(password) < 4:
            self.alertBox("La contraseña debe tener al menos 4 caracteres", "Contraseña inválida")
        else:
            self.accept()
            
    def rellenarDatos(self):
        self.nombresLineEdit.setText(self.nombres)
        self.apellidosLineEdit.setText(self.apellidos)
        self.generoComboBox.setCurrentText(self.genero)
        self.telefonoLineEdit.setText(self.telefono)
        self.emailLineEdit.setText(self.email)
        self.domicilioLineEdit.setText(self.domicilio)
        self.cargoComboBox.setCurrentText(self.cargo)
        self.passwordLineEdit.setText(self.password)
    
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
    
    def get_cargo(self):
        return self.cargoComboBox.currentText()
    
    def get_password(self):
        return self.passwordLineEdit.text()
