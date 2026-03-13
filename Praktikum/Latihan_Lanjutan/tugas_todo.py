# tugas_todo.py
# To-Do List Manager
# Nama: ___________
# NIM: ____________

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QListWidget, QVBoxLayout, QHBoxLayout,
    QMessageBox
)
from PySide6.QtCore import Qt


class TodoApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("To-Do List")
        self.resize(400, 500)

        layout = QVBoxLayout()

        # Judul
        judul = QLabel("MY TO-DO LIST")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet(
            "font-size:18px; font-weight:bold; padding:10px; background:#8e44ad; color:white; border-radius:5px;"
        )

        # Input tugas
        input_layout = QHBoxLayout()

        self.input_tugas = QLineEdit()
        self.input_tugas.setPlaceholderText("Masukkan tugas baru...")
        self.input_tugas.setStyleSheet("padding:8px; font-size:14px;")

        self.btn_tambah = QPushButton("Tambah")
        self.btn_tambah.setStyleSheet(
            "padding:8px 15px; background:#27ae60; color:white; border:none; border-radius:5px;"
        )

        self.btn_tambah.clicked.connect(self.tambah_tugas)

        input_layout.addWidget(self.input_tugas)
        input_layout.addWidget(self.btn_tambah)

        # List widget
        self.list_tugas = QListWidget()
        self.list_tugas.setStyleSheet("font-size:14px; padding:5px;")

        # Tombol aksi
        btn_layout = QHBoxLayout()

        self.btn_hapus = QPushButton("Hapus")
        self.btn_hapus.setStyleSheet(
            "padding:8px; background:#e74c3c; color:white; border:none; border-radius:5px;"
        )
        self.btn_hapus.clicked.connect(self.hapus_tugas)

        self.btn_clear = QPushButton("Hapus Semua")
        self.btn_clear.setStyleSheet(
            "padding:8px; background:#f39c12; color:white; border:none; border-radius:5px;"
        )
        self.btn_clear.clicked.connect(self.clear_semua)

        btn_layout.addWidget(self.btn_hapus)
        btn_layout.addWidget(self.btn_clear)

        # Label status
        self.label_status = QLabel("Total tugas: 0")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_status.setStyleSheet(
            "padding:10px; background:#ecf0f1; border-radius:5px;"
        )

        # Layout
        layout.addWidget(judul)
        layout.addLayout(input_layout)
        layout.addWidget(self.list_tugas)
        layout.addLayout(btn_layout)
        layout.addWidget(self.label_status)

        self.setLayout(layout)

    def tambah_tugas(self):
        tugas = self.input_tugas.text().strip()

        if tugas:
            self.list_tugas.addItem(tugas)
            self.input_tugas.clear()
            self.update_status()
        else:
            QMessageBox.warning(self, "Error", "Tugas tidak boleh kosong!")

    def hapus_tugas(self):
        current = self.list_tugas.currentRow()

        if current >= 0:
            self.list_tugas.takeItem(current)
            self.update_status()
        else:
            QMessageBox.warning(self, "Error", "Pilih tugas yang ingin dihapus!")

    def clear_semua(self):
        self.list_tugas.clear()
        self.update_status()

    def update_status(self):
        total = self.list_tugas.count()
        self.label_status.setText(f"Total tugas: {total}")


app = QApplication(sys.argv)
window = TodoApp()
window.show()
sys.exit(app.exec())