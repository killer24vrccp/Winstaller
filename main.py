import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from src.pages.mainUI import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    sys.exit(app.exec())