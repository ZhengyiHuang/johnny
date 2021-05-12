import sys

from sys import exit

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
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
        self.aboutButton()
        self.helpButton()

    def aboutButton(self):
        aboutMessageBox = QMessageBox(self)
        aboutMessageBox.setWindowTitle("About this program")
        aboutMessageBox.setText("<p><h4>This program is developed by engineers from EEE231 Group A. "
                                "The program is written in Python and most of the UI are written using Pyside.<br /> "
                                "</h4></p> "
                                "<p><h4>Acknowledgements to the programmers who contributed to this process (in no "
                                "particular order). </h4>"
                                "Joshua Adewoye <br />"
                                "Edward Atkinson <br />"
                                "Yang Cen <br />"
                                "Zhengyi Huang <br />"
                                "Iyad Khairallah <br />"
                                "Yufei Liu <br />"
                                "Chi Hei Tan <br />"
                                "Brian Wu <br />"
                                "Qidong Ye <br /></p>"
                                "<p><h4>Special thanks to (in no particular order) </h4>"
                                "Dr Peter Rockett<br />"
                                "Dr Charith Abhayaratne</p>")
        aboutMessageBox.setIcon(QMessageBox.Information)
        aboutMessageBox.open()

    def helpButton(self):
        helpMessageBox = QMessageBox(self)
        helpMessageBox.setWindowTitle("Help")
        helpMessageBox.setText('<h5>Please open this link for help</h5>'
                               '<a href="https://github.com/pirlite2/EEE231-group-A/blob/main/README.md">'
                               'link')
        helpMessageBox.setIcon(QMessageBox.Information)
        helpMessageBox.open()




    # ******************************************************************************


# ******************************************************************************
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    exit(application.exec_())

