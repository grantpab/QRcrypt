import sys
from PyQt5 import QtWidgets, uic
import Encoder

qtCreatorFile = "Window.ui"  # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.generatebutton.clicked.connect(self.callencoder)

    def callencoder(self):
        textin = (self.input_textbox.toPlainText())
        EC = (self.inputEC.currentText())
        print(textin)
        print(EC)
        Encoder.encoderfunc(textin, EC)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()

    sys.exit(app.exec_())
