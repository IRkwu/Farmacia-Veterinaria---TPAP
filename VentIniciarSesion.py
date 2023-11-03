from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Clases.Usuario import Usuario, usuarios
from VentMenuGerente import VentMenuGerente
from VentMenuVendedor import VentMenuVendedor

class VentIniciarSesion(object):
    def setupUi(self, VentIniciarSesion):
        Usuario.cargarUsuarioCSV()
        ImagenFondo = QtGui.QPixmap('Imagenes/menu_login.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentIniciarSesion.setWindowIcon(IconoTitulo)
        
        VentIniciarSesion.resize(500, 400)
        VentIniciarSesion.setMinimumSize(QtCore.QSize(500, 400))
        VentIniciarSesion.setMaximumSize(QtCore.QSize(500, 400))
        
        # Etiqueta imagen fondo
        self.imagen_fondoLabel = QtWidgets.QLabel(VentIniciarSesion)
        self.imagen_fondoLabel.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.imagen_fondoLabel.setText("")
        self.imagen_fondoLabel.setPixmap(ImagenFondo)
        
        # Etiqueta email y LineEdit
        self.emailLineEdit = QtWidgets.QLineEdit(VentIniciarSesion)
        self.emailLineEdit.setGeometry(QtCore.QRect(170, 151, 240, 40))
        self.emailLineEdit.setPlaceholderText("Ingrese su email")
        
        # Etiqueta password y LineEdit
        self.passwordLineEdit = QtWidgets.QLineEdit(VentIniciarSesion)
        self.passwordLineEdit.setGeometry(QtCore.QRect(170, 231, 240, 40))
        self.passwordLineEdit.setPlaceholderText("Ingrese su contraseña")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        # Boton ingresar cliente y accion al pulsar
        self.btnIngresarCliente = QtWidgets.QPushButton(VentIniciarSesion)
        self.btnIngresarCliente.setGeometry(QtCore.QRect(80, 340, 360, 40))
        self.btnIngresarCliente.clicked.connect(self.onActionIngresarCliente)

        self.retranslateUi(VentIniciarSesion)
        QtCore.QMetaObject.connectSlotsByName(VentIniciarSesion)

    def retranslateUi(self, VentIniciarSesion):
        _translate = QtCore.QCoreApplication.translate
        VentIniciarSesion.setWindowTitle(_translate("VentIniciarSesion", "Ingresar Sesión"))
        self.btnIngresarCliente.setText(_translate("VentIniciarSesion", "Iniciar Sesión"))
        
    # Mensajes de alerta, Vent emergente
    def alertBox(self, Mensaje, Datos, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Datos+"\n"+Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()
        
    def onActionIngresarCliente(self):
        email = self.emailLineEdit.text().lower()
        password = self.passwordLineEdit.text()
        if email.strip() == "":
            self.alertBox("Falta ingresar el email", "Falta un dato")
        elif password.strip() == "":
            self.alertBox("Falta ingresar la contraseña", "Falta un dato")
        else:
            datosValidos = False
            for usuario in usuarios:
                if email == usuario.get_email() and password == usuario.get_password():
                    datosValidos = True
                    break
            if datosValidos:
                self.alertBox("Ha ingresado sesión",usuario.get_nombres()+" - "+usuario.get_cargo(), "Vent - Ingresar Sesión")
                if (usuario.get_cargo() == "Gerente"):
                    self.cambiarVent(VentMenuGerente)
                elif (usuario.get_cargo() == "Vendedor"):
                    self.cambiarVent(VentMenuVendedor)
            else:
                self.alertBox("Contraseña o Email incorrecto","Inicio de sesión inválido","Vent - Datos Inválidos")
                
    def cambiarVent(self, nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()