from PyQt5 import QtWidgets
from calculations.lens_calculations import radius_of_curvature_to_power, focal_power
from calculations.prismatic_effect import prismatic_effect_power
from calculations.accommodation import calculate_ac_a_ratio
from calculations.astigmatism import astigmatism_fan_block_test, calculate_cylinder_power

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Optometrist Calculator')
        self.setGeometry(100, 100, 800, 600)

        self.init_radius_section()
        self.init_ac_a_section()
        self.init_astigmatism_section()

    def init_radius_section(self):
        self.radius_label = QtWidgets.QLabel('Radius of Curvature:', self)
        self.radius_label.move(50, 50)
        self.radius_input = QtWidgets.QLineEdit(self)
        self.radius_input.move(200, 50)

        self.calc_radius_button = QtWidgets.QPushButton('Calculate Power', self)
        self.calc_radius_button.move(200, 100)
        self.calc_radius_button.clicked.connect(self.calculate_radius_power)

        self.radius_result_label = QtWidgets.QLabel('Result:', self)
        self.radius_result_label.move(50, 150)
        self.radius_result_display = QtWidgets.QLabel('', self)
        self.radius_result_display.move(200, 150)

    def init_ac_a_section(self):
        self.ac_a_ipd_label = QtWidgets.QLabel('IPD (cm):', self)
        self.ac_a_ipd_label.move(50, 200)
        self.ac_a_ipd_input = QtWidgets.QLineEdit(self)
        self.ac_a_ipd_input.move(200, 200)

        self.ac_a_near_dev_label = QtWidgets.QLabel('Near Deviation:', self)
        self.ac_a_near_dev_label.move(50, 250)
        self.ac_a_near_dev_input = QtWidgets.QLineEdit(self)
        self.ac_a_near_dev_input.move(200, 250)

        self.ac_a_dist_dev_label = QtWidgets.QLabel('Distance Deviation:', self)
        self.ac_a_dist_dev_label.move(50, 300)
        self.ac_a_dist_dev_input = QtWidgets.QLineEdit(self)
        self.ac_a_dist_dev_input.move(200, 300)

        self.calc_ac_a_button = QtWidgets.QPushButton('Calculate AC/A Ratio', self)
        self.calc_ac_a_button.move(200, 350)
        self.calc_ac_a_button.clicked.connect(self.calculate_ac_a_ratio)

        self.ac_a_result_label = QtWidgets.QLabel('Result:', self)
        self.ac_a_result_label.move(50, 400)
        self.ac_a_result_display = QtWidgets.QLabel('', self)
        self.ac_a_result_display.move(200, 400)

    def init_astigmatism_section(self):
        self.astig_best_sphere_label = QtWidgets.QLabel('Best Sphere:', self)
        self.astig_best_sphere_label.move(50, 450)
        self.astig_best_sphere_input = QtWidgets.QLineEdit(self)
        self.astig_best_sphere_input.move(200, 450)

        self.astig_cyl_power_label = QtWidgets.QLabel('Approx Cylinder Power:', self)
        self.astig_cyl_power_label.move(50, 500)
        self.astig_cyl_power_input = QtWidgets.QLineEdit(self)
        self.astig_cyl_power_input.move(200, 500)

        self.calc_astig_button = QtWidgets.QPushButton('Calculate Astigmatism', self)
        self.calc_astig_button.move(200, 550)
        self.calc_astig_button.clicked.connect(self.calculate_astigmatism)

        self.astig_result_label = QtWidgets.QLabel('Result:', self)
        self.astig_result_label.move(50, 600)
        self.astig_result_display = QtWidgets.QLabel('', self)
        self.astig_result_display.move(200, 600)

    def calculate_radius_power(self):
        radius = float(self.radius_input.text())
        power = radius_of_curvature_to_power(radius)
        self.radius_result_display.setText(f'{power:.2f}')

    def calculate_ac_a_ratio(self):
        ipd = float(self.ac_a_ipd_input.text())
        near_dev = float(self.ac_a_near_dev_input.text())
        dist_dev = float(self.ac_a_dist_dev_input.text())
        ratio = calculate_ac_a_ratio(ipd, near_dev, dist_dev)
        self.ac_a_result_display.setText(f'{ratio:.2f}')

    def calculate_astigmatism(self):
        best_sphere = float(self.astig_best_sphere_input.text())
        cyl_power = float(self.astig_cyl_power_input.text())
        result = astigmatism_fan_block_test(best_sphere, cyl_power, 1.0)  # Visual acuity can be another input
        self.astig_result_display.setText(f'{result:.2f}')

def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
