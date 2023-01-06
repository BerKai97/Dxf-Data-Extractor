from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main import AssetCounter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        MainWindow.setMinimumSize(QtCore.QSize(300, 100))
        MainWindow.setMaximumSize(QtCore.QSize(300, 100))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 10, 150, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openFileNameDialog)

        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(100, 50, 150, 25))
        self.statusLabel.setObjectName("statusLabel")

        # put everything in a vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.statusLabel)
       
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DXF Asset Counter", "DXF Asset Counter"))
        self.pushButton.setText(_translate("MainWindow", "DXF Dosyası Seç"))
        
        self.statusLabel.setText(_translate("MainWindow", "Durum: Dosya seçilmedi."))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        fileName, _ = QFileDialog.getOpenFileName(None,"DXF Dosyası Seç", "","DXF Files (*.dxf)", options=options)
        if fileName:
            print(fileName)
            self.count_assets(fileName)

    def count_assets(self, file_path):
  
        self.statusLabel.setText("Durum: İşlem yapılıyor...")
        QtWidgets.QApplication.processEvents()

        ac = AssetCounter(file_path)
        result = ac.count_assets()
        if result == True:
            self.statusLabel.setText("Durum: İşlem başarılı.")
        else:
            self.statusLabel.setText("Durum: İşlem başarısız.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
