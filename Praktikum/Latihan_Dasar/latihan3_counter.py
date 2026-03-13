# latihan3_counter.py
# Latihan 3: Counter Menghitung Klik

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt


class CounterApp(QWidget):
    def __init__(self):
        super().__init__()

        # Variabel untuk menyimpan counter
        self.counter = 0

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Counter Klik")
        self.resize(300, 250)

        # Label untuk menampilkan counter
        self.label_counter = QLabel(f"Counter: {self.counter}")
        self.label_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_counter.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            padding: 20px;
            background-color: #000000;
            border-radius: 10px;
        """)

        # Tombol tambah
        self.tombol_tambah = QPushButton("Tambah")
        self.tombol_tambah.setStyleSheet("""
            padding: 15px;
            font-size: 16px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
        """)

        # Hubungkan tombol ke fungsi
        self.tombol_tambah.clicked.connect(self.tambah_counter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_counter)
        layout.addWidget(self.tombol_tambah)

        self.setLayout(layout)

    def tambah_counter(self):
        self.counter += 1
        self.label_counter.setText(f"Counter: {self.counter}")


app = QApplication(sys.argv)
window = CounterApp()
window.show()
sys.exit(app.exec())