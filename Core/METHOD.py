def coordinate_to_index(i, j, size):
    return i * size + j


def index_to_coordinate(index, size):
    return divmod(index, size)


def format_number(number):
    if number > 1000000000:
        return "1G"
    elif number > 999999:
        return f"{number // 1000000}M"
    elif number > 999:
        return f"{number // 1000}K"
    else:
        return str(number)


def display_number(n, have_neg=True):
    if have_neg:
        number = abs(n)
        neg = '-' if n < 0 else '+'
        return f"{neg}{format_number(number)}"
    else:
        return format_number(n) if n > 0 else '0'


def from_xy_to_position(x, y, size, lt_x, lt_y):
    return lt_x + x * size, lt_y + y * size


def from_index_to_positioin(index, n, size, lt_x, lt_y):
    # lt_x : left_top_x
    # lt_y : left_top_y
    x, y = divmod(index, n)
    return from_xy_to_position(x, y, size, lt_x, lt_y)
