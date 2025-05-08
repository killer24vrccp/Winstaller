import re
import subprocess
import sys

from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow

from src.pages.mainUI import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        icon = QIcon('src/assets/img/image_fx.jpg')
        self.setWindowIcon(icon)

        if self.ui.go.clicked.connect(self.go_search_app):
            pass

        self.show()

    def go_search_app(self):
        app_name = self.ui.searchApp.text().strip()

        if not app_name:
            print("⚠️ No application name entered.")
            return

        try:
            result = subprocess.run(
                ['winget', 'search', app_name],
                check=True,
                capture_output=True,
                text=True
            )

            lines = result.stdout.splitlines()

            try:
                start_index = next(i for i, line in enumerate(lines) if re.match(r'^-+$', line.strip()))
                table_lines = lines[start_index + 1:]
            except StopIteration:
                print("⚠️ No results table found.")
                return

            table_only = [line for line in table_lines if line.strip() and not re.match(r'^[^a-zA-Z]*$', line)]

            # Create the table model
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(["Name", "ID", "Version", "Source"])

            for line in table_only:
                name = line[:28].strip()
                app_id = line[28:60].strip()
                version = line[60:74].strip()
                source = line[74:].strip()

                model.appendRow([
                    QStandardItem(name),
                    QStandardItem(app_id),
                    QStandardItem(version),
                    QStandardItem(source),
                ])

            # Apply the model to the QTableView
            self.ui.appView.setModel(model)
            self.ui.appView.resizeColumnsToContents()

        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to search for '{app_name}'. Error:\n{e.stderr}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    sys.exit(app.exec())