# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'circularCurveWight.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtCore.QObject):
    infoEmit = QtCore.pyqtSignal(str, str)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1198, 765)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_mainMileage = QtWidgets.QPushButton(self.groupBox)
        self.button_mainMileage.setObjectName("button_mainMileage")
        self.verticalLayout_2.addWidget(self.button_mainMileage)
        self.button_pointStation = QtWidgets.QPushButton(self.groupBox)
        self.button_pointStation.setObjectName("button_pointStation")
        self.verticalLayout_2.addWidget(self.button_pointStation)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_easementMainMileage = QtWidgets.QPushButton(self.groupBox_2)
        self.button_easementMainMileage.setObjectName("button_easementMainMileage")
        self.verticalLayout_3.addWidget(self.button_easementMainMileage)
        self.button_easementPointStation = QtWidgets.QPushButton(self.groupBox_2)
        self.button_easementPointStation.setObjectName("button_easementPointStation")
        self.verticalLayout_3.addWidget(self.button_easementPointStation)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.groupBox_3)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./source/icon/ric.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(Form)
        self.button_mainMileage.clicked.connect(self.actionMainMileage)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "圆曲线计算"))
        self.button_mainMileage.setText(_translate("Form", "计算主点里程"))
        self.button_pointStation.setText(_translate("Form", "解算曲线中桩点坐标"))
        self.groupBox_2.setTitle(_translate("Form", "带缓和曲线的圆曲线计算"))
        self.button_easementMainMileage.setText(_translate("Form", "计算主点里程"))
        self.button_easementPointStation.setText(_translate("Form", "解算曲线中桩点坐标"))
        self.groupBox_3.setTitle(_translate("Form", "待解算数据"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "圆曲线半径/m"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "路线转向角/(°)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "路线转向角类型/(R/L)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "交点JD里程/m"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "*交点JD的X坐标/m"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "*交点JD的Y坐标/m"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "*待求中桩点里程/m"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "入(出)线坐标方位角/°"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "示例1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "203"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "20.36"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "R"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "258.36"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.commandLinkButton.setText(_translate("Form", "1.右键单击上方表格区域可以手动添加数据； 2.可以导入整理后的.rc格式的文本文件，格式参照说明"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">说明：</p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.如果只解算主点里程，数据只需要输入到交点JD里程即可；</p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.所有输入的角度的单位均取: 度(°)；</p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.坐标方位角取法：</p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  1）待求点在ZY-QZ：ZYJD；</p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  2）待求点在QZ-YZ：JDYZ；</p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  3）同理，对于带有缓和曲线的坐标方位角取法：ZHJD or JDHZ。</p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:10.5pt; font-style:italic; color:#546e7a;\">=================</span></p></body></html>"))

    def actionMainMileage(self):
        # 从表格读取数据
        tableRow = self.tableWidget.rowCount()
        tableColumn = self.tableWidget.columnCount()
        for i in range(tableRow):
            for k in range(tableColumn):
                print(self.tableWidget.item(i, k).text())

    def sendTopInfo(self,type,strInfo):
        self.infoEmit.emit(type,strInfo)