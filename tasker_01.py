# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasker.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import logick

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 908)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(434, 240, 661, 611))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 240, 421, 611))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.update_task)
        self.listWidget.itemClicked.connect(self.delete_task)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 50, 231, 111))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 50, 791, 111))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(554, 10, 301, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.add_task())
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 281, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.add_item())
        self.pushButton_2.setGeometry(QtCore.QRect(350, 180, 321, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.delete_task_sql())
        self.pushButton_3.setGeometry(QtCore.QRect(730, 180, 361, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(False)
        self.action.setChecked(False)
        self.action.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.action.setObjectName("action")
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.add_item()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Описание"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
        self.menu.setTitle(_translate("MainWindow", "Создать новую задачу"))
        self.action.setText(_translate("MainWindow", "Создать"))

    global item 
    def add_item(self):
        self.listWidget.clear()
        item = logick.view_task()
        for item_list in item:
            print(item_list)
            self.listWidget.addItem(item_list[0])

    def add_task(self): 
        name = self.lineEdit.text() 
        text = self.lineEdit_2.text()
        logick.create_task(name,text)
        self.lineEdit.setText("Добавлено!!!")
        
    def delete_task(self,item):
        a = self.lineEdit.setText(item.text())
        
    def delete_task_sql(self):
        b = self.lineEdit.text()
        logick.delete_task(b)

    def update_task(self,item):
        list_item = logick.get_task_text(item.text())
        self.label.setText(list_item[0])
        #self.lineEdit.setText(list_item[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())