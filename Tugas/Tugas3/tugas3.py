import sys
import json
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QLabel, QLineEdit,
    QComboBox, QDialog, QFormLayout, QDateEdit, QMessageBox,
    QToolBar, QStatusBar, QHeaderView, QAbstractItemView,
)
from PyQt6.QtGui import QColor, QAction, QBrush  # Ditambahkan QBrush
from PyQt6.QtCore import Qt, QDate, QSize

DATA_FILE = "tasks.json"

# DIPERBAIKI: Menggunakan warna latar belakang gelap agar teks (#cdd6f4) tetap terbaca
PRIORITY_COLORS = {
    "High":   {"bg": QColor("#542935")},  # Merah gelap
    "Medium": {"bg": QColor("#544829")},  # Kuning kecoklatan gelap
    "Low":    {"bg": QColor("#295438")},  # Hijau gelap
}

STATUS_OPTIONS   = ["Todo", "In Progress", "Done"]
PRIORITY_OPTIONS = ["High", "Medium", "Low"]
FILTER_OPTIONS   = ["Semua"] + PRIORITY_OPTIONS + STATUS_OPTIONS


class TaskDialog(QDialog):
    def __init__(self, parent=None, task=None):
        super().__init__(parent)
        self.setWindowTitle("Add Task" if task is None else "Edit Task")
        self.setMinimumWidth(400)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        title_label = QLabel("Add Task" if task is None else "Edit Task")
        title_label.setObjectName("dialogTitle")
        layout.addWidget(title_label)

        form = QFormLayout()
        form.setSpacing(12)
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        self.judul_edit = QLineEdit()
        self.judul_edit.setPlaceholderText("Masukkan judul task...")
        form.addRow("Judul Task:", self.judul_edit)

        self.prioritas_combo = QComboBox()
        self.prioritas_combo.addItems(PRIORITY_OPTIONS)
        form.addRow("Prioritas:", self.prioritas_combo)

        self.status_combo = QComboBox()
        self.status_combo.addItems(STATUS_OPTIONS)
        form.addRow("Status:", self.status_combo)

        self.due_date_edit = QDateEdit()
        self.due_date_edit.setCalendarPopup(True)
        self.due_date_edit.setDate(QDate.currentDate())
        self.due_date_edit.setDisplayFormat("yyyy-MM-dd")
        form.addRow("Due Date:", self.due_date_edit)

        layout.addLayout(form)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        self.cancel_btn = QPushButton("Batal")
        self.cancel_btn.setObjectName("cancelBtn")
        self.cancel_btn.clicked.connect(self.reject)

        self.save_btn = QPushButton("Simpan")
        self.save_btn.setObjectName("saveBtn")
        self.save_btn.clicked.connect(self.validate_and_accept)

        btn_layout.addWidget(self.cancel_btn)
        btn_layout.addWidget(self.save_btn)
        layout.addLayout(btn_layout)

        if task:
            self.judul_edit.setText(task["judul"])
            idx_p = self.prioritas_combo.findText(task["prioritas"])
            self.prioritas_combo.setCurrentIndex(idx_p if idx_p >= 0 else 0)
            idx_s = self.status_combo.findText(task["status"])
            self.status_combo.setCurrentIndex(idx_s if idx_s >= 0 else 0)
            self.due_date_edit.setDate(QDate.fromString(task["due_date"], "yyyy-MM-dd"))

        self.setStyleSheet("""
            QDialog { background-color: #1e2533; }
            QLabel { color: #cdd6f4; font-size: 13px; }
            QLabel#dialogTitle {
                color: #89b4fa; font-size: 18px; font-weight: bold; padding-bottom: 4px;
            }
            QLineEdit, QComboBox, QDateEdit {
                background-color: #2a3146; color: #cdd6f4;
                border: 1px solid #45475a; border-radius: 6px;
                padding: 6px 10px; font-size: 13px; min-height: 30px;
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus { border: 1px solid #89b4fa; }
            QComboBox::drop-down { border: none; }
            QComboBox QAbstractItemView {
                background-color: #2a3146; color: #cdd6f4;
                selection-background-color: #45475a;
            }
            QPushButton#saveBtn {
                background-color: #89b4fa; color: #1e2533; border: none;
                border-radius: 6px; padding: 8px 22px; font-size: 13px; font-weight: bold;
            }
            QPushButton#saveBtn:hover { background-color: #74c7ec; }
            QPushButton#cancelBtn {
                background-color: #45475a; color: #cdd6f4; border: none;
                border-radius: 6px; padding: 8px 22px; font-size: 13px;
            }
            QPushButton#cancelBtn:hover { background-color: #585b70; }
        """)

    def validate_and_accept(self):
        if not self.judul_edit.text().strip():
            QMessageBox.warning(self, "Validasi", "Judul task tidak boleh kosong!")
            return
        self.accept()

    def get_task_data(self):
        return {
            "judul":     self.judul_edit.text().strip(),
            "prioritas": self.prioritas_combo.currentText(),
            "status":    self.status_combo.currentText(),
            "due_date":  self.due_date_edit.date().toString("yyyy-MM-dd"),
        }


class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setMinimumSize(960, 600)
        self.tasks = []
        self.load_tasks()
        self.init_ui()
        self.apply_styles()
        self.refresh_table()

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = [
                {"judul": "Buat laporan praktikum", "prioritas": "High",   "status": "In Progress", "due_date": "2026-04-01"},
                {"judul": "Review materi PySide6",  "prioritas": "Medium", "status": "Todo",        "due_date": "2026-04-05"},
                {"judul": "Push code ke GitHub",    "prioritas": "Low",    "status": "Done",        "due_date": "2026-03-30"},
            ]

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def init_ui(self):
        self._build_menubar()
        self._build_toolbar()
        self._build_central()
        self._build_statusbar()

    def _build_menubar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        save_action = QAction("Simpan", self)
        save_action.triggered.connect(self.save_tasks)
        exit_action = QAction("Keluar", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        task_menu = menubar.addMenu("Task")
        add_action = QAction("Tambah Task", self)
        add_action.triggered.connect(self.add_task)
        edit_action = QAction("Edit Task", self)
        edit_action.triggered.connect(self.edit_task)
        del_action = QAction("Hapus Task", self)
        del_action.triggered.connect(self.delete_task)
        task_menu.addAction(add_action)
        task_menu.addAction(edit_action)
        task_menu.addAction(del_action)

        help_menu = menubar.addMenu("Help")
        about_action = QAction("Tentang", self)
        about_action.triggered.connect(
            lambda: QMessageBox.information(self, "Tentang", "Task Manager v1.0\nDibuat dengan PyQt6")
        )
        help_menu.addAction(about_action)

    def _build_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        self.add_btn = QPushButton("＋ Add Task")
        self.add_btn.setObjectName("addBtn")
        self.add_btn.clicked.connect(self.add_task)

        self.edit_btn = QPushButton("✎  Edit")
        self.edit_btn.setObjectName("editBtn")
        self.edit_btn.clicked.connect(self.edit_task)

        self.del_btn = QPushButton("🗑 Delete")
        self.del_btn.setObjectName("delBtn")
        self.del_btn.clicked.connect(self.delete_task)

        filter_label = QLabel("  Filter:")
        filter_label.setObjectName("toolbarLabel")

        self.filter_combo = QComboBox()
        self.filter_combo.addItems(FILTER_OPTIONS)
        self.filter_combo.setFixedWidth(110)
        self.filter_combo.currentTextChanged.connect(self.refresh_table)

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("🔍 Cari task...")
        self.search_edit.setFixedWidth(180)
        self.search_edit.textChanged.connect(self.refresh_table)

        for w in [self.add_btn, self.edit_btn, self.del_btn, filter_label,
                  self.filter_combo, self.search_edit]:
            toolbar.addWidget(w)

    def _build_central(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(0)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["No", "Judul Task", "Prioritas", "Status", "Due Date"])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(2, 130)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 130)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(True)
        self.table.doubleClicked.connect(self.edit_task)

        layout.addWidget(self.table)

    def _build_statusbar(self):
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.status_label = QLabel()
        self.statusbar.addWidget(self.status_label)
        self.file_label = QLabel(DATA_FILE)
        self.file_label.setObjectName("fileLabel")
        self.statusbar.addPermanentWidget(self.file_label)

    def get_filtered_tasks(self):
        filt   = self.filter_combo.currentText()
        search = self.search_edit.text().strip().lower()
        result = []
        for t in self.tasks:
            if filt != "Semua":
                if filt not in (t["prioritas"], t["status"]):
                    continue
            if search and search not in t["judul"].lower():
                continue
            result.append(t)
        return result

    def refresh_table(self):
        tasks = self.get_filtered_tasks()
        self.table.setRowCount(len(tasks))

        for row, task in enumerate(tasks):
            pri  = task["prioritas"]
            stat = task["status"]
            bg   = PRIORITY_COLORS.get(pri, {}).get("bg", QColor(30, 37, 51)) # Fallback warna default tabel

            items = [
                QTableWidgetItem(str(row + 1)),
                QTableWidgetItem(task["judul"]),
                QTableWidgetItem(pri),
                QTableWidgetItem("Done ✓" if stat == "Done" else stat),
                QTableWidgetItem(task["due_date"]),
            ]

            for col, item in enumerate(items):
                # DIPERBAIKI: Menggunakan QBrush untuk setBackground
                item.setBackground(QBrush(bg))
                align = Qt.AlignmentFlag.AlignVCenter | (
                    Qt.AlignmentFlag.AlignCenter if col != 1 else Qt.AlignmentFlag.AlignLeft
                )
                item.setTextAlignment(align)
                self.table.setItem(row, col, item)

        self.update_status()

    def update_status(self):
        total   = len(self.tasks)
        done    = sum(1 for t in self.tasks if t["status"] == "Done")
        in_prog = sum(1 for t in self.tasks if t["status"] == "In Progress")
        todo    = sum(1 for t in self.tasks if t["status"] == "Todo")
        self.status_label.setText(
            f"Total: {total} tasks  |  Done: {done}  |  In Progress: {in_prog}  |  Todo: {todo}"
        )

    def add_task(self):
        dlg = TaskDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.tasks.append(dlg.get_task_data())
            self.save_tasks()
            self.refresh_table()

    def edit_task(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.information(self, "Info", "Pilih task yang ingin diedit terlebih dahulu.")
            return
        filtered  = self.get_filtered_tasks()
        task_data = filtered[row]
        orig_idx  = self.tasks.index(task_data)

        dlg = TaskDialog(self, task=task_data)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.tasks[orig_idx] = dlg.get_task_data()
            self.save_tasks()
            self.refresh_table()

    def delete_task(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.information(self, "Info", "Pilih task yang ingin dihapus terlebih dahulu.")
            return
        filtered  = self.get_filtered_tasks()
        task_data = filtered[row]
        judul     = task_data["judul"]

        reply = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus task:\n\"{judul}\"?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.tasks.remove(task_data)
            self.save_tasks()
            self.refresh_table()

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #181c27; color: #cdd6f4;
                font-family: 'Segoe UI', 'Ubuntu', sans-serif; font-size: 13px;
            }
            QMenuBar {
                background-color: #12161f; color: #cdd6f4;
                padding: 2px 4px; border-bottom: 1px solid #2a3146;
            }
            QMenuBar::item:selected { background-color: #2a3146; border-radius: 4px; }
            QMenu { background-color: #1e2533; color: #cdd6f4; border: 1px solid #2a3146; }
            QMenu::item:selected { background-color: #2a3146; }
            QToolBar {
                background-color: #12161f; border-bottom: 1px solid #2a3146;
                padding: 6px 10px; spacing: 8px;
            }
            QLabel#toolbarLabel { color: #a6adc8; }
            QPushButton#addBtn {
                background-color: #a6e3a1; color: #1e2533; border: none;
                border-radius: 6px; padding: 6px 16px; font-weight: bold;
            }
            QPushButton#addBtn:hover { background-color: #94d392; }
            QPushButton#editBtn {
                background-color: #89b4fa; color: #1e2533; border: none;
                border-radius: 6px; padding: 6px 16px; font-weight: bold;
            }
            QPushButton#editBtn:hover { background-color: #74c7ec; }
            QPushButton#delBtn {
                background-color: #f38ba8; color: #1e2533; border: none;
                border-radius: 6px; padding: 6px 16px; font-weight: bold;
            }
            QPushButton#delBtn:hover { background-color: #eb7a99; }
            QComboBox {
                background-color: #2a3146; color: #cdd6f4;
                border: 1px solid #45475a; border-radius: 6px; padding: 4px 8px;
            }
            QComboBox::drop-down { border: none; }
            QComboBox QAbstractItemView {
                background-color: #1e2533; color: #cdd6f4;
                selection-background-color: #45475a;
            }
            QLineEdit {
                background-color: #2a3146; color: #cdd6f4;
                border: 1px solid #45475a; border-radius: 6px; padding: 4px 10px;
            }
            QLineEdit:focus { border: 1px solid #89b4fa; }
            QTableWidget {
                background-color: #1e2533; color: #cdd6f4;
                gridline-color: #2a3146; border: none;
            }
            QTableWidget::item { padding: 6px 8px; }
            QTableWidget::item:selected { background-color: #45475a; color: #cdd6f4; }
            QHeaderView::section {
                background-color: #12161f; color: #89b4fa; font-weight: bold;
                padding: 8px; border: none;
                border-bottom: 2px solid #2a3146; border-right: 1px solid #2a3146;
            }
            QStatusBar {
                background-color: #12161f; color: #a6adc8;
                border-top: 1px solid #2a3146; font-size: 12px; padding: 2px 8px;
            }
            QLabel#fileLabel { color: #585b70; font-size: 11px; }
            QScrollBar:vertical {
                background: #1e2533; width: 8px; border-radius: 4px;
            }
            QScrollBar::handle:vertical { background: #45475a; border-radius: 4px; }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = TaskManager()
    window.show()
    sys.exit(app.exec())