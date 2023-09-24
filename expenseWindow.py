from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class ExpenseWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self._project_ui = parent
        self.setWindowTitle("Expense Manager: Add Expense")
        self.setFixedSize(700, 450)
        self.set_window()

    def set_window(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 40, 111, 16))
        self.label.setText("Add Expense")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(40, 60, 610, 16))
        self.line.setStyleSheet("color:rgb(128,128,128)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 41, 21))
        self.label_2.setText("To")

        self.selection = QtWidgets.QComboBox(self)
        self.selection.setGeometry(QtCore.QRect(210, 100, 201, 28))
        self.selection.addItems(self._project_ui.get_combo_box_list())
        self.selection.activated.connect(self.get_selection)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(140, 130, 61, 16))
        self.label_3.setText("Amount")

        self.amount = QtWidgets.QTextEdit(self)
        self.amount.setGeometry(QtCore.QRect(210, 130, 101, 21))
        self.amount.textChanged.connect(self.show_msg_box)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(120, 170, 71, 16))
        self.label_4.setText("Description")

        self.desc = QtWidgets.QPlainTextEdit(self)
        self.desc.setGeometry(QtCore.QRect(210, 170, 261, 151))

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(40, 330, 610, 16))
        self.line_2.setStyleSheet("color:rgb(128,128,128)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(500, 350, 81, 31))
        self.push_button.setText("Cancel")
        self.push_button.clicked.connect(self.reject)

        self.push_button_2 = QtWidgets.QPushButton(self)
        self.push_button_2.setGeometry(QtCore.QRect(580, 350, 81, 31))
        self.push_button_2.setText("OK")
        self.push_button_2.clicked.connect(self.accept)

    def show_msg_box(self):
        try:
            revenue_amount = self.amount.toPlainText().strip()
            if revenue_amount:
                revenue_amount = int(revenue_amount)
            else:
                revenue_amount = 0

        except ValueError:
            show_msg = QMessageBox(QMessageBox.Critical,
                                   'Error',
                                   "Number required",
                                   QMessageBox.Ok | QMessageBox.Cancel)
            show_msg.exec_()


    def get_selection(self):
        selected_item = self.selection.currentText()

        return selected_item.rstrip()

    def get_amount(self):
        revenue_amount = self.amount.toPlainText()

        return revenue_amount.rstrip()

    def get_description(self):
        description = self.desc.toPlainText()

        return description.rstrip()
