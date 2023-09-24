from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QLabel, QMessageBox


class RevWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super(RevWindow, self).__init__() #What is the difference between this and the others?
        self._project_ui = parent
        self.setWindowTitle("Expense Manager: Add Revenue")
        self.setFixedSize(700, 450)
        self.set_window()

    def set_window(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 40, 111, 16))
        self.label.setText("Add Revenue")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(40, 60, 610, 16))
        self.line.setStyleSheet("color:rgb(128,128,128)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 41, 21))
        self.label_2.setText("To")

        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.setGeometry(QtCore.QRect(210, 100, 201, 28))
        self.combo_box.addItems(self._project_ui.get_combo_box_list())
        self.combo_box.activated.connect(self.get_selection)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(140, 130, 61, 16))
        self.label_3.setText("Amount")

        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setGeometry(QtCore.QRect(210, 130, 101, 21))
        self.text_edit.textChanged.connect(self.get_amount)
        self.text_edit.textChanged.connect(self.show_msg_box)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(120, 170, 71, 16))
        self.label_4.setText("Description")

        self.plain_text_edit = QtWidgets.QPlainTextEdit(self)
        self.plain_text_edit.setGeometry(QtCore.QRect(210, 170, 261, 151))
        self.plain_text_edit.textChanged.connect(self.get_description)


        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(40, 330, 610, 16))
        self.line.setStyleSheet("color:rgb(128,128,128)")
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
            revenue_amount = self.text_edit.toPlainText().strip()
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
        selected_item = self.combo_box.currentText()

        return selected_item.rstrip()

    def get_amount(self):
        revenue_amount = self.text_edit.toPlainText()

        return revenue_amount.rstrip()

    def get_description(self):
        description = self.plain_text_edit.toPlainText()

        return description.rstrip()















