import sys
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QComboBox, QApplication, QScrollBar


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Johnny's Test")
        self.resize(500, 500)
        self.initUI()

    def initUI(self):
        sb = QScrollBar(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
