from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from calculations.astigmatism import astigmatism_fan_block_test

class AstigmatismPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.best_sphere_label = QLabel('Best Sphere:')
        self.best_sphere_input = QLineEdit()
        self.cyl_power_label = QLabel('Approx Cylinder Power:')
        self.cyl_power_input = QLineEdit()
        self.calc_button = QPushButton('Calculate Astigmatism')
        self.result_label = QLabel('Result:')
        self.result_display = QLabel('')

        layout.addWidget(self.best_sphere_label)
        layout.addWidget(self.best_sphere_input)
        layout.addWidget(self.cyl_power_label)
        layout.addWidget(self.cyl_power_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

        self.calc_button.clicked.connect(self.calculate_astigmatism)

        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                padding: 5px;
                font-size: 14px;
                border: 1px solid #4a4a4a;
            }
            QPushButton {
                padding: 10px;
                font-size: 14px;
                background-color: #4a4a4a;
                color: #ffffff;
                border: none;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
            }
        """)

    def calculate_astigmatism(self):
        best_sphere = float(self.best_sphere_input.text())
        cyl_power = float(self.cyl_power_input.text())
        result = astigmatism_fan_block_test(best_sphere, cyl_power)
        self.result_display.setText(f'{result:.2f}')
