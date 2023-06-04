import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from flask import Flask, render_template, redirect, url_for, request
import jpeg_editor
import result_window

app = Flask(__name__)


class ResultWindow(QMainWindow):
    def __init__(self, arr_to_generate, left_col, upper_row, max_length):
        super().__init__()
        self.setWindowTitle("Result Window")
        self.setGeometry(100, 100, max_length * 20 * 2 + len(arr_to_generate[0]) * 30, max_length * 20 * 2 + len(arr_to_generate) * 30)

        # Отступы для массивов left_col и upper_row
        left_col_offset = QtCore.QPoint(0, max_length * 20)
        upper_row_offset = QtCore.QPoint(max_length * 20, 0)

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
                button.setGeometry(QtCore.QRect(max_length * 20 + col_num * 30, max_length * 20 + row_num * 30, 30, 30))
                button.setStyleSheet("background-color: white")
                button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # Обработчик события нажатия кнопки
        button = self.sender()
        if button.styleSheet() == "background-color: white":
            button.setStyleSheet("background-color: black")
        else:
            button.setStyleSheet("background-color: white")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    number = int(request.form['number'])
    # Выполнение операций с загруженным файлом и числом
    file.save('static/input.png')
    arr_to_generate = jpeg_editor.compression_to_arr(number)
    left_col, upper_row, max_length = jpeg_editor.generate_sides(arr_to_generate)

    # Открытие окна результатов с передачей параметров
    result_window = ResultWindow(arr_to_generate, left_col, upper_row, max_length)
    result_window.show()

    return redirect(url_for('index'))


if __name__ == '__main__':
    # app.run(debug=True, threaded=True)
    scale = 19
    arr = jpeg_editor.compression_to_arr(scale)
    left_col, upper_row, max_len = jpeg_editor.generate_sides(arr)
    app = result_window.ResultWindow(arr, left_col, upper_row, max_len)
    app.show()
    sys.exit()

