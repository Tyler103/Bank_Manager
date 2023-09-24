from PyQt5 import QtCore, QtGui, QtWidgets


class CategoryWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self._project_ui = parent
        self.setWindowTitle("Expense Manager: Add Expense")
        self.setFixedSize(700, 450)
        self.set_window()

    def set_window(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 40, 111, 16))
        self.label.setText("Add Category")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(40, 60, 610, 16))
        self.line.setStyleSheet("color:rgb(128,128,128)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 71, 21))
        self.label_2.setText("Category")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(240, 100, 201, 28))

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(40, 300, 610, 16))
        self.line.setStyleSheet("color:rgb(128,128,128)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(500, 320, 81, 31))
        self.push_button.setText("Cancel")
        self.push_button.clicked.connect(self.reject)

        self.push_button_2 = QtWidgets.QPushButton(self)
        self.push_button_2.setGeometry(QtCore.QRect(580, 320, 81, 31))
        self.push_button_2.setText("OK")
        self.push_button_2.clicked.connect(self.accept)




