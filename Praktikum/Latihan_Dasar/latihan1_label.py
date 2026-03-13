# latihan1_label.py
# Latihan 1: Jendela dengan Label

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout
)
from PySide6.QtCore import Qt


class JendelaPesan(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Pesan Sambutan")
        self.resize(400, 200)

        # Buat label
        label = QLabel("Selamat Datang di KinkQQ!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 20px; font-weight: bold;")

        # Buat layout dan tambahkan label
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


# Program utama
app = QApplication(sys.argv)
window = JendelaPesan()
window.show()
sys.exit(app.exec())