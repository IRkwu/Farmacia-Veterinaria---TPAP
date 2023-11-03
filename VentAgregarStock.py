from PyQt5.QtWidgets import QLabel, QSpinBox, QDateEdit, QDialog, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate

class AgregarStockDialog(QDialog):
    def __init__(self, tipo='', parent=None):
        super(AgregarStockDialog, self).__init__(parent)    
        self.tipo = tipo    
        self.setupUi(self)

        # Elimina el botón ? de la barra de titulo
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def setupUi(self, AgregarStockDialog):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')

        AgregarStockDialog.resize(260, 140)
        AgregarStockDialog.setMinimumSize(QtCore.QSize(260, 140))
        AgregarStockDialog.setMaximumSize(QtCore.QSize(260, 140))

        AgregarStockDialog.setWindowIcon(IconoTitulo)

        # Etiqueta stock y SpinBox
        self.stockLabel = QtWidgets.QLabel(AgregarStockDialog)
        self.stockLabel.setGeometry(QtCore.QRect(20, 20, 100, 25))
        self.stockSpinBox = QtWidgets.QSpinBox(AgregarStockDialog)
        self.stockSpinBox.setGeometry(QtCore.QRect(130, 20, 110, 25))
        self.stockSpinBox.setMinimum(1)
        self.stockSpinBox.setMaximum(999)
        
        # Etiqueta caducidad y DateEdit
        self.caducidadLabel = QtWidgets.QLabel(AgregarStockDialog)
        self.caducidadLabel.setGeometry(QtCore.QRect(20, 60, 100, 25))
        self.caducidadDateEdit = QtWidgets.QDateEdit(AgregarStockDialog)
        self.caducidadDateEdit.setGeometry(QtCore.QRect(130, 60, 110, 25))
        # Fecha actual, para que no se ingrese productos nuevos anteayer lol
        self.caducidadDateEdit.setMinimumDate(QDate.currentDate())

        # Boton confirmar y accion al pulsar
        self.btnConfirmar = QtWidgets.QPushButton(AgregarStockDialog)
        self.btnConfirmar.setGeometry(QtCore.QRect(135, 100, 115, 23))
        self.btnConfirmar.clicked.connect(self.accept)

        # Boton cancelar y accion al pulsar
        self.bntCancelar = QtWidgets.QPushButton(AgregarStockDialog)
        self.bntCancelar.setGeometry(QtCore.QRect(10, 100, 115, 23))
        self.bntCancelar.clicked.connect(self.reject)
        
        if self.tipo == "Experimental":
            AgregarStockDialog.resize(260, 140)
            AgregarStockDialog.setMinimumSize(QtCore.QSize(260, 180))
            AgregarStockDialog.setMaximumSize(QtCore.QSize(260, 180))
            self.btnConfirmar.setGeometry(QtCore.QRect(135, 140, 115, 23))
            self.bntCancelar.setGeometry(QtCore.QRect(10, 140, 115, 23))
            # Etiqueta caducidad y DateEdit
            self.fechaEntregaLabel = QtWidgets.QLabel(AgregarStockDialog)
            self.fechaEntregaLabel.setGeometry(QtCore.QRect(20, 100, 100, 25))
            self.fechaEntregaDateEdit = QtWidgets.QDateEdit(AgregarStockDialog)
            self.fechaEntregaDateEdit.setGeometry(QtCore.QRect(130, 100, 110, 25))
            self.fechaEntregaDateEdit.setMinimumDate(QDate.currentDate())
            self.fechaEntregaLabel.setText("Fecha de Entrega")
            
        self.retranslateUi(AgregarStockDialog)
        QtCore.QMetaObject.connectSlotsByName(AgregarStockDialog)

    def retranslateUi(self, AgregarStockDialog):
        _translate = QtCore.QCoreApplication.translate
        AgregarStockDialog.setWindowTitle(_translate("AgregarStockDialog", "Agregar Lote"))
        self.stockLabel.setText(_translate("AgregarStockDialog", "Nuevo Stock:"))
        self.caducidadLabel.setText(_translate("AgregarStockDialog", "Fecha de Caducidad:"))
        self.btnConfirmar.setText(_translate("AgregarStockDialog", "Confirmar Cambios"))
        self.bntCancelar.setText(_translate("AgregarStockDialog", "Cancelar"))

    def get_stock(self):
        return self.stockSpinBox.text()

    def get_fecha_caducidad(self):
        return self.caducidadDateEdit.date().toString("dd/MM/yyyy")
    
    def get_fecha_entrega(self):
        if self.tipo == "Experimental":
            fecha_entrega = self.fechaEntregaDateEdit.date().toString("dd/MM/yyyy")
        else:
            fecha_entrega = "No Aplica"
        return fecha_entrega
        