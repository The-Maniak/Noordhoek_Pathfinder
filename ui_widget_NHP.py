# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget_NHP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget)


class Ui_Widget_NHP(object):
    def setupUi(self, widget_NHP):
        if not widget_NHP.objectName():
            widget_NHP.setObjectName(u"widget_NHP")
        widget_NHP.resize(580, 297)
        self.widget = QWidget(widget_NHP)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 548, 33))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_UKcrewlist = QLabel(self.widget)
        self.label_UKcrewlist.setObjectName(u"label_UKcrewlist")
        self.label_UKcrewlist.setMargin(10)

        self.horizontalLayout.addWidget(self.label_UKcrewlist)

        self.lineEdit_UKcrewlist = QLineEdit(self.widget)
        self.lineEdit_UKcrewlist.setObjectName(u"lineEdit_UKcrewlist")
        self.lineEdit_UKcrewlist.setEnabled(True)
        self.lineEdit_UKcrewlist.setMinimumSize(QSize(250, 0))
        self.lineEdit_UKcrewlist.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_UKcrewlist)

        self.pushButton_copyUKcrewlist = QPushButton(self.widget)
        self.pushButton_copyUKcrewlist.setObjectName(u"pushButton_copyUKcrewlist")

        self.horizontalLayout.addWidget(self.pushButton_copyUKcrewlist)

        self.pushButton_createUKcrewlist = QPushButton(self.widget)
        self.pushButton_createUKcrewlist.setObjectName(u"pushButton_createUKcrewlist")

        self.horizontalLayout.addWidget(self.pushButton_createUKcrewlist)

        self.retranslateUi(widget_NHP)

        QMetaObject.connectSlotsByName(widget_NHP)

    # setupUi

    def retranslateUi(self, widget_NHP):
        widget_NHP.setWindowTitle(QCoreApplication.translate("widget_NHP", u"Form", None))
        self.label_UKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"UK crewlist", None))
        self.lineEdit_UKcrewlist.setText("")
        self.lineEdit_UKcrewlist.setPlaceholderText(
            QCoreApplication.translate("widget_NHP", u"Paste in the destination vessels crewlist", None))
        self.pushButton_copyUKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"Copy the NHP crewlist", None))
        self.pushButton_createUKcrewlist.setText(
            QCoreApplication.translate("widget_NHP", u"Create an UK crewlist", None))
    # retranslateUi
