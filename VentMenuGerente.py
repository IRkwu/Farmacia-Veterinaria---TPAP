
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from VentAgregarCliente import VentAgregarCliente
from VentListaClientes import VentListaClientes
from VentCarrito import VentCarrito
from VentAgregarUsuario import VentAgregarUsuario
from VentListaUsuarios import VentListaUsuarios
from VentModificarStock import VentModificarStock
from VentModificarMedicamentos import VentModificarMedicamentos
from VentHistorialBoletas import VentHistorialBoletas

class VentMenuGerente(object):
    def setupUi(self, VentMenuGerente):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        ImgAgregarCliente = QtGui.QIcon('Imagenes/agregar_cliente.png')
        ImgModificarCliente = QtGui.QIcon('Imagenes/modificar_cliente.png')
        ImgAgregarUsuario = QtGui.QIcon('Imagenes/agregar_usuario.png')
        ImgModificarUsuario = QtGui.QIcon('Imagenes/modificar_usuario.png')
        ImgModificarMedicamento = QtGui.QIcon('Imagenes/modificar_medicamento.png')
        ImgModificarStock = QtGui.QIcon('Imagenes/modificar_stock.png')
        ImgCarrito = QtGui.QIcon('Imagenes/carrito.png')
        ImgBoletas = QtGui.QIcon('Imagenes/historial_boletas.png')
        ImgCerrar = QtGui.QIcon('Imagenes/btn_cerrar.png')
        
        VentMenuGerente.setWindowIcon(IconoTitulo)
        
        VentMenuGerente.resize(700, 435)
        VentMenuGerente.setMinimumSize(QtCore.QSize(700, 435))
        VentMenuGerente.setMaximumSize(QtCore.QSize(700, 435))
        
        # Etiqueta imagen fondo
        self.imagen_fondoLabel = QtWidgets.QLabel(VentMenuGerente)
        self.imagen_fondoLabel.setGeometry(QtCore.QRect(0, 0, 700, 90))
        self.imagen_fondoLabel.setText("")
        self.imagen_fondoLabel.setPixmap(ImagenBanner.scaled(700, 90))
        
        # Boton Agregar Cliente
        self.BtnAgregarCliente = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnAgregarCliente.setGeometry(QtCore.QRect(125, 121, 200, 50))
        self.BtnAgregarCliente.setIcon(ImgAgregarCliente)
        self.BtnAgregarCliente.setIconSize(QtCore.QSize(200, 50))
        self.BtnAgregarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnAgregarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Editar Cliente
        self.BtnEditarCliente = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnEditarCliente.setGeometry(QtCore.QRect(368, 121, 200, 50))
        self.BtnEditarCliente.setIcon(ImgModificarCliente)
        self.BtnEditarCliente.setIconSize(QtCore.QSize(200, 50))
        self.BtnEditarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnEditarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Agregar Usuario
        self.BtnAgregarUsuario = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnAgregarUsuario.setGeometry(QtCore.QRect(125, 201, 200, 50))
        self.BtnAgregarUsuario.setIcon(ImgAgregarUsuario)
        self.BtnAgregarUsuario.setIconSize(QtCore.QSize(200, 50))
        self.BtnAgregarUsuario.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnAgregarUsuario.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Editar Usuario
        self.BtnEditarUsuario = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnEditarUsuario.setGeometry(QtCore.QRect(368, 201, 200, 50))
        self.BtnEditarUsuario.setIcon(ImgModificarUsuario)
        self.BtnEditarUsuario.setIconSize(QtCore.QSize(200, 50))
        self.BtnEditarUsuario.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnEditarUsuario.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Modificar Medicamentos
        self.BtnModificarMedicamentos = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnModificarMedicamentos.setGeometry(QtCore.QRect(125, 281, 200, 51))
        self.BtnModificarMedicamentos.setIcon(ImgModificarMedicamento)
        self.BtnModificarMedicamentos.setIconSize(QtCore.QSize(200, 50))
        self.BtnModificarMedicamentos.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnModificarMedicamentos.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Modificar Stock
        self.BtnModificarStock = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnModificarStock.setGeometry(QtCore.QRect(368, 281, 200, 51))
        self.BtnModificarStock.setIcon(ImgModificarStock)
        self.BtnModificarStock.setIconSize(QtCore.QSize(200, 50))
        self.BtnModificarStock.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnModificarStock.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Historial Boletas
        self.BtnBoletas = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnBoletas.setGeometry(QtCore.QRect(125, 361, 200, 50))
        self.BtnBoletas.setIcon(ImgBoletas)
        self.BtnBoletas.setIconSize(QtCore.QSize(200, 50))
        self.BtnBoletas.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnBoletas.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Carrito
        self.BtnCarrito = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnCarrito.setGeometry(QtCore.QRect(368, 361, 200, 50))
        self.BtnCarrito.setIcon(ImgCarrito)
        self.BtnCarrito.setIconSize(QtCore.QSize(200, 50))
        self.BtnCarrito.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCarrito.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Cerrar Menu
        self.BtnCerrarMenu = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnCerrarMenu.setGeometry(QtCore.QRect(648, 10, 40, 40))
        self.BtnCerrarMenu.setIcon(ImgCerrar)
        self.BtnCerrarMenu.setIconSize(QtCore.QSize(40, 40))
        self.BtnCerrarMenu.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCerrarMenu.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Acción clickear botones
        self.BtnAgregarCliente.clicked.connect(lambda: self.cambiarVent(VentAgregarCliente))
        self.BtnEditarCliente.clicked.connect(lambda: self.cambiarVent(VentListaClientes))
        self.BtnAgregarUsuario.clicked.connect(lambda: self.cambiarVent(VentAgregarUsuario))
        self.BtnEditarUsuario.clicked.connect(lambda: self.cambiarVent(VentListaUsuarios))
        self.BtnCarrito.clicked.connect(lambda: self.cambiarVent(VentCarrito))
        self.BtnBoletas.clicked.connect(lambda: self.cambiarVent(VentHistorialBoletas))
        self.BtnModificarMedicamentos.clicked.connect(lambda: self.cambiarVent(VentModificarMedicamentos))
        self.BtnModificarStock.clicked.connect(lambda: self.cambiarVent(VentModificarStock))
        self.BtnCerrarMenu.clicked.connect(VentMenuGerente.close)
        
        
        self.retranslateUi(VentMenuGerente)
        QtCore.QMetaObject.connectSlotsByName(VentMenuGerente)

    def retranslateUi(self, VentMenuGerente):
        _translate = QtCore.QCoreApplication.translate
        VentMenuGerente.setWindowTitle(_translate("VentMenuGerente", "Menu Gerente"))

    def cambiarVent(self, nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()