import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFrame, QVBoxLayout, QWidget
)

class ZoneWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3 Zones Verticales")
        self.setGeometry(100, 100, 400, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Création et ajout des 3 widgets étendant QFrame
        for _ in range(3):
            zone = ZoneWidget()
            layout.addWidget(zone)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())