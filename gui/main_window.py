from PyQt5 import QtWidgets, QtGui, QtCore
from gui.radius_page import RadiusPage
from gui.ac_a_page import ACAPage
from gui.astigmatism_page import AstigmatismPage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Optometrist Calculator')
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QHBoxLayout(self.central_widget)

        self.init_navigation()
        self.init_pages()
        self.init_menu()

    def init_navigation(self):
        self.nav_widget = QtWidgets.QWidget()
        self.nav_layout = QtWidgets.QVBoxLayout(self.nav_widget)

        self.nav_list = QtWidgets.QListWidget()
        self.nav_list.addItem('Radius of Curvature')
        self.nav_list.addItem('AC/A Ratio')
        self.nav_list.addItem('Astigmatism Test')
        self.nav_list.currentRowChanged.connect(self.display_page)

        self.nav_list.setStyleSheet("""
            QListWidget {
                background-color: #2e2e2e;
                color: #ffffff;
                border: 1px solid #4a4a4a;
            }
            QListWidget::item {
                height: 50px;
                padding: 10px;
            }
            QListWidget::item:selected {
                background-color: #4a4a4a;
            }
        """)

        self.nav_layout.addWidget(self.nav_list)
        self.layout.addWidget(self.nav_widget)

    def init_pages(self):
        self.pages = QtWidgets.QStackedWidget()
        self.pages.addWidget(RadiusPage())
        self.pages.addWidget(ACAPage())
        self.pages.addWidget(AstigmatismPage())
        self.layout.addWidget(self.pages)

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        load_action = QtWidgets.QAction('Load', self)
        save_action = QtWidgets.QAction('Save', self)
        exit_action = QtWidgets.QAction('Exit', self)

        exit_action.triggered.connect(self.close)

        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

    def display_page(self, index):
        self.pages.setCurrentIndex(index)

def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
