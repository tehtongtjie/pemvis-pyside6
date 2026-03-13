# latihan4_input.py
# Latihan 4: Input Nama dengan Validasi

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QVBoxLayout
)
from PySide6.QtCore import Qt


class InputNamaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Input Nama")
        self.resize(400, 300)

        # Label instruksi
        label_instruksi = QLabel("Masukkan nama Anda:")
        label_instruksi.setStyleSheet("font-size: 14px; font-weight: bold;")

        # Input nama
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Ketik nama di sini...")
        self.input_nama.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
        """)

        # Tombol sapa
        self.tombol_sapa = QPushButton("Sapa!")
        self.tombol_sapa.setStyleSheet("""
            padding: 12px;
            font-size: 14px;
            background-color: #2ecc71;
            color: white;
            border: none;
            border-radius: 5px;
        """)

        self.tombol_sapa.clicked.connect(self.sapa)

        # Label hasil
        self.label_hasil = QLabel("")
        self.label_hasil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_hasil.setStyleSheet("font-size: 16px; padding: 15px;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label_instruksi)
        layout.addWidget(self.input_nama)
        layout.addWidget(self.tombol_sapa)
        layout.addWidget(self.label_hasil)
        layout.addStretch()

        self.setLayout(layout)

    def sapa(self):
        # Ambil teks dari input dan hapus spasi di awal/akhir
        nama = self.input_nama.text().strip()

        # Validasi jika input kosong
        if nama == "":
            self.label_hasil.setText("Nama tidak boleh kosong!")
            self.label_hasil.setStyleSheet("color: red; font-size: 16px; padding: 15px;")
        else:
            self.label_hasil.setText(f"Halo, {nama}! Selamat datang!")
            self.label_hasil.setStyleSheet("color: green; font-size: 16px; padding: 15px;")


app = QApplication(sys.argv)
window = InputNamaApp()
window.show()
sys.exit(app.exec())