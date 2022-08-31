from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from calculations.lens_calculations import radius_of_curvature_to_power

class RadiusPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.radius_label = QLabel('Radius of Curvature:')
        self.radius_input = QLineEdit()
        self.calc_button = QPushButton('Calculate Power')
        self.result_label = QLabel('Result:')
        self.result_display = QLabel('')

        layout.addWidget(self.radius_label)
        layout.addWidget(self.radius_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

        self.calc_button.clicked.connect(self.calculate_power)

    def calculate_power(self):
        radius = float(self.radius_input.text())
        power = radius_of_curvature_to_power(radius)
        self.result_display.setText(f'{power:.2f}')
