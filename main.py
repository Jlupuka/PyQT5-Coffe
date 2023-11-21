import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QWidget
from PyQt5.uic import loadUi


class DataBase:
    def __init__(self) -> None:
        with sqlite3.connect('coffee.sqlite') as conn:
            self.cursor = conn
            conn.isolation_level = None
            self.create_database()

    def create_database(self) -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS coffee (
            id INTEGER PRIMARY KEY,
            sort_name TEXT,
            roast_degree TEXT,
            ground_or_whole TEXT,
            taste_description TEXT,
            price REAL,
            package_volume INTEGER
        )
        """
        self.cursor.execute(sql)

    def get_all_data(self) -> list[list[str]]:
        sql = """
        SELECT
            *
        FROM
            coffee
        """
        return self.cursor.execute(sql).fetchall()

    def add_information(self, sort_name,
                        roast_degree,
                        ground_or_whole,
                        taste_description,
                        price,
                        package_volume) -> None:
        sql = """
        INSERT INTO
             coffee 
                (sort_name,
                roast_degree,
                ground_or_whole,
                taste_description,
                price,
                package_volume)
        VALUES 
            (?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql,
                            (sort_name,
                             roast_degree,
                             ground_or_whole,
                             taste_description,
                             price,
                             package_volume))

    def update_data(self,
                    coffee_id,
                    sort_name,
                    roast_degree,
                    ground_or_whole,
                    taste_description,
                    price,
                    package_volume) -> None:
        sql = """
        UPDATE 
            coffee 
        SET
            sort_name=?,
            roast_degree=?,
            ground_or_whole=?,
            taste_description=?,
            price=?, 
            package_volume=?
        WHERE
            id=?
        """
        self.cursor.execute(sql, (sort_name,
                                  roast_degree,
                                  ground_or_whole,
                                  taste_description,
                                  price,
                                  package_volume,
                                  coffee_id))


class CoffeeApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        loadUi('main.ui', self)

        self.db = DataBase()
        self.add_coffee_window = None

        self.initUI()

    def initUI(self) -> None:
        self.load_data_from_db()
        self.AddpushButton.clicked.connect(self.clicked_add_btn)
        self.EditpushButton.clicked.connect(self.update_data)

    def load_data_from_db(self) -> None:

        data = self.db.get_all_data()

        self.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

    def update_data(self) -> None:
        for row in range(self.tableWidget.rowCount()):
            id_item = self.tableWidget.item(row, 0)
            if id_item is not None:
                coffee_id = int(id_item.text())
                sort_name = self.tableWidget.item(row, 1).text()
                roast_degree = self.tableWidget.item(row, 2).text()
                ground_or_whole = self.tableWidget.item(row, 3).text()
                taste_description = self.tableWidget.item(row, 4).text()
                price = float(self.tableWidget.item(row, 5).text())
                package_volume = int(self.tableWidget.item(row, 6).text())
                self.db.update_data(coffee_id,
                                    sort_name,
                                    roast_degree,
                                    ground_or_whole,
                                    taste_description,
                                    price,
                                    package_volume)

    def clicked_add_btn(self) -> None:
        self.add_coffee_window = AddCoffeeInformation(db=self.db)

        self.close()

        self.add_coffee_window.show()


class AddCoffeeInformation(QWidget):
    def __init__(self, db: DataBase) -> None:
        super().__init__()

        self.db = db
        self.coffee_window = None

        loadUi('addEditCoffeeForm.ui', self)

        self.AddPushButton.clicked.connect(self.add_data)
        self.ExitPushButton.clicked.connect(self.exit_btn)

    def add_data(self) -> None:
        try:
            sort_name = self.SortLineEdit.text()
            roast_degree = self.DegreeLineEdit.text()
            ground_or_whole = self.GWLineEdit.text()
            taste_description = self.DescrLineEdit.text()
            price = self.PriceSpinBox.text()
            package_volume = self.VolumeSpinBox.text()
            self.db.add_information(sort_name,
                                    roast_degree,
                                    ground_or_whole,
                                    taste_description,
                                    price,
                                    package_volume)
        except Exception as ex:
            print(ex.__repr__())

    def exit_btn(self) -> None:
        self.coffee_window = CoffeeApp()

        self.coffee_window.show()

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffeeApp = CoffeeApp()
    coffeeApp.show()
    sys.exit(app.exec_())
