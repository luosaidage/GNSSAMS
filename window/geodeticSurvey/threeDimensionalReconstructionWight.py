# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threeDimensionalReconstructionWight.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from database.database import Database
from window.geodeticSurvey import callExModuleThread


class Ui_Form(QtCore.QObject):
    infoEmit = QtCore.pyqtSignal(str, str)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1069, 682)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_horizontalCount = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_horizontalCount.setMinimum(1)
        self.spinBox_horizontalCount.setSingleStep(1)
        self.spinBox_horizontalCount.setProperty("value", 10)
        self.spinBox_horizontalCount.setObjectName("spinBox_horizontalCount")
        self.horizontalLayout_2.addWidget(self.spinBox_horizontalCount)
        self.spinBox_verticalCount = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_verticalCount.setMinimum(1)
        self.spinBox_verticalCount.setSingleStep(1)
        self.spinBox_verticalCount.setProperty("value", 10)
        self.spinBox_verticalCount.setObjectName("spinBox_verticalCount")
        self.horizontalLayout_2.addWidget(self.spinBox_verticalCount)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox_cellSize = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spinBox_cellSize.setProperty("value", 10.0)
        self.spinBox_cellSize.setObjectName("spinBox_cellSize")
        self.horizontalLayout_4.addWidget(self.spinBox_cellSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.checkBox_autoSaveCorner = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_autoSaveCorner.setObjectName("checkBox_autoSaveCorner")
        self.verticalLayout_3.addWidget(self.checkBox_autoSaveCorner)
        self.button_camaraPara = QtWidgets.QPushButton(self.groupBox_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/phot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_camaraPara.setIcon(icon)
        self.button_camaraPara.setIconSize(QtCore.QSize(50, 50))
        self.button_camaraPara.setCheckable(False)
        self.button_camaraPara.setAutoRepeat(False)
        self.button_camaraPara.setAutoExclusive(False)
        self.button_camaraPara.setAutoRepeatDelay(500)
        self.button_camaraPara.setAutoRepeatInterval(300)
        self.button_camaraPara.setAutoDefault(True)
        self.button_camaraPara.setDefault(False)
        self.button_camaraPara.setFlat(False)
        self.button_camaraPara.setObjectName("button_camaraPara")
        self.verticalLayout_3.addWidget(self.button_camaraPara)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_videoFrame = QtWidgets.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./source/icon/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_videoFrame.setIcon(icon1)
        self.button_videoFrame.setIconSize(QtCore.QSize(50, 50))
        self.button_videoFrame.setCheckable(False)
        self.button_videoFrame.setAutoRepeat(False)
        self.button_videoFrame.setAutoExclusive(False)
        self.button_videoFrame.setAutoRepeatDelay(500)
        self.button_videoFrame.setAutoRepeatInterval(300)
        self.button_videoFrame.setAutoDefault(True)
        self.button_videoFrame.setDefault(False)
        self.button_videoFrame.setFlat(False)
        self.button_videoFrame.setObjectName("button_videoFrame")
        self.verticalLayout_2.addWidget(self.button_videoFrame)
        self.button_pointCode = QtWidgets.QPushButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./source/icon/3d-modelling.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_pointCode.setIcon(icon2)
        self.button_pointCode.setIconSize(QtCore.QSize(50, 50))
        self.button_pointCode.setObjectName("button_pointCode")
        self.verticalLayout_2.addWidget(self.button_pointCode)
        self.button_3D = QtWidgets.QPushButton(self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./source/icon/3D.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_3D.setIcon(icon3)
        self.button_3D.setIconSize(QtCore.QSize(50, 50))
        self.button_3D.setObjectName("button_3D")
        self.verticalLayout_2.addWidget(self.button_3D)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./source/icon/song.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_openModel = QtWidgets.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./source/icon/3d-glasses.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_openModel.setIcon(icon4)
        self.button_openModel.setIconSize(QtCore.QSize(50, 50))
        self.button_openModel.setObjectName("button_openModel")
        self.horizontalLayout.addWidget(self.button_openModel)
        self.button_changeModel = QtWidgets.QPushButton(self.groupBox)
        self.button_changeModel.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./source/icon/time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_changeModel.setIcon(icon5)
        self.button_changeModel.setIconSize(QtCore.QSize(50, 50))
        self.button_changeModel.setObjectName("button_changeModel")
        self.horizontalLayout.addWidget(self.button_changeModel)
        self.button_clear = QtWidgets.QPushButton(self.groupBox)
        self.button_clear.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./source/icon/Bulldozer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_clear.setIcon(icon6)
        self.button_clear.setIconSize(QtCore.QSize(50, 50))
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout.addWidget(self.button_clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Form)

        self.button_3D.setEnabled(False)

        self.button_clear.clicked.connect(self.textEdit.clear)

        self.callModule = callExModuleThread.CallExModule()
        self.callModule.infoEmit.connect(self.showInfo)
        self.button_pointCode.clicked.connect(self.actionCallVisualSFM)
        self.button_openModel.clicked.connect(self.actionCallMeshLab)
        self.button_camaraPara.clicked.connect(self.getPara_CHESE)
        self.button_3D.clicked.connect(self.actionCallMeshLab)
        self.button_videoFrame.clicked.connect(self.videoKeyFrame)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_3.setTitle(_translate("Form", "相机参数"))
        self.label_2.setText(_translate("Form", "棋盘角点："))
        self.label_4.setText(_translate("Form", "方格尺寸(mm)："))
        self.checkBox_autoSaveCorner.setText(_translate("Form", "保存角点标记图"))
        self.button_camaraPara.setText(_translate("Form", "参数纠正"))
        self.groupBox_2.setTitle(_translate("Form", "三维模型"))
        self.button_videoFrame.setText(_translate("Form", "视频抽帧"))
        self.button_pointCode.setText(_translate("Form", "点云重建"))
        self.button_3D.setText(_translate("Form", "模型构建"))
        self.button_openModel.setText(_translate("Form", "查看模型"))
        self.button_changeModel.setText(_translate("Form", "时序模型形变监测"))

    def defaultStatus(self):
        self.button_3D.isEnabled()

    def showInfo(self, type, strInfo):
        if type == "3D":
            self.textEdit.append(strInfo)
        elif type == "kill":
            self.callModule.killThread()
            self.showInfo("I", "关闭子线程.")
        else:
            self.infoEmit.emit(type, strInfo)

    def actionCallVisualSFM(self):
        self.callModule.setPara({"code": 100})
        self.callModule.start()
        self.showInfo("3D", " -[SFM] 已启动 VisualSFM 三维重建模块")
        self.showInfo("I", "- 三维模型构建模块 已激活")
        self.button_3D.setEnabled(True)

    def actionCallMeshLab(self):
        self.callModule.setPara({"code": 101})
        self.callModule.start()
        self.showInfo("3D", " -[SFM] 已启动 MeshLab 点云重建模型-纹理贴图处理模块")

    def getPara_CHESE(self):
        imagePaths, type = QtWidgets.QFileDialog.getOpenFileNames(self.parent(), "指定标定影像路径", Database.workspace,
                                                                  "JPEG(*.JPG);;All Files(*)")
        if len(imagePaths) > 0:
            dir, name = os.path.split(imagePaths[0])
            self.showInfo("dirFile", dir)
            self.callModule.setPara(
                {"code": 102, "paths": imagePaths, "horizontalCount": int(self.spinBox_horizontalCount.text()),
                 "verticalCount": int(self.spinBox_verticalCount.text()),
                 "cellSize": float(self.spinBox_cellSize.text()),
                 "autoSaveCorner": self.checkBox_autoSaveCorner.isChecked()})
            self.callModule.start()

    def videoKeyFrame(self):
        self.showInfo("T", "由于设计缺陷，该功能的交互式执行暂时关闭！")
        # videoPath, type = QtWidgets.QFileDialog.getOpenFileNames(self.parent(), "选择视频", Database.workspace,
        #                                                          "MP4(*.mp4);;All Files(*)")
        # if len(videoPath) > 0:
        #     dir, name = os.path.split(videoPath[0])
        #     self.showInfo("dirFile", dir)
        #     self.callModule.setPara({"code": 103, "videoPath": videoPath})
        #     self.callModule.start()
