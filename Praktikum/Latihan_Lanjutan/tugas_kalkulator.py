# tugas_kalkulator.py
# Kalkulator Lengkap dengan 4 Operasi
# Nama: Lalu Rifqi Ramadhan
# NIM: F1D02310071

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt


class KalkulatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Kalkulator Lengkap")
        self.setFixedSize(400, 350)

        layout = QVBoxLayout()

        # Judul
        judul = QLabel("KALKULATOR")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("font-size: 20px; font-weight: bold; padding: 15px; background: #34495e; color: white; border-radius: 5px;")

        # Input fields
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Angka pertama")
        self.input1.setStyleSheet("padding: 12px; font-size: 16px;")

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Angka kedua")
        self.input2.setStyleSheet("padding: 12px; font-size: 16px;")

        # Tombol operasi
        btn_layout = QHBoxLayout()

        self.btn_tambah = QPushButton("+")
        self.btn_kurang = QPushButton("-")
        self.btn_kali = QPushButton("x")
        self.btn_bagi = QPushButton("/")

        btn_style = "padding: 15px; font-size: 20px; font-weight: bold; background: #3498db; color: white; border: none; border-radius: 5px;"

        for btn in [self.btn_tambah, self.btn_kurang, self.btn_kali, self.btn_bagi]:
            btn.setStyleSheet(btn_style)
            btn_layout.addWidget(btn)

        # Connect signals
        self.btn_tambah.clicked.connect(self.hitung_tambah)
        self.btn_kurang.clicked.connect(self.hitung_kurang)
        self.btn_kali.clicked.connect(self.hitung_kali)
        self.btn_bagi.clicked.connect(self.hitung_bagi)

        # Label hasil
        self.label_hasil = QLabel("Hasil: -")
        self.label_hasil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_hasil.setStyleSheet("font-size: 24px; font-weight: bold; padding: 20px; background: #ecf0f1; border-radius: 5px;")

        # Assembly
        layout.addWidget(judul)
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addLayout(btn_layout)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    def get_numbers(self):
        try:
            a = float(self.input1.text())
            b = float(self.input2.text())
            return a, b
        except ValueError:
            QMessageBox.warning(self, "Error", "Input harus angka!")
            return None

    def tampil_hasil(self, hasil):
        self.label_hasil.setText(f"Hasil: {hasil}")
        self.label_hasil.setStyleSheet("font-size: 24px; font-weight: bold; padding: 20px; background: #2ecc71; color: white; border-radius: 5px;")

    def hitung_tambah(self):
        nums = self.get_numbers()
        if nums:
            self.tampil_hasil(nums[0] + nums[1])

    def hitung_kurang(self):
        nums = self.get_numbers()
        if nums:
            self.tampil_hasil(nums[0] - nums[1])

    def hitung_kali(self):
        nums = self.get_numbers()
        if nums:
            self.tampil_hasil(nums[0] * nums[1])

    def hitung_bagi(self):
        nums = self.get_numbers()
        if nums:
            if nums[1] == 0:
                QMessageBox.warning(self, "Error", "Tidak bisa bagi dengan nol!")
            else:
                self.tampil_hasil(nums[0] / nums[1])


app = QApplication(sys.argv)
window = KalkulatorApp()
window.show()
sys.exit(app.exec())