import sys
from PyQt5 import QtWidgets
from project_ui import UiDialog


def main():
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = UiDialog()
    ui.set_up_ui(dialog)
    dialog.show()
    sys.exit(app.exec_())


main()

