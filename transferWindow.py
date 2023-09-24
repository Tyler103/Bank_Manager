from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QComboBox, QApplication, QFontComboBox, QMessageBox


class TransferWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self._project_ui = parent
        self.setWindowTitle("Expense Manager")
        self.setFixedSize(700, 450)
        self.set_window()

    def set_window(self):

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 80, 341, 191))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 30, 141, 31))
        self.label.setText("Transfer Money")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(40, 60, 610, 16))
        self.line.setStyleSheet("color:rgb(128,128,128)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)

        self._from = QtWidgets.QLabel(self)
        self._from.setGeometry(QtCore.QRect(110, 86, 41, 21))
        self._from.setText("   From")

        self.from_selection = QComboBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.from_selection, 0, 0, 1, 1)
        self.from_selection.addItems(self._project_ui.get_combo_box_list())
        self.from_selection.activated.connect(self.error_check)


        self._to = QtWidgets.QLabel(self)
        self._to.setGeometry(QtCore.QRect(110, 120, 58, 22))
        self._to.setText("   To")

        self.to_selection = QComboBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.to_selection, 1, 0, 1, 1)
        self.to_selection.addItems(self._project_ui.get_combo_box_list())
        self.to_selection.activated.connect(self.get_outgoing_selection)
        self.to_selection.activated.connect(self.error_check)

        self._amount = QtWidgets.QLabel(self)
        self._amount.setGeometry(QtCore.QRect(110, 160, 58, 21))
        self._amount.setText("   Amount")

        self.amount_entry = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.amount_entry, 2, 0, 1, 1)
        self.amount_entry.textChanged.connect(self.check)


        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(500, 310, 81, 31))
        self.push_button.setText("Submit")
        self.push_button.clicked.connect(self.accept)
        self.push_button.clicked.connect(self.show_msg_box)



        self.push_button_2 = QtWidgets.QPushButton(self)
        self.push_button_2.setGeometry(QtCore.QRect(580, 310, 81, 31))
        self.push_button_2.setText("Cancel")
        self.push_button_2.clicked.connect(self.reject)


        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(40, 280, 610, 16))
        self.line.setStyleSheet("color:rgb(128,128,128)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
    def check(self):
        try:
            revenue_amount = self.amount_entry.toPlainText().strip()
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
    def show_msg_box(self):

        amount = str(self.amount_entry.toPlainText())
        from_account = self.from_selection.currentText()
        to_account = self.to_selection.currentText()

        message = f"Thank you! ${amount} was successfully transferred from {from_account} to {to_account}."

        show_msg = QMessageBox(QMessageBox.Information,
                                'Money Transferred Successfully',
                                message,
                                QMessageBox.Ok,
                                self)
        show_msg.setText('Money Transferred Successfully')
        show_msg.setInformativeText(message)
        show_msg.exec_()

    def error_check(self):
        if self.to_selection.currentText() == self.from_selection.currentText():
            show_msg = QMessageBox(QMessageBox.Critical,
                                   'Error',
                                   "Same location",
                                   QMessageBox.Ok | QMessageBox.Cancel)
            show_msg.exec_()
            self.push_button_2.clicked.connect(self.reject)

    def transfer_amount(self):
        transfer_amount = self.amount_entry.toPlainText()

        return transfer_amount.rstrip()

    def get_outgoing_selection(self):
        selection = self.to_selection.currentText()

        return selection.rstrip()

    def get_from_selection(self):
        selection = self.from_selection.currentText()

        return selection.rstrip()




