from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

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

    def calculate_power(self):
        radius = float(self.radius_input.text())
        power = 337.5 / radius
        self.result_display.setText(f'{power:.2f}')
