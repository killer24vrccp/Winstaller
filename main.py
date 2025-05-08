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
        import re
        from PySide6.QtGui import QStandardItemModel, QStandardItem
        import subprocess

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

            # Trouve l'en-tête et la ligne de séparation
            try:
                header_index = next(
                    i for i, line in enumerate(lines) if re.match(r'^\s*Nom\s+ID\s+Version\s+Source\s*$', line))
                separator_index = header_index + 1
                table_lines = lines[separator_index + 1:]
            except StopIteration:
                print("⚠️ No results table found.")
                return

            # Longueurs de colonnes (à ajuster selon ton format exact)
            name_width = 27
            id_width = 20
            version_width = 10
            # Source = reste

            # Crée le modèle
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(["Name", "ID", "Version", "Source"])

            for line in table_lines:
                if not line.strip():
                    continue

                name = line[0:26].strip()  # Jusqu'à colonne ID
                app_id = line[26:46].strip()  # Jusqu'à Version
                version = line[46:56].strip()  # Jusqu'à Source
                source = line[56:].strip()  # Le reste

                model.appendRow([
                    QStandardItem(name),
                    QStandardItem(app_id),
                    QStandardItem(version),
                    QStandardItem(source),
                ])

            self.ui.appView.setModel(model)
            self.ui.appView.resizeColumnsToContents()

        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to search for '{app_name}'. Error:\n{e.stderr}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    sys.exit(app.exec())