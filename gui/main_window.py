from PyQt5 import QtWidgets, QtCore
from gui.radius_page import RadiusPage
from gui.ac_a_page import ACAPage
from gui.astigmatism_page import AstigmatismPage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Optometrist Calculator')
        self.setGeometry(100, 100, 1000, 600)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QHBoxLayout(self.central_widget)

        self.init_navigation()
        self.init_pages()

    def init_navigation(self):
        self.nav_list = QtWidgets.QListWidget()
        self.nav_list.addItem('Radius of Curvature')
        self.nav_list.addItem('AC/A Ratio')
        self.nav_list.addItem('Astigmatism Test')
        self.nav_list.currentRowChanged.connect(self.display_page)
        self.layout.addWidget(self.nav_list)

    def init_pages(self):
        self.pages = QtWidgets.QStackedWidget()
        self.pages.addWidget(RadiusPage())
        self.pages.addWidget(ACAPage())
        self.pages.addWidget(AstigmatismPage())
        self.layout.addWidget(self.pages)

    def display_page(self, index):
        self.pages.setCurrentIndex(index)

def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
