import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QTableWidget
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee.ui', self)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffeeee.sqlite3')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()
        self.tableView.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
