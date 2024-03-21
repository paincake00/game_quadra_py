import sys

from PyQt5.QtWidgets import QApplication

from grid_window import GridWindow

def application():
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()