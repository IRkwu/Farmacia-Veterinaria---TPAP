from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from VentAgregarCliente import VentAgregarCliente
from VentCarrito import VentCarrito
from VentModificarStock import VentModificarStock

class VentMenuVendedor(object):
    def setupUi(self, VentMenuVendedor):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        ImgAgregarCliente = QtGui.QIcon('Imagenes/agregar_cliente.png')
        ImgModificarStock = QtGui.QIcon('Imagenes/modificar_stock.png')
        ImgCarrito = QtGui.QIcon('Imagenes/carrito.png')
        ImgCerrar = QtGui.QIcon('Imagenes/btn_cerrar.png')
        
        VentMenuVendedor.setWindowIcon(IconoTitulo)
        
        VentMenuVendedor.resize(600, 380)
        VentMenuVendedor.setMinimumSize(QtCore.QSize(600, 380))
        VentMenuVendedor.setMaximumSize(QtCore.QSize(600, 380))
        
        # Etiqueta imagen fondo
        self.imagen_fondoLabel = QtWidgets.QLabel(VentMenuVendedor)
        self.imagen_fondoLabel.setGeometry(QtCore.QRect(-100, 0, 1000, 90))
        self.imagen_fondoLabel.setText("")
        self.imagen_fondoLabel.setPixmap(ImagenBanner.scaled(800, 90))
        
        # Boton Agregar Cliente
        self.BtnAgregarCliente = QtWidgets.QPushButton(VentMenuVendedor)
        self.BtnAgregarCliente.setGeometry(QtCore.QRect(201, 121, 200, 50))
        self.BtnAgregarCliente.setIcon(ImgAgregarCliente)
        self.BtnAgregarCliente.setIconSize(QtCore.QSize(200, 50))
        self.BtnAgregarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnAgregarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Carrito
        self.BtnCarrito = QtWidgets.QPushButton(VentMenuVendedor)
        self.BtnCarrito.setGeometry(QtCore.QRect(201, 201, 200, 50))
        self.BtnCarrito.setIcon(ImgCarrito)
        self.BtnCarrito.setIconSize(QtCore.QSize(200, 50))
        self.BtnCarrito.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCarrito.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Carrito
        self.BtnModificarStock = QtWidgets.QPushButton(VentMenuVendedor)
        self.BtnModificarStock.setGeometry(QtCore.QRect(201, 281, 200, 50))
        self.BtnModificarStock.setIcon(ImgModificarStock)
        self.BtnModificarStock.setIconSize(QtCore.QSize(200, 50))
        self.BtnModificarStock.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnModificarStock.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Cerrar Menu
        self.BtnCerrarMenu = QtWidgets.QPushButton(VentMenuVendedor)
        self.BtnCerrarMenu.setGeometry(QtCore.QRect(548, 10, 40, 40))
        self.BtnCerrarMenu.setIcon(ImgCerrar)
        self.BtnCerrarMenu.setIconSize(QtCore.QSize(40, 40))
        self.BtnCerrarMenu.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCerrarMenu.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Acción clickear botones
        self.BtnAgregarCliente.clicked.connect(lambda: self.cambiarVent(VentAgregarCliente))
        self.BtnCarrito.clicked.connect(lambda: self.cambiarVent(VentCarrito))
        self.BtnModificarStock.clicked.connect(lambda: self.cambiarVent(VentModificarStock))
        self.BtnCerrarMenu.clicked.connect(VentMenuVendedor.close)
        
        self.retranslateUi(VentMenuVendedor)
        QtCore.QMetaObject.connectSlotsByName(VentMenuVendedor)

    def retranslateUi(self, VentMenuVendedor):
        _translate = QtCore.QCoreApplication.translate
        VentMenuVendedor.setWindowTitle(_translate("VentMenuVendedor", "Menu Vendedor"))
        
    def cambiarVent(self, nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()