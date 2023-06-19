import sys

from flask import Flask, render_template, redirect, url_for, request
import jpeg_editor

app = Flask(__name__)

arr_to_generate = [0]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    global arr_to_generate
    file = request.files['file']
    number = int(request.form['number'])
    file.save('static/input.png')
    arr_to_generate = jpeg_editor.compression_to_arr(number)
    left_col, upper_row, max_length = jpeg_editor.generate_sides(arr_to_generate)

    return render_template('crossword.html', colunms=upper_row, rows=left_col,
                           height=len(arr_to_generate), width=len(arr_to_generate[0]),
                           max_col_block_size=max_length,
                           max_row_block_size=max_length)


@app.route('/result', methods=['POST'])
def result():
    global arr_to_generate
    left_col, upper_row, max_length = jpeg_editor.generate_sides(arr_to_generate)

    return render_template('result.html', input_array=arr_to_generate, colunms=upper_row, rows=left_col,
                           height=len(arr_to_generate), width=len(arr_to_generate[0]),
                           max_col_block_size=max_length,
                           max_row_block_size=max_length)


if __name__ == '__main__':
    app.run(debug=True)
    # scale = 19
    # arr = jpeg_editor.compression_to_arr(scale)
    # left_col, upper_row, max_len = jpeg_editor.generate_sides(arr)
    # app = result_window.ResultWindow(arr, left_col, upper_row, max_len)
    # app.show()
    # sys.exit()

