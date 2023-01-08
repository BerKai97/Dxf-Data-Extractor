from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main import DDE
import qt_question
import sys
from messages import Messages, Message, Language

class Ui_MainWindow(object):
    def __init__(self):
        self.file_dxf = None
        self.file_prices_csv = None
        self.height = 250

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, self.height)
        MainWindow.setMinimumSize(QtCore.QSize(300, self.height))
        MainWindow.setMaximumSize(QtCore.QSize(300, self.height))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.button_selectFile = QtWidgets.QPushButton(self.centralwidget)
        self.button_selectFile.setGeometry(QtCore.QRect(100, 10, 150, 25))
        self.button_selectFile.setObjectName("pushButton")
        self.button_selectFile.clicked.connect(self.openFileNameDialog)

        self.button_selectPriceCsv = QtWidgets.QPushButton(self.centralwidget)
        self.button_selectPriceCsv.setGeometry(QtCore.QRect(100, 10, 150, 25))
        self.button_selectPriceCsv.setObjectName("pushButton")
        self.button_selectPriceCsv.clicked.connect(self.openFileNameDialogPriceCsv)

        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(100, 10, 150, 25))
        self.button_start.setObjectName("startButton")
        self.button_start.clicked.connect(lambda: self.process_data(self.file_dxf, self.file_prices_csv))


        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(100, 50, 150, 25))
        self.statusLabel.setObjectName("statusLabel")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.addWidget(self.button_selectFile)
        self.verticalLayout.addWidget(self.button_selectPriceCsv)
        self.verticalLayout.addWidget(self.button_start)
        self.verticalLayout.addWidget(self.statusLabel)
       
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DXF Data Extractor", "DXF Data Extractor"))
        self.button_selectPriceCsv.setText(_translate("MainWindow", Messages().get(Message.SELECT_CSV_FILE)))
        self.button_selectFile.setText(_translate("MainWindow", Messages().get(Message.SELECT_DXF_FILE)))
        self.button_start.setText(_translate("MainWindow", Messages().get(Message.START)))
        
        self.statusLabel.setText(_translate("MainWindow", Messages().get(Message.STATUS_IDLE)))

    def openFileNameDialogPriceCsv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        fileName, _ = QFileDialog.getOpenFileName(None,"Select a Price CSV File", "","CSV Files (*.csv)", options=options)
        if fileName:
            self.file_prices_csv = fileName
            print(fileName)
            self.button_selectFile.setEnabled(True)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        fileName, _ = QFileDialog.getOpenFileName(None,"Select a DXF File", "","DXF Files (*.dxf)", options=options)
        if fileName:
            self.file_dxf = fileName
            print(fileName)
            self.button_start.setEnabled(True)
        
            # self.count_assets(fileName)


    def process_data(self, file_dxf, file_prices_csv):
  
        if file_dxf == None:
            self.statusLabel.setText(Messages().get(Message.NODXFFILE))
            self.statusLabel.setStyleSheet("QLabel { color : red; }")
            return
        if file_prices_csv == None:
            question = qt_question.QuestionWidget().initUI(Messages().get(Message.NOPRICEFILE))
            if question == True:
                pass
            else:
                return

            
        self.statusLabel.setText(Messages().get(Message.STATUS_PROCESSING))
        self.statusLabel.setStyleSheet("QLabel { color : orange; }")
        QtWidgets.QApplication.processEvents()

        ac = DDE(file_dxf)
        result = ac.count_assets()
        if result == True:
            self.statusLabel.setText(Messages().get(Message.STATUS_COUNTED))
            self.statusLabel.setStyleSheet("QLabel { color : orange; }")
            QtWidgets.QApplication.processEvents()
            
            if file_prices_csv == None:
                self.statusLabel.setText(Messages().get(Message.STATUS_COMPNOTCOST))
                self.statusLabel.setStyleSheet("QLabel { color : green; }")
                QtWidgets.QApplication.processEvents()
                return

            cost = ac.calculate_price(file_prices_csv)
            if cost != None:
                self.statusLabel.setText(Messages().get(Message.STATUS_COMPCOST) + str(cost))
                self.statusLabel.setStyleSheet("QLabel { color : green; }")
                QtWidgets.QApplication.processEvents()


        else:
            self.statusLabel.setText(Messages().get(Message.STATUS_ERROR))
            self.statusLabel.setStyleSheet("QLabel { color : red; }")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
