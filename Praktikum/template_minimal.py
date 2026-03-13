import sys
from PySide6.QtWidgets import QApplication, QWidget

# membuat aplikasi Qt
app = QApplication(sys.argv)

# membuat window
window = QWidget()
window.setWindowTitle("Jendela Pertama")
window.resize(400, 200)

# menampilkan window
window.show()

# menjalankan aplikasi
sys.exit(app.exec())