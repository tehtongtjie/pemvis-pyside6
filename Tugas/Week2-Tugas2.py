import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt


class KonversiSuhu(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Konversi Suhu")
        self.setFixedSize(350, 320)

        layout = QVBoxLayout()

        # ===== Judul =====
        judul = QLabel("KONVERSI SUHU")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        padding:10px;
        background:#3498db;
        color:white;
        border-radius:5px;
        """)

        # ===== Label Input =====
        label_input = QLabel("Masukkan Suhu (Celsius):")

        # ===== Input =====
        self.input_suhu = QLineEdit()
        self.input_suhu.setPlaceholderText("Masukkan nilai suhu...")
        self.input_suhu.setStyleSheet("""
        padding:8px;
        font-size:14px;
        border:2px solid #2ecc71;
        border-radius:4px;
        """)

        # ===== Tombol =====
        btn_layout = QHBoxLayout()

        self.btn_f = QPushButton("Fahrenheit")
        self.btn_k = QPushButton("Kelvin")
        self.btn_r = QPushButton("Reamur")

        btn_style = """
        padding:8px;
        background:#2980b9;
        color:white;
        border:none;
        border-radius:5px;
        """

        for btn in [self.btn_f, self.btn_k, self.btn_r]:
            btn.setStyleSheet(btn_style)

        btn_layout.addWidget(self.btn_f)
        btn_layout.addWidget(self.btn_k)
        btn_layout.addWidget(self.btn_r)

        # ===== Label Hasil =====
        self.label_hasil = QLabel("Hasil Konversi:")
        self.label_hasil.setStyleSheet("""
        padding:10px;
        background:#1B4F72;
        border-radius:5px;
        """)

        # ===== Layout =====
        layout.addWidget(judul)
        layout.addWidget(label_input)
        layout.addWidget(self.input_suhu)
        layout.addLayout(btn_layout)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

        # ===== Connect =====
        self.btn_f.clicked.connect(self.ke_fahrenheit)
        self.btn_k.clicked.connect(self.ke_kelvin)
        self.btn_r.clicked.connect(self.ke_reamur)

    # ===== Ambil Input =====
    def get_input(self):
        try:
            c = float(self.input_suhu.text())
            return c
        except:
            QMessageBox.warning(self, "Error", "Input harus berupa angka!")
            return None

    # ===== Konversi Fahrenheit =====
    def ke_fahrenheit(self):
        c = self.get_input()
        if c is not None:
            f = (c * 9/5) + 32
            self.label_hasil.setText(
                f"Hasil Konversi:\n\n{c} Celsius = {f:.2f} Fahrenheit"
            )

    # ===== Konversi Kelvin =====
    def ke_kelvin(self):
        c = self.get_input()
        if c is not None:
            k = c + 273.15
            self.label_hasil.setText(
                f"Hasil Konversi:\n\n{c} Celsius = {k:.2f} Kelvin"
            )

    # ===== Konversi Reamur =====
    def ke_reamur(self):
        c = self.get_input()
        if c is not None:
            r = c * 4/5
            self.label_hasil.setText(
                f"Hasil Konversi:\n\n{c} Celsius = {r:.2f} Reamur"
            )


app = QApplication(sys.argv)
window = KonversiSuhu()
window.show()
sys.exit(app.exec())