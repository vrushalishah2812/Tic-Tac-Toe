# from _typeshed import Self
from sys import winver
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    flag = 0
    winner = ''
    last = 0
    o_score_counter = 0
    x_score_counter = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setStyleSheet
        (
            "QMainWindow\n" "{\n" "    background-color : white;\n" "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 120, 271, 16))
        self.line.setStyleSheet
        (
            "Line\n"
            " {\n"
            "    background-color :rgb(132, 129, 129);\n"
            "    border : 100px;\n"
            " }"
        )
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(190, 50, 16, 261))
        self.line_3.setStyleSheet(
            "Line\n"
            " {\n"
            "    background-color :rgb(132, 129, 129);\n"
            "    border : 100px;\n"
            " }"
        )
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(290, 50, 16, 261))
        self.line_4.setStyleSheet(
            "Line\n"
            " {\n"
            "    background-color :rgb(132, 129, 129);\n"
            "    border : 100px;\n"
            " }"
        )
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 220, 271, 16))
        self.line_2.setStyleSheet(
            "Line\n"
            " {\n"
            "    background-color :rgb(132, 129, 129);\n"
            "    border : 100px;\n"
            " }"
        )
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        # Lines for winning
        self.line_win_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_win_1.setGeometry(QtCore.QRect(122, -47, 250, 261))
        self.line_win_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_win_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_win_1.setObjectName("line_win_1")
        self.line_win_1.hide()
        self.line_win_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_win_2.setGeometry(QtCore.QRect(122, 53, 250, 261))
        self.line_win_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_win_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_win_2.setObjectName("line_win_2")
        self.line_win_2.hide()
        self.line_win_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_win_3.setGeometry(QtCore.QRect(123, 153, 250, 261))
        self.line_win_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_win_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_win_3.setObjectName("line_win_3")
        self.line_win_3.hide()
        self.line_win_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_win_4.setGeometry(QtCore.QRect(26, 60, 250, 245))
        self.line_win_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_win_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_win_4.setObjectName("line_win_4")
        self.line_win_4.hide()
        self.line_win_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_win_5.setGeometry(QtCore.QRect(126, 60, 250, 245))
        self.line_win_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_win_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_win_5.setObjectName("line_win_5")
        self.line_win_5.hide()
        self.line_win_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_win_6.setGeometry(QtCore.QRect(226, 60, 250, 245))
        self.line_win_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_win_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_win_6.setObjectName("line_win_6")
        self.line_win_6.hide()

        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 140, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_4.setText("    ")
        # self.pushButton_4.hide()
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(110, 40, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_1.setText(" ")
        # self.pushButton_1.hide()
        self.pushButton_1.setFlat(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 40, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_2.setText("  ")
        # self.pushButton_2.hide()
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 40, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_3.setText("   ")
        # self.pushButton_3.hide()
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 140, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_5.setText("     ")
        # self.pushButton_5.hide()
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 140, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_6.setText("      ")
        # self.pushButton_6.hide()
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 240, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_9.setText("         ")
        # self.pushButton_9.hide()
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 240, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_8.setText("        ")
        # self.pushButton_8.hide()
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 240, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(
            "QPushButton\n" "{\n" "    background: transparent;\n" "}"
        )
        self.pushButton_7.setText("       ")
        # self.pushButton_7.hide()
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(260, 420, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    color : rgb(75, 171, 173);\n"
            "    background: transparent;\n"
            "}"
        )
        self.reset_button.setObjectName("reset_button")
        self.undo_button = QtWidgets.QPushButton(self.centralwidget)
        self.undo_button.setGeometry(QtCore.QRect(130, 420, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.undo_button.setFont(font)
        self.reset_button.clicked.connect(lambda: self.reset())
        self.undo_button.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    color : rgb(75, 171, 173);\n"
            "    background: transparent;\n"
            "}"
        )
        self.undo_button.setObjectName("undo_button")
        self.undo_button.clicked.connect(lambda : self.undo())
        self.o_label = QtWidgets.QLabel(self.centralwidget)
        self.o_label.setGeometry(QtCore.QRect(20, 320, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.o_label.setFont(font)
        self.o_label.setStyleSheet(
            "QLabel\n"
            "{\n"
            "    color : rgb(75, 171, 173);\n"
            "    background: transparent;\n"
            "}"
        )
        self.o_label.setObjectName("o_label")
        self.o_score = QtWidgets.QLabel(self.centralwidget)
        self.o_score.setGeometry(QtCore.QRect(80, 320, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.o_score.setFont(font)
        self.o_score.setStyleSheet(
            "QLabel\n"
            "{\n"
            "    color :rgb(105, 105, 158);\n"
            "    background: transparent;\n"
            "}"
        )
        self.o_score.setObjectName("o_score")
        self.x_label = QtWidgets.QLabel(self.centralwidget)
        self.x_label.setGeometry(QtCore.QRect(20, 360, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.x_label.setFont(font)
        self.x_label.setStyleSheet(
            "QLabel\n"
            "{\n"
            "    color : rgb(75, 171, 173);\n"
            "    background: transparent;\n"
            "}"
        )
        self.x_label.setObjectName("x_label")
        self.x_score = QtWidgets.QLabel(self.centralwidget)
        self.x_score.setGeometry(QtCore.QRect(80, 360, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.x_score.setFont(font)
        self.x_score.setStyleSheet(
            "QLabel\n"
            "{\n"
            "    color :rgb(105, 105, 158);\n"
            "    background: transparent;\n"
            "}"
        )
        self.x_score.setObjectName("x_score")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menua = QtWidgets.QMenu(self.menubar)
        self.menua.setObjectName("menua")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.menua.addAction(self.actiona)
        self.menubar.addAction(self.menua.menuAction())

        self.pushButton_1.clicked.connect(lambda: self.pressbutton(1))
        self.pushButton_2.clicked.connect(lambda: self.pressbutton(2))
        self.pushButton_3.clicked.connect(lambda: self.pressbutton(3))
        self.pushButton_4.clicked.connect(lambda: self.pressbutton(4))
        self.pushButton_5.clicked.connect(lambda: self.pressbutton(5))
        self.pushButton_6.clicked.connect(lambda: self.pressbutton(6))
        self.pushButton_7.clicked.connect(lambda: self.pressbutton(7))
        self.pushButton_8.clicked.connect(lambda: self.pressbutton(8))
        self.pushButton_9.clicked.connect(lambda: self.pressbutton(9))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.reset_button.setText(_translate("MainWindow", "RESET"))
        self.undo_button.setText(_translate("MainWindow", "UNDO"))
        self.o_label.setText(_translate("MainWindow", "O : "))
        self.o_score.setText(_translate("MainWindow", "0"))
        self.x_label.setText(_translate("MainWindow", "X : "))
        self.x_score.setText(_translate("MainWindow", "0"))
        self.menua.setTitle(_translate("MainWindow", "a"))
        self.actiona.setText(_translate("MainWindow", "a"))
        
    def msg_notify(self, text) :
        str = ''
        msg = QMessageBox()
        if text == 'O' :
            msg.setText("{} : WON".format(text))
            self.x = msg.exec_()
            self.o_score_counter += 1
            str = '{}'.format(self.o_score_counter)
            self.o_score.setText(str)
            self.reset()
        elif text == 'X' :
            msg.setText("{} : WON".format(text))
            self.x = msg.exec_()
            self.x_score_counter += 1
            str = '{}'.format(self.x_score_counter)
            self.x_score.setText(str)
            self.reset()
        else :
            msg.setText("{}".format(text))
            self.x = msg.exec_()
            self.reset()

    def check_win(self) :
        global winner      
        if self.pushButton_1.text() == self.pushButton_2.text() and self.pushButton_2.text() == self.pushButton_3.text() :
            self.winner = self.pushButton_1.text()
            self.line_win_1.show()
            self.msg_notify(self.winner)
            self.line_win_1.hide()
        
        elif self.pushButton_4.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_6.text() :
            self.winner = self.pushButton_4.text()
            self.line_win_2.show()
            self.msg_notify(self.winner)
            self.line_win_2.hide()

        elif self.pushButton_7.text() == self.pushButton_8.text() and self.pushButton_8.text() == self.pushButton_9.text() :
            self.winner = self.pushButton_7.text()
            self.line_win_3.show()
            self.msg_notify(self.winner)
            self.line_win_3.hide()
    
        elif self.pushButton_1.text() == self.pushButton_4.text() and self.pushButton_4.text() == self.pushButton_7.text() :
            self.winner = self.pushButton_1.text()
            self.line_win_4.show()
            self.msg_notify(self.winner)
            self.line_win_4.hide()

        elif self.pushButton_2.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_8.text() :
            self.winner = self.pushButton_2.text()
            self.line_win_5.show()
            self.msg_notify(self.winner)
            self.line_win_5.hide()

        elif self.pushButton_3.text() == self.pushButton_6.text() and self.pushButton_6.text() == self.pushButton_9.text() :
            self.winner = self.pushButton_3.text()
            self.line_win_6.show()
            self.msg_notify(self.winner)
            self.line_win_6.hide()

        elif self.pushButton_1.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_9.text() :
            self.winner = self.pushButton_1.text()
            self.msg_notify(self.winner)

        elif self.pushButton_3.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_7.text() :
            self.winner = self.pushButton_3.text()
            self.msg_notify(self.winner)
            
        elif self.flag == 9 :
            self.winner = 'DRAW'
            self.msg_notify(self.winner)
        
    def reset(self) :
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_1.setText(' ')
        self.pushButton_2.setText('  ')
        self.pushButton_3.setText('   ')
        self.pushButton_4.setText('    ')
        self.pushButton_5.setText('     ')
        self.pushButton_6.setText('      ')
        self.pushButton_7.setText('       ')
        self.pushButton_8.setText('        ')
        self.pushButton_9.setText('         ')
        self.flag = 0

    def undo(self) :
        self.flag -= 1
        if self.last == 1 :
            self.pushButton_1.setText(' ')
            self.pushButton_1.setEnabled(True)
            self.last -= 1
        elif self.last == 2 :
            self.pushButton_2.setText('  ')
            self.pushButton_2.setEnabled(True)
            self.last -= 1
        elif self.last == 3 :
            self.pushButton_3.setText('   ')
            self.pushButton_3.setEnabled(True)
            self.last -= 1
        elif self.last == 4 :
            self.pushButton_4.setText('    ')
            self.pushButton_4.setEnabled(True)
            self.last -= 1
        elif self.last == 5 :
            self.pushButton_5.setText('     ')
            self.pushButton_5.setEnabled(True)
            self.last -= 1
        elif self.last == 6 :
            self.pushButton_6.setText('      ')
            self.pushButton_6.setEnabled(True)
            self.last -= 1
        elif self.last == 7 :
            self.pushButton_7.setText('       ')
            self.pushButton_7.setEnabled(True)
            self.last -= 1
        elif self.last == 8 :
            self.pushButton_8.setText('        ')
            self.pushButton_8.setEnabled(True)
            self.last -= 1
        elif self.last == 9 :
            self.pushButton_9.setText('         ')
            self.pushButton_9.setEnabled(True)
            self.last -= 1

    def pressbutton(self, pos) :
        global flag
        global last
        if self.flag % 2 == 0 :
            mark = 'O'
        else :
            mark = 'X'
        if pos == 1 :
            self.pushButton_1.setText(mark)
            self.pushButton_1.show()
            self.pushButton_1.setEnabled(False)   
            self.last = 1
        elif pos == 2 :
            self.pushButton_2.setText(mark)
            self.pushButton_2.show()
            self.pushButton_2.setEnabled(False)
            self.last = 2
        elif pos == 3 :
            self.pushButton_3.setText(mark)
            self.pushButton_3.setEnabled(False)
            self.pushButton_3.show()
            self.last = 3
        elif pos == 4 :
            self.pushButton_4.setText(mark)
            self.pushButton_4.setEnabled(False)
            self.pushButton_4.show()
            self.last = 4
        elif pos == 5 :
            self.pushButton_5.setText(mark)
            self.pushButton_5.setEnabled(False)
            self.last = 5
        elif pos == 6 :
            self.pushButton_6.setText(mark)
            self.pushButton_6.setEnabled(False)
            self.last = 6
        elif pos == 7 :
            self.pushButton_7.setText(mark)
            self.pushButton_7.setEnabled(False)
            self.last = 7
        elif pos == 8 :
            self.pushButton_8.setText(mark)
            self.pushButton_8.setEnabled(False)
            self.last = 8
        else :
            self.pushButton_9.setText(mark)
            self.pushButton_9.setEnabled(False)
            self.last = 9
        self.flag += 1     
        self.check_win()   
 
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
