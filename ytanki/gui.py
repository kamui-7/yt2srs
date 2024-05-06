# Form implementation generated from reading ui file 'ytanki/gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 692)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.container = QtWidgets.QVBoxLayout()
        self.container.setObjectName("container")
        self.link_box = QtWidgets.QVBoxLayout()
        self.link_box.setContentsMargins(-1, -1, -1, 10)
        self.link_box.setObjectName("link_box")
        self.link_label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.link_label.sizePolicy().hasHeightForWidth())
        self.link_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.link_label.setFont(font)
        self.link_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.link_label.setObjectName("link_label")
        self.link_box.addWidget(self.link_label)
        self.link_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.link_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.link_input.setObjectName("link_input")
        self.link_box.addWidget(self.link_input)
        self.container.addLayout(self.link_box)
        self.export_settings_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.export_settings_box.setObjectName("export_settings_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.export_settings_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.export_settings_box)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.note_type_field = QtWidgets.QComboBox(parent=self.export_settings_box)
        self.note_type_field.setEnabled(True)
        self.note_type_field.setObjectName("note_type_field")
        self.verticalLayout_7.addWidget(self.note_type_field)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.export_settings_box)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.audio_field = QtWidgets.QComboBox(parent=self.export_settings_box)
        self.audio_field.setEnabled(True)
        self.audio_field.setObjectName("audio_field")
        self.verticalLayout_9.addWidget(self.audio_field)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_9, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 3, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.export_settings_box)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.picture_field = QtWidgets.QComboBox(parent=self.export_settings_box)
        self.picture_field.setEnabled(True)
        self.picture_field.setObjectName("picture_field")
        self.verticalLayout_10.addWidget(self.picture_field)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.gridLayout_4.addLayout(self.verticalLayout_10, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.export_settings_box)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.text_field = QtWidgets.QComboBox(parent=self.export_settings_box)
        self.text_field.setEnabled(True)
        self.text_field.setObjectName("text_field")
        self.verticalLayout.addWidget(self.text_field)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        self.container.addWidget(self.export_settings_box)
        self.media_settings_box = QtWidgets.QVBoxLayout()
        self.media_settings_box.setObjectName("media_settings_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subtitle_settings_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.subtitle_settings_box.setObjectName("subtitle_settings_box")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.subtitle_settings_box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.subtitle_settings_box)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.language_field = QtWidgets.QComboBox(parent=self.subtitle_settings_box)
        self.language_field.setObjectName("language_field")
        self.horizontalLayout_4.addWidget(self.language_field)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.fallback_checkbox = QtWidgets.QCheckBox(parent=self.subtitle_settings_box)
        self.fallback_checkbox.setObjectName("fallback_checkbox")
        self.verticalLayout_6.addWidget(self.fallback_checkbox)
        self.optimize_checkbox = QtWidgets.QCheckBox(parent=self.subtitle_settings_box)
        self.optimize_checkbox.setObjectName("optimize_checkbox")
        self.verticalLayout_6.addWidget(self.optimize_checkbox)
        self.horizontalLayout_2.addWidget(self.subtitle_settings_box)
        self.media_settings_box.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.media_settings_box.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.generate_settings_box = QtWidgets.QHBoxLayout()
        self.generate_settings_box.setObjectName("generate_settings_box")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.limit_desc = QtWidgets.QLabel(parent=self.groupBox)
        self.limit_desc.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.limit_desc.setObjectName("limit_desc")
        self.verticalLayout_8.addWidget(self.limit_desc)
        self.limit_input = QtWidgets.QSpinBox(parent=self.groupBox)
        self.limit_input.setMaximum(10000)
        self.limit_input.setObjectName("limit_input")
        self.verticalLayout_8.addWidget(self.limit_input)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.generate_settings_box.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.generate_settings_box)
        self.picture_settings_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.picture_settings_box.setObjectName("picture_settings_box")
        self.formLayout = QtWidgets.QFormLayout(self.picture_settings_box)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_10 = QtWidgets.QLabel(parent=self.picture_settings_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_12.addWidget(self.label_10)
        self.width_input = QtWidgets.QSpinBox(parent=self.picture_settings_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_input.sizePolicy().hasHeightForWidth())
        self.width_input.setSizePolicy(sizePolicy)
        self.width_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.width_input.setMaximum(3840)
        self.width_input.setObjectName("width_input")
        self.verticalLayout_12.addWidget(self.width_input)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(parent=self.picture_settings_box)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.height_input = QtWidgets.QSpinBox(parent=self.picture_settings_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_input.sizePolicy().hasHeightForWidth())
        self.height_input.setSizePolicy(sizePolicy)
        self.height_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.height_input.setMaximum(2160)
        self.height_input.setObjectName("height_input")
        self.verticalLayout_11.addWidget(self.height_input, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.horizontalLayout_6)
        self.horizontalLayout_3.addWidget(self.picture_settings_box)
        self.media_settings_box.addLayout(self.horizontalLayout_3)
        self.container.addLayout(self.media_settings_box)
        self.generate_box = QtWidgets.QHBoxLayout()
        self.generate_box.setObjectName("generate_box")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.generate_box.addItem(spacerItem11)
        self.generate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate_button.setObjectName("generate_button")
        self.generate_box.addWidget(self.generate_button)
        self.container.addLayout(self.generate_box)
        self.verticalLayout_2.addLayout(self.container)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.link_label.setText(_translate("MainWindow", "Video Link"))
        self.export_settings_box.setTitle(_translate("MainWindow", "Export Settings"))
        self.label_5.setText(_translate("MainWindow", "Note Type"))
        self.label_7.setText(_translate("MainWindow", "Audio Field"))
        self.label_8.setText(_translate("MainWindow", "Picture Field"))
        self.label_6.setText(_translate("MainWindow", "Text Field"))
        self.subtitle_settings_box.setTitle(_translate("MainWindow", "Subtitle Settings"))
        self.label_4.setText(_translate("MainWindow", "Language"))
        self.fallback_checkbox.setText(_translate("MainWindow", "Fallback to auto-captions"))
        self.optimize_checkbox.setText(_translate("MainWindow", "Optimize subtitles"))
        self.groupBox.setTitle(_translate("MainWindow", "Generate Settings"))
        self.limit_desc.setText(_translate("MainWindow", "Limit (0 = Off)"))
        self.picture_settings_box.setTitle(_translate("MainWindow", "Picture Dimensions (px)"))
        self.label_10.setText(_translate("MainWindow", "Width"))
        self.label_2.setText(_translate("MainWindow", "Height"))
        self.generate_button.setText(_translate("MainWindow", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
