import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Editor(QDialog):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.text = QTextEdit()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        self.setLayout(layout)
        self.setWindowTitle("Text Editor")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Editor()
    window.resize(350, 250)
    window.show()
    sys.exit(app.exec_())