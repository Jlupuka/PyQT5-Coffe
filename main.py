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

    def get_all_data(self) -> list[tuple[str]]:
        sql = """
        SELECT
            *
        FROM
            coffee
        """
        return self.cursor.execute(sql).fetchall()


class CoffeeApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        loadUi('main.ui', self)

        self.db = DataBase()

        self.initUI()

    def initUI(self) -> None:
        self.load_data_from_db()

    def load_data_from_db(self) -> None:
        data = self.db.get_all_data()

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffeeApp = CoffeeApp()
    coffeeApp.show()
    sys.exit(app.exec_())
