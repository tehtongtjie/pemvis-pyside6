# latihan2_tombol.py
# Latihan 2: Tombol Klik dengan Signal-Slot

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt


class AplikasiTombol(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Aplikasi Tombol")
        self.resize(300, 200)

        # Buat Label
        self.label = QLabel("Belum diklik")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; padding: 20px;")

        # Buat tombol
        self.tombol = QPushButton("Klik Saya!")
        self.tombol.setStyleSheet("padding: 10px; font-size: 14px;")

        # Hubungkan tombol ke fungsi
        self.tombol.clicked.connect(self.tombol_diklik)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.tombol)

        self.setLayout(layout)

    def tombol_diklik(self):
        self.label.setText("Tombol sudah diklik!")


app = QApplication(sys.argv)
window = AplikasiTombol()
window.show()
sys.exit(app.exec())