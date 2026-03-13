import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout, QCheckBox
)
from PySide6.QtCore import Qt


class LoginApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Login")
        self.setFixedSize(300, 330)

        layout = QVBoxLayout()

        # ===== Judul =====
        judul = QLabel("LOGIN")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("""
        background:#9b59b6;
        color:white;
        font-size:16px;
        font-weight:bold;
        padding:10px;
        border-radius:5px;
        """)

        # ===== Username =====
        label_user = QLabel("Username:")
        self.input_user = QLineEdit()

        # ===== Password =====
        label_pass = QLabel("Password:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)

        # ===== Checkbox tampilkan password =====
        self.checkbox = QCheckBox("Tampilkan Password")
        self.checkbox.stateChanged.connect(self.toggle_password)

        # ===== Tombol =====
        btn_layout = QHBoxLayout()

        self.btn_login = QPushButton("Login")
        self.btn_reset = QPushButton("Reset")

        self.btn_login.setStyleSheet(
            "background:#27ae60; color:white; padding:6px; border-radius:4px;"
        )

        self.btn_reset.setStyleSheet(
            "background:#7f8c8d; color:white; padding:6px; border-radius:4px;"
        )

        btn_layout.addWidget(self.btn_login)
        btn_layout.addWidget(self.btn_reset)

        # ===== Label hasil =====
        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)

        # ===== Layout =====
        layout.addWidget(judul)
        layout.addWidget(label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(label_pass)
        layout.addWidget(self.input_pass)
        layout.addWidget(self.checkbox)
        layout.addLayout(btn_layout)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

        # ===== Connect tombol =====
        self.btn_login.clicked.connect(self.login)
        self.btn_reset.clicked.connect(self.reset_form)

    # ===== Toggle password =====
    def toggle_password(self):

        if self.checkbox.isChecked():
            self.input_pass.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)

    # ===== Login =====
    def login(self):

        username = self.input_user.text()
        password = self.input_pass.text()

        if username == "admin" and password == "12345":

            self.input_user.setStyleSheet("border:2px solid green;")
            self.input_pass.setStyleSheet("border:2px solid green;")

            self.label_hasil.setText("Login berhasil! Selamat datang, admin.")
            self.label_hasil.setStyleSheet("""
            padding:10px;
            background:#d5f4e6;
            border-left:4px solid #27ae60;
            """)

        else:

            self.input_user.setStyleSheet("border:2px solid red;")
            self.input_pass.setStyleSheet("border:2px solid red;")

            self.label_hasil.setText("Login gagal! Username atau password salah.")
            self.label_hasil.setStyleSheet("""
            padding:10px;
            background:#f5b7b1;
            border-left:4px solid #c0392b;
            """)

    # ===== Reset =====
    def reset_form(self):

        self.input_user.clear()
        self.input_pass.clear()

        self.input_user.setStyleSheet("")
        self.input_pass.setStyleSheet("")

        self.checkbox.setChecked(False)

        self.label_hasil.clear()


app = QApplication(sys.argv)
window = LoginApp()
window.show()
sys.exit(app.exec())