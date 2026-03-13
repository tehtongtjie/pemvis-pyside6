# template_class.py
# Template dengan struktur class (OOP)

import sys
from PySide6.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Konfigurasi jendela
        self.setWindowTitle("Aplikasi OOP")
        self.resize(500, 400)

def main():
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())

# Jalankan program
if __name__ == "__main__":
    main()