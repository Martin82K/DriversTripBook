import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem


class DriversTripBookApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Kniha Jízd')
        self.setGeometry(200, 200, 600, 600)

        self.init_ui()

    def init_ui(self):
        # Vytvoření centrálního widgetu a hlavního rozvržení
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Vytvoření prvků UI (popisek, vstupních polí, tlačítka)
        label_company_center = QLabel('Středisko:')
        self.input_company_center = QLineEdit(placeholderText='Stredisko005 - Soukromé, Služební - Služební cesta')

        label_trip_info = QLabel('Popis nebo cíl cesty:')
        self.input_trip_info = QLineEdit(placeholderText="Zadej popis, cíl cesty nebo oblast")

        label_date = QLabel('Datum:')
        self.input_date = QLineEdit(placeholderText='Zadej datum jízdy ve formátu DD.MM.RRRR')

        label_distance = QLabel('Ujetá vzdálenost (km):')
        self.input_distance = QLineEdit(placeholderText='Zadej ujeté kilometry')

        add_button = QPushButton('Přidat jízdu', self)
        add_button.clicked.connect(self.add_trip)

        update_button = QPushButton("Upravit jízdu", self)
        update_button.clicked.connect(self.update_trip)

        delete_button = QPushButton("Smazat jízdu", self)
        delete_button.clicked.connect(self.delete_trip)

        save_file_button = QPushButton("Uložit do souboru", self)
        save_file_button.clicked.connect(self.save_data)

        load_file_button = QPushButton("Načíst ze souboru", self)
        load_file_button.clicked.connect(self.load_data)

        # Vytvoření tabulky pro zobrazení dat
        self.table = QTableWidget(self)
        self.table.setAlternatingRowColors(True)
        self.setStyleSheet("background-color: #2D2F30; color: #FFFFFF")
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Datum', 'Středisko', 'Popis cesty', 'Vzdálenost (km)'])

        # Nastavení šířky sloupců
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(1, 80)
        self.table.setColumnWidth(2, 300)
        self.table.setColumnWidth(3, 100)
        

        # Přidání prvků do rozložení
        layout.addWidget(label_company_center)
        layout.addWidget(self.input_company_center)

        layout.addWidget(label_trip_info)
        layout.addWidget(self.input_trip_info)

        layout.addWidget(label_date)
        layout.addWidget(self.input_date)

        layout.addWidget(label_distance)
        layout.addWidget(self.input_distance)

        """ Vytvoření samostatného layoutu pro tlačítka """
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(delete_button)
        
        layout.addLayout(buttons_layout)

        layout.addWidget(save_file_button)
        layout.addWidget(load_file_button)

        layout.addWidget(self.table)

        central_widget.setLayout(layout)

    def get_values(self):
        """ Získání hodnot z jednotlivých vstupních polí."""
        print("Získávám hodnoty: ")

    def get_trip_info(self):
        """ Získání hodnot z jednotlivých vstupních polí """
        print("Získávám informace o jízdě.")

    def add_trip(self):
        """ Získání hodnot z jednotlivých vstupních polí """
        print("Přidávám jízdu.")

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        """ Získání hodnot z jednotlivých vstupních polí """
        print("Získávám hodnoty: ")
        date = self.input_date.text()
        company_center = self.input_company_center.text()
        trip_info = self.input_trip_info.text()
        distance = self.input_distance.text()

        self.table.setItem(row_position, 0, QTableWidgetItem(date))
        self.table.setItem(row_position, 1, QTableWidgetItem(company_center))
        self.table.setItem(row_position, 2, QTableWidgetItem(trip_info))
        self.table.setItem(row_position, 3, QTableWidgetItem(distance))


    def update_trip(self):
        print("Upravuji jízdu.")
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            for column in range(self.table.columnCount()):
                item = self.table.item(selected_row, column)
                if item is not None:
                    new_value, ok = QInputDialog.getText(
                        self, "Upravit jízdu", 
                        f"Upravit {self.table.horizontalHeaderItem(column).text()}:"
                        )
                    if ok:
                        item.setText(new_value)
        else:
            print("Nelze upravit prázdný řádek.")
            pass

    def delete_trip(self):
        print("Mažu jízdu.")
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            self.table.removeRow(selected_row)
        else:
            print("Nelze smazat prázdný řádek.")
            pass

    def save_data(self):
        print("ukládám data do souboru")
        with open("drivers_trip_book.csv", mode="w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("") # prázdná buňka, pokud nejsou zadány žádné hodnoty
                writer.writerow(row_data)

    def load_data(self):
        print("Načítám data ze souboru")
        with open("drivers_trip_book.csv", mode="r") as file:
            reader = csv.reader(file, delimiter=",")
            for row_data in reader:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                for column, item in enumerate(row_data):
                    self.table.setItem(row_position, column, QTableWidgetItem(item))


def main():
    app = QApplication(sys.argv)
    drivers_book_app = DriversTripBookApp()
    drivers_book_app.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
