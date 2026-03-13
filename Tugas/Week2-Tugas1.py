import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout,
    QFormLayout, QMessageBox
)
from PySide6.QtCore import Qt


class FormBiodata(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedSize(350, 420)

        main_layout = QVBoxLayout()

        # ===== Form Layout =====
        form_layout = QFormLayout()

        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan nama lengkap")

        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")

        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: TI-2A")

        self.combo_gender = QComboBox()
        self.combo_gender.addItems([
            "-- Pilih Jenis Kelamin --",
            "Laki-laki",
            "Perempuan"
        ])

        form_layout.addRow("Nama Lengkap:", self.input_nama)
        form_layout.addRow("NIM:", self.input_nim)
        form_layout.addRow("Kelas:", self.input_kelas)
        form_layout.addRow("Jenis Kelamin:", self.combo_gender)

        # ===== Tombol =====
        btn_layout = QHBoxLayout()

        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")

        self.btn_tampil.setStyleSheet(
            "background:#3498db; color:white; padding:8px; border-radius:4px;"
        )

        self.btn_reset.setStyleSheet(
            "background:#7f8c8d; color:white; padding:8px; border-radius:4px;"
        )

        btn_layout.addWidget(self.btn_tampil)
        btn_layout.addWidget(self.btn_reset)

        # ===== Label hasil =====
        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)
        self.label_hasil.setStyleSheet("""
        padding:12px;
        background:#27ae60;
        border-left:4px solid #d5f4e6;
        border-radius:4px;
        """)

        # ===== Layout utama =====
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.label_hasil)

        self.setLayout(main_layout)

        # ===== Connect tombol =====
        self.btn_tampil.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_form)

    def tampilkan_data(self):

        nama = self.input_nama.text().strip()
        nim = self.input_nim.text().strip()
        kelas = self.input_kelas.text().strip()
        gender = self.combo_gender.currentText()

        # ===== Validasi =====
        if not nama or not nim or not kelas:
            QMessageBox.warning(self, "Error", "Semua field harus diisi!")
            return

        if gender == "-- Pilih Jenis Kelamin --":
            QMessageBox.warning(self, "Error", "Pilih jenis kelamin!")
            return

        # ===== Tampilkan hasil =====
        hasil = f"""
DATA BIODATA

Nama: {nama}
NIM: {nim}
Kelas: {kelas}
Jenis Kelamin: {gender}
"""

        self.label_hasil.setText(hasil)

    def reset_form(self):

        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_gender.setCurrentIndex(0)
        self.label_hasil.clear()


app = QApplication(sys.argv)
window = FormBiodata()
window.show()
sys.exit(app.exec())