# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\u64132\Documents\mtpy2\mtpy\gui\SmartMT\ui_asset\dialog_export.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_Export(object):
    def setupUi(self, Dialog_Export):
        Dialog_Export.setObjectName(_fromUtf8("Dialog_Export"))
        Dialog_Export.resize(400, 171)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_Export)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget = QtGui.QWidget(Dialog_Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_export = QtGui.QPushButton(self.widget)
        self.pushButton_export.setObjectName(_fromUtf8("pushButton_export"))
        self.gridLayout.addWidget(self.pushButton_export, 1, 2, 1, 1)
        self.pushButton_preview = QtGui.QPushButton(self.widget)
        self.pushButton_preview.setObjectName(_fromUtf8("pushButton_preview"))
        self.gridLayout.addWidget(self.pushButton_preview, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_cancel = QtGui.QPushButton(self.widget)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 3, 1, 1)
        self.checkBox_open_after_export = QtGui.QCheckBox(self.widget)
        self.checkBox_open_after_export.setChecked(True)
        self.checkBox_open_after_export.setObjectName(_fromUtf8("checkBox_open_after_export"))
        self.gridLayout.addWidget(self.checkBox_open_after_export, 0, 2, 1, 2)
        self.gridLayout_2.addWidget(self.widget, 7, 0, 1, 5)
        self.label_5 = QtGui.QLabel(Dialog_Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog_Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog_Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog_Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.checkBox_tightBbox = QtGui.QCheckBox(Dialog_Export)
        self.checkBox_tightBbox.setChecked(True)
        self.checkBox_tightBbox.setObjectName(_fromUtf8("checkBox_tightBbox"))
        self.gridLayout_2.addWidget(self.checkBox_tightBbox, 2, 4, 1, 1)
        self.comboBox_fileName = QtGui.QComboBox(Dialog_Export)
        self.comboBox_fileName.setEditable(True)
        self.comboBox_fileName.setObjectName(_fromUtf8("comboBox_fileName"))
        self.comboBox_fileName.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_fileName, 0, 1, 1, 4)
        self.checkBox_transparent = QtGui.QCheckBox(Dialog_Export)
        self.checkBox_transparent.setObjectName(_fromUtf8("checkBox_transparent"))
        self.gridLayout_2.addWidget(self.checkBox_transparent, 4, 4, 1, 1)
        self.comboBox_orientation = QtGui.QComboBox(Dialog_Export)
        self.comboBox_orientation.setObjectName(_fromUtf8("comboBox_orientation"))
        self.comboBox_orientation.addItem(_fromUtf8(""))
        self.comboBox_orientation.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_orientation, 4, 1, 1, 1)
        self.pushButton_browse = QtGui.QPushButton(Dialog_Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_browse.sizePolicy().hasHeightForWidth())
        self.pushButton_browse.setSizePolicy(sizePolicy)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.gridLayout_2.addWidget(self.pushButton_browse, 1, 4, 1, 1)
        self.comboBox_directory = QtGui.QComboBox(Dialog_Export)
        self.comboBox_directory.setEditable(True)
        self.comboBox_directory.setObjectName(_fromUtf8("comboBox_directory"))
        self.gridLayout_2.addWidget(self.comboBox_directory, 1, 1, 1, 3)
        self.label_2 = QtGui.QLabel(Dialog_Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.spinBox_dpi = QtGui.QSpinBox(Dialog_Export)
        self.spinBox_dpi.setMinimum(100)
        self.spinBox_dpi.setMaximum(1000)
        self.spinBox_dpi.setProperty("value", 300)
        self.spinBox_dpi.setObjectName(_fromUtf8("spinBox_dpi"))
        self.gridLayout_2.addWidget(self.spinBox_dpi, 4, 3, 1, 1)
        self.comboBox_fileType = QtGui.QComboBox(Dialog_Export)
        self.comboBox_fileType.setObjectName(_fromUtf8("comboBox_fileType"))
        self.gridLayout_2.addWidget(self.comboBox_fileType, 2, 1, 1, 3)

        self.retranslateUi(Dialog_Export)
        self.comboBox_orientation.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Export)
        Dialog_Export.setTabOrder(self.comboBox_fileName, self.comboBox_directory)
        Dialog_Export.setTabOrder(self.comboBox_directory, self.pushButton_browse)
        Dialog_Export.setTabOrder(self.pushButton_browse, self.comboBox_fileType)
        Dialog_Export.setTabOrder(self.comboBox_fileType, self.checkBox_tightBbox)
        Dialog_Export.setTabOrder(self.checkBox_tightBbox, self.comboBox_orientation)
        Dialog_Export.setTabOrder(self.comboBox_orientation, self.spinBox_dpi)
        Dialog_Export.setTabOrder(self.spinBox_dpi, self.checkBox_transparent)
        Dialog_Export.setTabOrder(self.checkBox_transparent, self.pushButton_preview)
        Dialog_Export.setTabOrder(self.pushButton_preview, self.pushButton_export)
        Dialog_Export.setTabOrder(self.pushButton_export, self.pushButton_cancel)

    def retranslateUi(self, Dialog_Export):
        Dialog_Export.setWindowTitle(_translate("Dialog_Export", "Export Image...", None))
        self.pushButton_export.setText(_translate("Dialog_Export", "Export", None))
        self.pushButton_preview.setText(_translate("Dialog_Export", "Preview", None))
        self.pushButton_cancel.setText(_translate("Dialog_Export", "Cancel", None))
        self.checkBox_open_after_export.setText(_translate("Dialog_Export", "Open Image After Export", None))
        self.label_5.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Orientation of the export, currently only available on postscripts</p></body></html>", None))
        self.label_5.setText(_translate("Dialog_Export", "Orientation:", None))
        self.label.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Directory to save the file</p></body></html>", None))
        self.label.setText(_translate("Dialog_Export", "To Directory:", None))
        self.label_4.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>The resolution in dots per inch.</p></body></html>", None))
        self.label_4.setText(_translate("Dialog_Export", "DPI:", None))
        self.label_3.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Format of the exported image</p></body></html>", None))
        self.label_3.setText(_translate("Dialog_Export", "File Type:", None))
        self.checkBox_tightBbox.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Save only the minimum figure area</p></body></html>", None))
        self.checkBox_tightBbox.setText(_translate("Dialog_Export", "Tight Format", None))
        self.comboBox_fileName.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Name of the image file (with or without . format extension)</p></body></html>", None))
        self.comboBox_fileName.setItemText(0, _translate("Dialog_Export", "figure.png", None))
        self.checkBox_transparent.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>make the axes patches transparent; the figure patch will abso be transparent unless facecolor and/or edgecolor are specified in the figure. This is useful, for example, for displaying a plot on top of a colored background.</p></body></html>", None))
        self.checkBox_transparent.setText(_translate("Dialog_Export", "Transparent", None))
        self.comboBox_orientation.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Orientation of the export, currently only available on postscripts</p></body></html>", None))
        self.comboBox_orientation.setItemText(0, _translate("Dialog_Export", "Portrait", None))
        self.comboBox_orientation.setItemText(1, _translate("Dialog_Export", "Landscape", None))
        self.pushButton_browse.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Directory to save the file</p></body></html>", None))
        self.pushButton_browse.setText(_translate("Dialog_Export", "Browse", None))
        self.comboBox_directory.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Directory to save the file</p></body></html>", None))
        self.label_2.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Name of the image file (with or without . format extension)</p></body></html>", None))
        self.label_2.setText(_translate("Dialog_Export", "File Name:", None))
        self.spinBox_dpi.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>The resolution in dots per inch.</p></body></html>", None))
        self.comboBox_fileType.setToolTip(_translate("Dialog_Export", "<html><head/><body><p>Format of the exported image</p></body></html>", None))

