from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class ResultWindow(QMainWindow):
    def __init__(self, arr_to_generate, left_col, upper_row, max_length):
        super().__init__()
        self.setWindowTitle("Result Window")
        self.setGeometry(100, 100, 800, 800)

        # Отступы для массивов left_col и upper_row
        left_col_offset = QtCore.QPoint(0, max_length * 30)
        upper_row_offset = QtCore.QPoint(max_length * 30, 0)

        # Отрисовка массива left_col
        for row_num, row in enumerate(left_col):
            for col_num, value in enumerate(row):
                button = QPushButton(self)
                button.setGeometry(QtCore.QRect(left_col_offset.x() + col_num * 30, left_col_offset.y() + row_num * 30, 30, 30))
                button.setText(str(value))
                button.setEnabled(False)

        # Отрисовка массива upper_row
        for row_num, row in enumerate(upper_row):
            for col_num, value in enumerate(row):
                button = QPushButton(self)
                button.setGeometry(QtCore.QRect(upper_row_offset.x() + col_num * 30, upper_row_offset.y() + row_num * 30, 30, 30))
                button.setText(str(value))
                button.setEnabled(False)

        # Отрисовка поля из кнопок
        for row_num, row in enumerate(arr_to_generate):
            for col_num, value in enumerate(row):
                button = QPushButton(self)
                button.setGeometry(QtCore.QRect(max_length * 30 + col_num * 30, max_length * 30 + row_num * 30, 30, 30))
                button.setStyleSheet("background-color: white")
                button.clicked.connect(self.button_clicked)


    def button_clicked(self):
        # Обработчик события нажатия кнопки
        button = self.sender()
        if button.styleSheet() == "background-color: white":
            button.setStyleSheet("background-color: black")
        else:
            button.setStyleSheet("background-color: white")



