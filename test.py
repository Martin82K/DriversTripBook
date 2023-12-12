import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Vytvoření tabulky
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)  # Počet sloupců
        self.table.setHorizontalHeaderLabels(['Středisko', 'Popis'])  # Názvy sloupců

        # Přidání vstupních polí


        # Vytvoření tlačítka
        button = QPushButton('Přidat řádek', self)

        # Přiřazení funkce k signálu "clicked" (stisknutí tlačítka)
        button.clicked.connect(self.add_row)

        # Vytvoření rozložení
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.table)

        # Nastavení rozložení pro hlavní okno
        self.setLayout(layout)

        # Nastavení základních vlastností okna
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('PyQt Tlačítko a Tabulka')

        # Zobrazení okna
        self.show()

    def add_row(self):
        # Přidání nového řádku do tabulky
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Přidání dat do nového řádku
        name_item = QTableWidgetItem('středisko')
        value_item = QTableWidgetItem('cesta')

        self.table.setItem(row_position, 0, name_item)
        self.table.setItem(row_position, 1, value_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
