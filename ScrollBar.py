import sys

from sys import exit

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QScrollBar
from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtWidgets import QToolBar, QStatusBar
from PySide6.QtWidgets import QFileDialog, QMessageBox

from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtGui import QColor, QPainter, QPainterPath, QPen, QBrush, QIcon
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsPathItem, \
    QGraphicsSimpleTextItem, QGraphicsRectItem, QGraphicsItemGroup

from PySide6.QtGui import QFontMetrics


# ******************************************************************************
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Johnny's Test Box")
        self.resize(500, 500)
        self.initUI()

    def initUI(self):
        sb = QScrollBar(self)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    exit(application.exec_())