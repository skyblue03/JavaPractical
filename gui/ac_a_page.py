from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from calculations.accommodation import calculate_ac_a_ratio

class ACAPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.ipd_label = QLabel('IPD (cm):')
        self.ipd_input = QLineEdit()
        self.near_dev_label = QLabel('Near Deviation:')
        self.near_dev_input = QLineEdit()
        self.dist_dev_label = QLabel('Distance Deviation:')
        self.dist_dev_input = QLineEdit()
        self.calc_button = QPushButton('Calculate AC/A Ratio')
        self.result_label = QLabel('Result:')
        self.result_display = QLabel('')

        layout.addWidget(self.ipd_label)
        layout.addWidget(self.ipd_input)
        layout.addWidget(self.near_dev_label)
        layout.addWidget(self.near_dev_input)
        layout.addWidget(self.dist_dev_label)
        layout.addWidget(self.dist_dev_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

        self.calc_button.clicked.connect(self.calculate_ac_a_ratio)

    def calculate_ac_a_ratio(self):
        ipd = float(self.ipd_input.text())
        near_dev = float(self.near_dev_input.text())
        dist_dev = float(self.dist_dev_input.text())
        ratio = calculate_ac_a_ratio(ipd, near_dev, dist_dev)
        self.result_display.setText(f'{ratio:.2f}')
