# tugas_form.py
# Form Registrasi Mahasiswa
# Nama: ____________
# NIM: _____________

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QComboBox, QCheckBox, QVBoxLayout,
    QHBoxLayout, QFormLayout, QMessageBox
)
from PySide6.QtCore import Qt


class FormRegistrasi(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Form Registrasi Mahasiswa")
        self.setFixedSize(450, 450)

        main_layout = QVBoxLayout()

        # Judul
        judul = QLabel("FORM REGISTRASI")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet(
            "font-size: 18px; font-weight: bold; padding: 15px; background: #9b59b6; color: white; border-radius: 5px;"
        )

        # Form Layout
        form_layout = QFormLayout()

        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan nama lengkap")
        form_layout.addRow("Nama:", self.input_nama)

        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
        form_layout.addRow("NIM:", self.input_nim)

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Masukkan email")
        form_layout.addRow("Email:", self.input_email)

        self.combo_prodi = QComboBox()
        self.combo_prodi.addItems([
            "-- Pilih Prodi --",
            "Teknik Informatika",
            "Sistem Informasi",
            "Teknik Komputer"
        ])
        form_layout.addRow("Prodi:", self.combo_prodi)

        # Checkbox
        self.checkbox = QCheckBox("Saya setuju dengan syarat dan ketentuan")

        # Tombol
        btn_layout = QHBoxLayout()

        self.btn_submit = QPushButton("Submit")
        self.btn_submit.setStyleSheet(
            "padding: 10px; background: #27ae60; color: white; border: none; border-radius: 5px;"
        )
        self.btn_submit.clicked.connect(self.submit)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet(
            "padding: 10px; background: #95a5a6; color: white; border: none; border-radius: 5px;"
        )
        self.btn_reset.clicked.connect(self.reset)

        btn_layout.addWidget(self.btn_submit)
        btn_layout.addWidget(self.btn_reset)

        # Label hasil
        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)
        self.label_hasil.setStyleSheet("padding: 15px; font-size: 12px;")

        # Assembly
        main_layout.addWidget(judul)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.checkbox)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.label_hasil)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def submit(self):
        nama = self.input_nama.text().strip()
        nim = self.input_nim.text().strip()
        email = self.input_email.text().strip()
        prodi = self.combo_prodi.currentText()

        # Validasi checkbox
        if not self.checkbox.isChecked():
            QMessageBox.warning(self, "Error", "Centang persetujuan!")
            return

        # Validasi field kosong
        if not nama or not nim or not email:
            QMessageBox.warning(self, "Error", "Semua field harus diisi!")
            return

        # Validasi prodi
        if prodi == "-- Pilih Prodi --":
            QMessageBox.warning(self, "Error", "Pilih program studi!")
            return

        # Tampilkan hasil
        self.label_hasil.setText(
            f"Data Tersimpan:\n\nNama: {nama}\nNIM: {nim}\nEmail: {email}\nProdi: {prodi}"
        )

        self.label_hasil.setStyleSheet(
            "padding: 15px; background: #d5f4e6; border-left: 4px solid #27ae60;"
        )

    def reset(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_email.clear()
        self.combo_prodi.setCurrentIndex(0)
        self.checkbox.setChecked(False)
        self.label_hasil.clear()


app = QApplication(sys.argv)
window = FormRegistrasi()
window.show()
sys.exit(app.exec())