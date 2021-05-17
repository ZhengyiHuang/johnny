import sys
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QComboBox, QApplication


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        box = QComboBox(self)
        box.resize(box.sizeHint())
        box.setStyleSheet("""
QComboBox::drop-down {border-width: 0px;}
QComboBox::down-arrow {image: url(noimg); border-width: 0px;}
""")
        box.move(50, 50)

        #Using the palette doesn't work:
        pal = box.palette()
        pal.setColor(box.backgroundRole(), QColor())
        box.setAutoFillBackground(True)
        box.setPalette(pal)

        self.setGeometry(300, 300, 250, 150)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())