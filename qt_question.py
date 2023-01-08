import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from messages import Messages, Message, Language

class QuestionWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Are you sure?'
        # self.initUI()

    def initUI(self, msg="Are you sure?"):
        self.setWindowTitle(self.title)

        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle("")
        box.setText(msg)
        box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText(Messages().get(Message.YES))
        buttonN = box.button(QMessageBox.No)
        buttonN.setText(Messages().get(Message.NO))
        box.exec_()
        if box.clickedButton() == buttonY:
            return True

        else:
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuestionWidget()
    sys.exit(app.exec_())