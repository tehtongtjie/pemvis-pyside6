# latihan5_kalkulator.py
# Latihan 5: Kalkulator Mini Plus Minus

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt


class KalkulatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Kalkulator Mini")
        self.resize(350, 400)

        layout = QVBoxLayout()

        # Judul
        judul = QLabel("Kalkulator Mini")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet(
            "font-size: 18px; font-weight: bold; padding: 10px; "
            "background: #1abc9c; color: white; border-radius: 5px;"
        )

        # Input angka pertama
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Angka pertama")
        self.input1.setStyleSheet("padding: 10px; font-size: 14px;")

        # Input angka kedua
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Angka kedua")
        self.input2.setStyleSheet("padding: 10px; font-size: 14px;")

        # Layout tombol
        tombol_layout = QHBoxLayout()

        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")

        # Style tombol
        for btn in [self.btn_plus, self.btn_minus]:
            btn.setStyleSheet("""
                padding: 15px;
                font-size: 18px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
            """)

        tombol_layout.addWidget(self.btn_plus)
        tombol_layout.addWidget(self.btn_minus)

        # Hubungkan tombol ke fungsi
        self.btn_plus.clicked.connect(self.hitung_plus)
        self.btn_minus.clicked.connect(self.hitung_minus)

        # Label hasil
        self.label_hasil = QLabel("Hasil: -")
        self.label_hasil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_hasil.setStyleSheet(
            "font-size: 20px; padding: 20px; background: #ecf0f1; border-radius: 5px;"
        )

        # Masukkan ke layout
        layout.addWidget(judul)
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addLayout(tombol_layout)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    def hitung_plus(self):
        try:
            a = float(self.input1.text())
            b = float(self.input2.text())
            hasil = a + b

            self.label_hasil.setText(f"Hasil: {hasil}")
            self.label_hasil.setStyleSheet(
                "font-size: 20px; padding: 20px; background: #2ecc71; color: white; border-radius: 5px;"
            )

        except:
            self.label_hasil.setText("Error: Input harus angka!")
            self.label_hasil.setStyleSheet(
                "font-size: 20px; padding: 20px; background: #e74c3c; color: white; border-radius: 5px;"
            )

    def hitung_minus(self):
        try:
            a = float(self.input1.text())
            b = float(self.input2.text())
            hasil = a - b

            self.label_hasil.setText(f"Hasil: {hasil}")
            self.label_hasil.setStyleSheet(
                "font-size: 20px; padding: 20px; background: #2ecc71; color: white; border-radius: 5px;"
            )

        except:
            self.label_hasil.setText("Error: Input harus angka!")
            self.label_hasil.setStyleSheet(
                "font-size: 20px; padding: 20px; background: #e74c3c; color: white; border-radius: 5px;"
            )


app = QApplication(sys.argv)
window = KalkulatorApp()
window.show()
sys.exit(app.exec())