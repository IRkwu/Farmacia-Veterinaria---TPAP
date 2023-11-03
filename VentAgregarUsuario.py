from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QMessageBox
from Clases.Usuario import Usuario
import csv

class VentAgregarUsuario(object):
    def setupUi(self, VentAgregarUsuario):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentAgregarUsuario.setWindowIcon(IconoTitulo)
        
        VentAgregarUsuario.resize(800, 657)
        VentAgregarUsuario.setMinimumSize(QtCore.QSize(800, 657))
        VentAgregarUsuario.setMaximumSize(QtCore.QSize(800, 657))
        
        # Etiqueta nombres y LineEdit
        self.nombresLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.nombresLabel.setGeometry(QtCore.QRect(14, 137, 42, 50))
        self.nombresLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.nombresLineEdit.setGeometry(QtCore.QRect(106, 137, 260, 50))
        self.nombresLineEdit.setPlaceholderText("Ingrese primer y segundo nombre")
        self.nombresLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.nombresLineEdit))
        
        # Etiqueta apellidos y LineEdit
        self.apellidosLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.apellidosLabel.setGeometry(QtCore.QRect(399, 137, 42, 50))
        self.apellidosLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.apellidosLineEdit.setGeometry(QtCore.QRect(504, 137, 260, 50))
        self.apellidosLineEdit.setPlaceholderText("Ingrese apellido paterno y materno")
        self.apellidosLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[^0-9]+"), self.apellidosLineEdit))

        # Etiqueta genero y ComboBox
        self.generoLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.generoLabel.setGeometry(QtCore.QRect(14, 229, 35, 50))
        self.generoComboBox = QtWidgets.QComboBox(VentAgregarUsuario)
        self.generoComboBox.setGeometry(QtCore.QRect(106, 229, 260, 50))
        self.generoComboBox.setMinimumSize(QtCore.QSize(260, 50))
        self.generoComboBox.setEditable(False)
        self.generoComboBox.addItem("")
        self.generoComboBox.addItem("")
        iconoHombre = QIcon("Imagenes/man.png")
        iconoMujer = QIcon("Imagenes/woman.png")
        self.generoComboBox.setItemIcon(0, iconoHombre)
        self.generoComboBox.setItemIcon(1, iconoMujer)

        # Etiqueta fecha_nacimiento y DateEdit
        self.fecha_nacimientoLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.fecha_nacimientoLabel.setGeometry(QtCore.QRect(399, 229, 99, 50))
        self.fecha_nacimientoDateEdit = QtWidgets.QDateEdit(VentAgregarUsuario)
        self.fecha_nacimientoDateEdit.setGeometry(QtCore.QRect(504, 229, 260, 50))
        self.fecha_nacimientoDateEdit.setMaximumDate(QtCore.QDate.currentDate().addYears(-18))
        self.fecha_nacimientoDateEdit.setMinimumDate(QtCore.QDate.currentDate().addYears(-100))
        
        # Etiqueta rut y LineEdit
        self.rutLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.rutLabel.setGeometry(QtCore.QRect(14, 321, 17, 50))
        self.rutLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.rutLineEdit.setGeometry(QtCore.QRect(106, 321, 200, 50))
        self.rutLineEdit.setMaxLength(8)
        self.rutLineEdit.setValidator(QIntValidator())
        self.rutLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.rutLineEdit.setPlaceholderText("Ingrese rut sin puntos")
        
        # Etiqueta digito_verificador y LineEdit
        self.digito_verificadorLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.digito_verificadorLabel.setGeometry(QtCore.QRect(312, 321, 17, 50))
        self.digito_verificadorLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.digito_verificadorLineEdit.setGeometry(QtCore.QRect(326, 321, 40, 50))
        self.digito_verificadorLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9Kk]")))
        self.digito_verificadorLineEdit.setMaxLength(1)
        self.digito_verificadorLineEdit.setPlaceholderText("0-9 | K")
        
        # Etiqueta telefono y LineEdit
        self.telefonoLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.telefonoLabel.setGeometry(QtCore.QRect(399, 321, 42, 50))
        self.telefonoLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.telefonoLineEdit.setGeometry(QtCore.QRect(504, 321, 260, 50))
        self.telefonoLineEdit.setMaxLength(9)
        self.telefonoLineEdit.setValidator(QIntValidator())
        self.telefonoLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.telefonoLineEdit.setPlaceholderText("Ingrese su numero de 9 digitos")
        
        # Etiqueta email y LineEdit
        self.emailLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.emailLabel.setGeometry(QtCore.QRect(14, 413, 24, 50))
        self.emailLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.emailLineEdit.setGeometry(QtCore.QRect(106, 413, 260, 50))
        self.emailLineEdit.setPlaceholderText("Ingrese su email")
        self.emailLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-Z@.0-9]+")))

        # Etiqueta domicilio y LineEdit
        self.domicilioLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.domicilioLabel.setGeometry(QtCore.QRect(399, 413, 40, 50))
        self.domicilioLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.domicilioLineEdit.setGeometry(QtCore.QRect(504, 413, 260, 50))
        self.domicilioLineEdit.setPlaceholderText("Ingrese domicilio")
        
        # Etiqueta email y LineEdit
        self.passwordLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.passwordLabel.setGeometry(QtCore.QRect(14, 505, 80, 50))
        self.passwordLineEdit = QtWidgets.QLineEdit(VentAgregarUsuario)
        self.passwordLineEdit.setGeometry(QtCore.QRect(106, 505, 260, 50))
        self.passwordLineEdit.setPlaceholderText("Ingrese su contraseña")
        
        # Etiqueta genero y ComboBox
        self.cargoLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.cargoLabel.setGeometry(QtCore.QRect(399, 505, 35, 50))
        self.cargoComboBox = QtWidgets.QComboBox(VentAgregarUsuario)
        self.cargoComboBox.setGeometry(QtCore.QRect(504, 505, 260, 50))
        self.cargoComboBox.setMinimumSize(QtCore.QSize(260, 50))
        self.cargoComboBox.setEditable(False)
        self.cargoComboBox.addItem("")
        self.cargoComboBox.addItem("")
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentAgregarUsuario)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner)
        
        # Btoton agregar y accion al pulsar
        self.btnAgregar = QtWidgets.QPushButton(VentAgregarUsuario)
        self.btnAgregar.setGeometry(QtCore.QRect(14, 592, 85, 50))
        self.btnAgregar.clicked.connect(self.onActionBtnAgregar)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentAgregarUsuario)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentAgregarUsuario.close)
        
        # Definir textos
        self.retranslateUi(VentAgregarUsuario)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentAgregarUsuario)

    # Metodo definir textos
    def retranslateUi(self, VentAgregarUsuario):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentAgregarUsuario.setWindowTitle(_translate("VentAgregarUsuario", "Agregar Usuario"))
        self.nombresLabel.setText(_translate("VentAgregarUsuario", "Nombres"))
        self.apellidosLabel.setText(_translate("VentAgregarUsuario", "Apellidos"))
        self.generoLabel.setText(_translate("VentAgregarUsuario", "Genero"))
        self.generoComboBox.setItemText(0, _translate("VentAgregarUsuario", "Masculino"))
        self.generoComboBox.setItemText(1, _translate("VentAgregarUsuario", "Femenino"))
        self.generoComboBox.setPlaceholderText("Seleccione género")
        self.fecha_nacimientoLabel.setText(_translate("VentAgregarUsuario", "Fecha de Nacimiento"))
        self.rutLabel.setText(_translate("VentAgregarUsuario", "Rut"))
        self.digito_verificadorLabel.setText(_translate("VentAgregarUsuario", "-"))
        self.telefonoLabel.setText(_translate("VentAgregarUsuario", "Telefono"))
        self.emailLabel.setText(_translate("VentAgregarUsuario", "Email"))
        self.domicilioLabel.setText(_translate("VentAgregarUsuario", "Domicilio"))
        self.passwordLabel.setText(_translate("VentAgregarUsuario", "Contraseña"))
        self.cargoLabel.setText(_translate("VentAgregarUsuario", "Cargo"))
        self.cargoComboBox.setItemText(0, _translate("VentAgregarUsuario", "Gerente"))
        self.cargoComboBox.setItemText(1, _translate("VentAgregarUsuario", "Vendedor"))
        self.cargoComboBox.setPlaceholderText("Seleccione género")
        self.btnAgregar.setText(_translate("VentAgregarUsuario", "Agregar \nUsuario"))
        
    # Mensajes de alerta, Vent emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()

    # Accion al clickear boton agregar
    def onActionBtnAgregar(self):
        nombres = self.nombresLineEdit.text()
        apellidos = self.apellidosLineEdit.text()
        genero = self.generoComboBox.currentText()
        fecha_nacimiento = self.fecha_nacimientoDateEdit.date().toString("dd/MM/yyyy")
        rut = self.rutLineEdit.text()
        digito_verificador = self.digito_verificadorLineEdit.text()
        telefono =self.telefonoLineEdit.text()
        email = self.emailLineEdit.text()
        domicilio = self.domicilioLineEdit.text()
        password = self.passwordLineEdit.text()
        cargo = self.cargoComboBox.currentText()
        # Convertir la k minuscula en mayuscula
        if digito_verificador == "k":
            digito_verificador = digito_verificador.replace("k", "K")
        # Pasar el rut al formato "xx.xxx.xxx-x"
        if len(rut) > 0:
            rutFormatted = "{:,}".format(int(rut)).replace(",", ".")
            rut_con_digito_verificador = rutFormatted + "-" + digito_verificador
        else:
            rut_con_digito_verificador = ""
        if nombres.strip() == "":
            self.alertBox("Falta agregar el nombre", "Falta un dato")
        elif apellidos.strip() == "":
            self.alertBox("Falta agregar el apellido", "Falta un dato")
        elif len(rut) < 7 or len(digito_verificador) != 1:
            self.alertBox("Faltan números en el rut o el dígito verificador", "Falta un dato")
        elif self.verificarRutExistente(rut_con_digito_verificador):
            self.alertBox("El rut ya pertenece a un usuario", "RUT duplicado")
        elif len(telefono) != 9:
            self.alertBox("Faltan numeros en el telefono", "Falta un dato")
        elif '@' not in email or '.' not in email:
            self.alertBox("Falta agregar '@' o '.' en el email", "Falta un dato")
        elif domicilio.strip() == "":
            self.alertBox("Falta agregar el domicilio", "Falta un dato")
        elif len(password) < 4:
            self.alertBox("La contraseña debe tener al menos 4 caracteres", "Contraseña inválida")
        else:
            Usuario.agregar_usuario(nombres, apellidos, domicilio, genero, fecha_nacimiento, rut_con_digito_verificador, email, password, telefono, cargo, )
            self.alertBox("El usuario: "+nombres+" "+apellidos+" ha sido ingresado", "Se ha ingresado el Usuario")
            
            # Limpiar LineEdit
            self.nombresLineEdit.setText("")
            self.apellidosLineEdit.setText("")
            self.fecha_nacimientoDateEdit.setDate(QtCore.QDate.fromString("01/01/2000", "dd/MM/yyyy"))
            self.rutLineEdit.setText("")
            self.digito_verificadorLineEdit.setText("")
            self.emailLineEdit.setText("")
            self.telefonoLineEdit.setText("")
            self.domicilioLineEdit.setText("")
            self.passwordLineEdit.setText("")
    
    # Verificar si ya existe el rut
    def verificarRutExistente(self, rut):
        with open('ArchivosCSV/Usuario.csv', 'r') as file:
            encabezados = csv.reader(file)
            for fila in encabezados:
                if fila[7] == rut:
                    return True
        return False