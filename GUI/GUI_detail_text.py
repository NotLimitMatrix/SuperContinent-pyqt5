from GUI import (
    CONST,
    QTextBrowser,
    QFont,
)


class DetailText:
    def __init__(self, parent):
        textBrowser = QTextBrowser(parent)
        textBrowser.setGeometry(CONST.DETAIL_START_X, CONST.DETAIL_START_Y,
                                CONST.DETAIL_WIDTH, CONST.DETAIL_HEIGHT)
        font = QFont()
        font.setPixelSize(12)

        textBrowser.setFont(font)
        self.tb = textBrowser
        self.text = '没有信息'

    def check_items(self, items):
        if items == self.text:
            return True

        self.text = items
        if self.text:
            return False
        else:
            self.text = '没有信息'
            return True

    def update(self, items):
        if self.check_items(items):
            return

        self.tb.setText(self.text)
