import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from VentHistorialBoletas import VentHistorialBoletas
from VentCarrito import VentCarrito
from VentMenuGerente import VentMenuGerente
from VentModificarMedicamentos import VentModificarMedicamentos
from VentListaUsuarios import VentListaUsuarios
from VentModificarStock import VentModificarStock
from VentIniciarSesion import VentIniciarSesion

class main(QMainWindow):
           
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = VentIniciarSesion()
        self.ui.setupUi(self)
                
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())