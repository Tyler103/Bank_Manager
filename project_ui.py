from io import BytesIO

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem
from category import Category
from categoryWindow import CategoryWindow
from expenseWindow import ExpenseWindow
from revWindow import RevWindow
from transferWindow import TransferWindow
import matplotlib.pyplot as plt


# change everything to snake case from camelcase
class UiDialog(QMainWindow):
    def __init__(self):
        super(UiDialog, self).__init__()
        self._category_list = []
        self._combo_box_list = []
        self._dictionary = {}

        self._des_list = []
        self._expense_list = []
        self._correspond_list = []

        self.category = None

    def set_up_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(751, 563)

        self.grid_layout_widget = QtWidgets.QWidget(dialog)
        self.grid_layout_widget.setGeometry(QtCore.QRect(60, 10, 608, 261))
        self.grid_layout_widget.setObjectName("gridLayoutWidget")

        # overall grid layout
        self.grid_layout = QtWidgets.QGridLayout(self.grid_layout_widget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName("gridLayout")
        self.graphics_view = QtWidgets.QGraphicsView(self.grid_layout_widget)
        self.graphics_view.setObjectName("graphicsView")
        self.grid_layout.addWidget(self.graphics_view, 1, 2, 2, 3)

        # revenue button
        self.revenue_button = QtWidgets.QPushButton(self.grid_layout_widget)
        self.revenue_button.setObjectName("revenueButton")
        self.revenue_button.setAutoDefault(False)
        self.grid_layout.addWidget(self.revenue_button, 0, 1, 1, 1)

        # category button
        self.cate_button = QtWidgets.QPushButton(self.grid_layout_widget)
        self.cate_button.setObjectName("cateButton")
        self.cate_button.setAutoDefault(False)
        self.grid_layout.addWidget(self.cate_button, 0, 0, 1, 1)

        # drop down menu
        self.drop_down = QtWidgets.QComboBox(self.grid_layout_widget)
        self.drop_down.setObjectName("drop_down")
        self.grid_layout.addWidget(self.drop_down, 1, 0, 1, 2)
        self.drop_down.activated.connect(self.update_results)


        # chart area
        self.scroll_area = QtWidgets.QScrollArea(self.grid_layout_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scrollArea")
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 242, 188))
        self.scroll_area_widget_contents.setObjectName("scrollAreaWidgetContents")

        # table
        self.table = QtWidgets.QTableWidget(self.scroll_area_widget_contents)
        self.table.setGeometry(QtCore.QRect(0, 0, 235, 181))
        self.table.setObjectName("table")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.grid_layout.addWidget(self.scroll_area, 2, 0, 1, 2)

        # transfer button
        self.transfer_button = QtWidgets.QPushButton(self.grid_layout_widget)
        self.transfer_button.setObjectName("transferButton")
        self.transfer_button .setAutoDefault(False)
        self.grid_layout.addWidget(self.transfer_button, 0, 3, 1, 1)

        # expense button
        self.expense_button = QtWidgets.QPushButton(self.grid_layout_widget)
        self.expense_button.setObjectName("expenseButton")
        self.expense_button.setAutoDefault(False)
        self.grid_layout.addWidget(self.expense_button, 0, 2, 1, 1)

        # quit button
        self.quit_button = QtWidgets.QPushButton(dialog)
        self.quit_button.setGeometry(QtCore.QRect(600, 360, 69, 32))
        self.quit_button.setObjectName("quitButton")
        self.quit_button.setAutoDefault(False)

        # Bottom line
        self.line = QtWidgets.QFrame(dialog)
        self.line.setGeometry(QtCore.QRect(60, 330, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setStyleSheet("color:rgb(128,128,128)")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setObjectName("line")

        # label for text total
        self.text_label = QtWidgets.QLabel(dialog)
        self.text_label.setGeometry(QtCore.QRect(70, 250, 114, 101))
        self.text_label.setObjectName("label")

        self.pie_label = QtWidgets.QLabel(dialog)
        self.pie_label.setGeometry(QtCore.QRect(400, 20, 390, 290))
        self.pie_label.setObjectName("label_2")

        # total box label
        self.text_browser = QtWidgets.QLineEdit(dialog)
        self.text_browser.setGeometry(QtCore.QRect(220, 290, 90, 21))
        self.text_browser.setObjectName("textBrowser")


        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

        self.revenue_button.clicked.connect(self.add_revenue)
        self.cate_button.clicked.connect(self.add_category)
        self.expense_button.clicked.connect(self.add_expense)
        self.transfer_button.clicked.connect(self.transfer_money)

        self.quit_button.clicked.connect(self.quit_program)

    def create_pie(self, slices, candidates):

        # makes sure that multiple names are not added
        for i in range(len(candidates)):
            category = candidates[i]
            value = slices[i]
            if category in self._dictionary:
                self._dictionary[category] += value
            else:
                self._dictionary[category] = value

        labels = list(self._dictionary.keys())
        sizes = list(self._dictionary.values())

        buffer = BytesIO()
        plt.figure(figsize=(2, 2))
        plt.pie(sizes,
                labels=labels,
                startangle=-110,
                shadow=False,
                autopct="%1.2f%%", labeldistance=1.05)
        plt.title("Spending Percentage")

        plt.savefig(buffer)
        image_bytes = buffer.getvalue()
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)

        self.pie_label.clear()
        self.pie_label.setPixmap(pixmap)

    def update_results(self):
        current_selection = self.drop_down.currentText()
        self.category = self.get_object(current_selection)

        self.text_browser.setText("{:.2f}".format(self.category.get_balance()))

        if len(self.category.wallet):
            self.table.setRowCount(len(self.category.wallet))
            self.table.setColumnCount(2)
            self.table.setColumnWidth(0, 150)

            self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Item"))
            self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Price"))
            for i, item in enumerate(self.category.wallet):
                self.table.setItem(i, 0, QTableWidgetItem(item["description"]))
                self.table.setItem(i, 1, QTableWidgetItem("{:.2f}".format(item["amount"])))

                if item["description"] not in self._des_list:
                    if item["amount"] < 0:
                        self._expense_list.append(item["amount"] * -1)
                        self._des_list.append(item["description"])
                        self._correspond_list.append(self.category.category)

                        if len(self._expense_list) > 0:
                            self.create_pie(self._expense_list, self._correspond_list)

        else:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)

    def get_combo_box_list(self):
        list = [self.drop_down.itemText(i) for i in range(self.drop_down.count())]

        return list

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Expense Manager"))

        self.revenue_button.setText(_translate("Dialog", "Add Revenue"))
        self.cate_button.setText(_translate("Dialog", "Add Category"))
        self.expense_button.setText(_translate("Dialog", "Add Expense"))
        self.transfer_button.setText(_translate("Dialog", "Transfer Money"))

        self.quit_button.setText(_translate("Dialog", "Exit"))
        self.text_label.setText(_translate("Dialog", "Total"))

    def add_revenue(self):
        revenue_dialog = RevWindow(self)
        outcome = revenue_dialog.exec_()

        if outcome == QDialog.Accepted:
            selection = revenue_dialog.get_selection()
            amount = revenue_dialog.get_amount()
            description = revenue_dialog.get_description()

            for item in self._category_list:
                if selection == item.category:
                    item.add_revenue(int(amount), description)

            self.update_results()


    def transfer_money(self):
        transfer_dialog = TransferWindow(self)
        outcome = transfer_dialog.exec_()

        if outcome == QDialog.Accepted:
            transfer_amount = transfer_dialog.transfer_amount()
            from_selection = transfer_dialog.get_from_selection()
            to_selection = transfer_dialog.get_outgoing_selection()

            from_value = self.get_object(from_selection)
            to_value = self.get_object(to_selection)

            from_value.transfer_money(int(transfer_amount), to_value)

            self.update_results()

    def add_expense(self):
        expense_dialog = ExpenseWindow(self)
        outcome = expense_dialog.exec_()

        if outcome == QDialog.Accepted:
            selection = expense_dialog.get_selection()
            amount = expense_dialog.get_amount()
            description = expense_dialog.get_description()

            for item in self._category_list:
                if selection == item.category:
                    item.add_expense(int(amount), description)

            self.update_results()


    def get_object(self, value):
        for item in self._category_list:
            if value == item.category:
                return item

    def add_category(self):
        category_dialog = CategoryWindow(self)
        outcome = category_dialog.exec_()

        if outcome == QDialog.Accepted:
            category_name = category_dialog.textEdit.toPlainText()
            if category_name not in self._combo_box_list:
                self._combo_box_list.append(category_name)
                self.drop_down.addItem(category_name)
                self.category = Category(category_name)
                self._category_list.append(self.category)

    def quit_program(self):
        QApplication.instance().quit()

    def print_category_list(self):
        for category in self._category_list:
            print("category: " + category.category)
            print("Bal: " + str(category.get_balance()))

            for item in category.wallet:
                print(item)




