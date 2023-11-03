import random
import csv
from PyQt5.QtWidgets import QLabel, QSpinBox, QDialog, QPushButton, QMessageBox, QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate

class AgregarMedicamentos(QDialog):
    def __init__(self, parent=None):
        super(AgregarMedicamentos, self).__init__(parent)
        self.setupUi(self)

        # Elimina el botón ? de la barra de título
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def setupUi(self, AgregarMedicamentos):
        AgregarMedicamentos.resize(450, 400)
        AgregarMedicamentos.setMinimumSize(QtCore.QSize(450, 400))
        AgregarMedicamentos.setMaximumSize(QtCore.QSize(450, 400))

        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        AgregarMedicamentos.setWindowIcon(IconoTitulo)

        self.imagen_on_topLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(-150, 0, 600, 90))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(750, 80))
        
        self.nombreLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.nombreLabel.setGeometry(QtCore.QRect(20, 105, 47, 13))
        self.nombreLineEdit = QtWidgets.QLineEdit(AgregarMedicamentos)
        self.nombreLineEdit.setGeometry(QtCore.QRect(20, 125, 121, 31))

        self.precioLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.precioLabel.setGeometry(QtCore.QRect(20, 165, 47, 13))
        self.precioLineEdit = QtWidgets.QLineEdit(AgregarMedicamentos)
        self.precioLineEdit.setGeometry(QtCore.QRect(20, 185, 121, 31))
        self.precioLineEdit.setValidator(QtGui.QIntValidator())
        
        self.lote_inicialLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.lote_inicialLabel.setGeometry(QtCore.QRect(20, 225, 60, 13))
        self.lote_inicialSpinBox = QtWidgets.QSpinBox(AgregarMedicamentos)
        self.lote_inicialSpinBox.setGeometry(QtCore.QRect(20, 245, 121, 31))
        self.lote_inicialSpinBox.setMinimum(1)
        self.lote_inicialSpinBox.setMaximum(999)
        
        self.fechaCaducidadLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.fechaCaducidadLabel.setGeometry(QtCore.QRect(170, 245, 100, 31))
        self.fechaCaducidadDateEdit = QtWidgets.QDateEdit(AgregarMedicamentos)
        self.fechaCaducidadDateEdit.setGeometry(QtCore.QRect(280, 245, 150, 31))
        self.fechaCaducidadDateEdit.setMinimumDate(QDate.currentDate())
        
        self.tipoLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.tipoLabel.setGeometry(QtCore.QRect(20, 285, 100, 13))
        self.tipoComboBox = QComboBox(AgregarMedicamentos)
        self.tipoComboBox.setGeometry(QtCore.QRect(20, 305, 121, 31))
        self.tipoComboBox.addItem("Nacional")
        self.tipoComboBox.addItem("Experimental")
        self.tipoComboBox.currentTextChanged.connect(self.onTipoComboBoxChanged)

        self.descripcionLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.descripcionLabel.setGeometry(QtCore.QRect(170, 100, 61, 16))
        self.descripcionTextEdit = QtWidgets.QTextEdit(AgregarMedicamentos)
        self.descripcionTextEdit.setGeometry(QtCore.QRect(170, 125, 261, 100))
        self.descripcionTextEdit.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.descripcionTextEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)

        self.fechaEntregaLabel = QtWidgets.QLabel(AgregarMedicamentos)
        self.fechaEntregaLabel.setGeometry(QtCore.QRect(170, 305, 100, 31))
        self.fechaEntregaDateEdit = QtWidgets.QDateEdit(AgregarMedicamentos)
        self.fechaEntregaDateEdit.setGeometry(QtCore.QRect(280, 305, 150, 31))
        self.fechaEntregaDateEdit.setMinimumDate(QDate.currentDate())
        self.fechaEntregaLabel.setVisible(False)
        self.fechaEntregaDateEdit.setVisible(False)

        self.btnAgregar = QtWidgets.QPushButton(AgregarMedicamentos)
        self.btnAgregar.setGeometry(QtCore.QRect(320, 350, 111, 41))
        self.btnAgregar.clicked.connect(self.onActionBtnConfirmar)

        self.btnVolver = QtWidgets.QPushButton(AgregarMedicamentos)
        self.btnVolver.setGeometry(QtCore.QRect(20, 350, 101, 41))
        self.btnVolver.clicked.connect(AgregarMedicamentos.close)

        self.retranslateUi(AgregarMedicamentos)
        QtCore.QMetaObject.connectSlotsByName(AgregarMedicamentos)

    def retranslateUi(self, AgregarMedicamentos):
        _translate = QtCore.QCoreApplication.translate
        AgregarMedicamentos.setWindowTitle(_translate("AgregarMedicamentos", "Agregar Medicamentos"))
        self.nombreLabel.setText(_translate("AgregarMedicamentos", "Nombre"))
        self.precioLabel.setText(_translate("AgregarMedicamentos", "Precio"))
        self.lote_inicialLabel.setText(_translate("AgregarMedicamentos", "Lote Inicial"))
        self.tipoLabel.setText(_translate("AgregarMedicamentos", "Tipo de Medicamento"))
        self.descripcionLabel.setText(_translate("AgregarMedicamentos", "Descripción"))
        self.btnAgregar.setText(_translate("AgregarMedicamentos", "Agregar"))
        self.btnVolver.setText(_translate("AgregarMedicamentos", "Volver"))
        self.fechaEntregaLabel.setText(_translate("AgregarMedicamentos", "Fecha Entrega"))
        self.fechaCaducidadLabel.setText(_translate("AgregarMedicamentos", "Fecha Caducidad"))
        
    # Mensajes de alerta, Ventana emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()

    def onActionBtnConfirmar(self):
        nombre = self.nombreLineEdit.text()
        precio = self.precioLineEdit.text()
        descripcion = self.descripcionTextEdit.toPlainText()
        lote = self.lote_inicialSpinBox.text()
        tipo = self.tipoComboBox.currentText()
        fecha_entrega = self.fechaEntregaDateEdit.date().toString("dd/MM/yyyy")
        fecha_caducidad = self.fechaCaducidadDateEdit.date().toString("dd/MM/yyyy")
        
        if nombre.strip() == "":
            self.alertBox("Falta ingresar el nombre", "Falta un dato")
        elif self.verificarMedicamentoExistente(nombre):
            self.alertBox("El medicamento ya existe, no se puede agregar nuevamente", "Medicamento duplicado")
        elif precio.strip() == "":
            self.alertBox("Falta ingresar el precio", "Falta un dato")
        elif descripcion.strip() == "":
            self.alertBox("Falta ingresar la descripción", "Falta un dato")
        else:
            if self.tipoComboBox.currentText() == "Experimental":
                mensaje = f"Se ha ingresado el medicamento:\nNombre: {nombre}\nPrecio: {precio}\nDescripción: {descripcion}\nTipo: {tipo}\nLote: {lote}\nFecha de Caducidad: {fecha_caducidad}\nFecha de Entrega: {fecha_entrega}"
            else:
                mensaje = f"Se ha ingresado el medicamento:\nNombre: {nombre}\nPrecio: {precio}\nDescripción: {descripcion}\nTipo: {tipo}\nLote: {lote} Unidades\nFecha de Caducidad: {fecha_caducidad}"
                fecha_entrega = ""
            self.alertBox(mensaje, "Lista Actualizada")
            self.accept()
            
    def onTipoComboBoxChanged(self, text):
        if text == "Experimental":
            self.fechaEntregaLabel.setVisible(True)
            self.fechaEntregaDateEdit.setVisible(True)
        else:
            self.fechaEntregaLabel.setVisible(False)
            self.fechaEntregaDateEdit.setVisible(False)
            
    def verificarMedicamentoExistente(self, nombre):
        with open('ArchivosCSV/Medicamentos.csv', 'r') as file:
            encabezados = csv.reader(file)
            for fila in encabezados:
                if fila[1].lower() == nombre.lower():
                    return True
        return False
            
    def get_nombre(self):
        return self.nombreLineEdit.text()

    def get_precio(self):
        return self.precioLineEdit.text()

    def get_descripcion(self):
        return self.descripcionTextEdit.toPlainText()

    def get_tipo(self):
        return self.tipoComboBox.currentText()
    
    def get_fecha_entrega(self):
        if self.tipoComboBox.currentText() == "Experimental":
            fecha_entrega = self.fechaEntregaDateEdit.date().toString("dd/MM/yyyy")
        else:
            fecha_entrega = "No Aplica"
        return fecha_entrega
    
    def get_fecha_caducidad(self):
        return self.fechaCaducidadDateEdit.date().toString("dd/MM/yyyy")

    def get_lote_inicial(self):
        return self.lote_inicialSpinBox.text()
    
    def get_id(self):
        with open('ArchivosCSV/Medicamentos.csv', 'r') as file:
            reader = csv.reader(file)
            id_existente = set()
            next(reader)  # Omitir la primera fila
            for row in reader:
                id_existente.add(int(row[0]))
    
        ultima_id = None
        for i in range(1, len(id_existente) + 2):
            if i not in id_existente:
                ultima_id = i
                break
            
        nueva_id = str(ultima_id).zfill(3)
        return nueva_id