from PyQt5.QtCore import QRect


class Zoning:
    def __init__(self, ident, row, col, size):
        self.ident = ident
        self.row = row
        self.col = col
        self.size = size

    def real_position(self, top, left):
        return QRect(self.size * self.col + left, self.size * self.row + top, self.size, self.size)
