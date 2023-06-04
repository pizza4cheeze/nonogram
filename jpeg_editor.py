from PIL import Image


def get_arr_nonogramm():
    image = Image.open('static/output.jpg')

    pixel_img = []

    for y in range(image.height):
        curr_str = []
        for x in range(image.width):
            # 0 - черный, 255 - белый
            pixel = image.getpixel((x, y))

            if pixel <= 20:
                curr_str.append(1)
            else:
                curr_str.append(0)

        pixel_img.append(curr_str)

    return pixel_img


def compression_to_arr(scale_compression):
    image = Image.open('static/input.png')

    bw_image = image.convert("1")

    width, height = bw_image.size
    new_width = width // scale_compression
    new_height = height // scale_compression

    bw_image = bw_image.resize((new_width, new_height))

    bw_image.save('static/output.jpg')

    return get_arr_nonogramm()

def generate_sides(arr):
    left_col = []
    upper_row = []

    # Генерация строковых условий
    for row in arr:
        row_conditions = []
        count = 0
        for element in row:
            if element == 1:
                count += 1
            elif element == 0 and count > 0:
                row_conditions.append(count)
                count = 0
        if count > 0:
            row_conditions.append(count)
        left_col.append(row_conditions)

    # Генерация столбцовых условий
    for column in zip(*arr):
        column_conditions = []
        count = 0
        for element in column:
            if element == 1:
                count += 1
            elif element == 0 and count > 0:
                column_conditions.append(count)
                count = 0
        if count > 0:
            column_conditions.append(count)
        upper_row.append(column_conditions)

    max_length = 0

    # Перебор первого двумерного массива
    for row in left_col:
        length = len(row)
        if length > max_length:
            max_length = length

    # Перебор второго двумерного массива
    for row in upper_row:
        length = len(row)
        if length > max_length:
            max_length = length

    for i in range(len(left_col)):
        num_zeros = max_length - len(left_col[i])
        left_col[i] = [0] * num_zeros + left_col[i]

    for i in range(len(upper_row)):
        num_zeros = max_length - len(upper_row[i])
        upper_row[i] = [0] * num_zeros + upper_row[i]

    return left_col, upper_row, max_length



counts = generate_sides(compression_to_arr(18))
print(counts)
