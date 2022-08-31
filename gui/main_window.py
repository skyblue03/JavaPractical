from PyQt5 import QtWidgets
from calculations.lens_calculations import radius_of_curvature_to_power, focal_power
from calculations.prismatic_effect import prismatic_effect_power

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Optometrist Calculator')
        self.setGeometry(100, 100, 800, 600)

        self.radius_label = QtWidgets.QLabel('Radius of Curvature:', self)
        self.radius_label.move(50, 50)
        self.radius_input = QtWidgets.QLineEdit(self)
        self.radius_input.move(200, 50)

        self.calc_button = QtWidgets.QPushButton('Calculate Power', self)
        self.calc_button.move(200, 100)
        self.calc_button.clicked.connect(self.calculate_power)

        self.result_label = QtWidgets.QLabel('Result:', self)
        self.result_label.move(50, 150)
        self.result_display = QtWidgets.QLabel('', self)
        self.result_display.move(200, 150)

    def calculate_power(self):
        radius = float(self.radius_input.text())
        power = radius_of_curvature_to_power(radius)
        self.result_display.setText(f'{power:.2f}')

def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
