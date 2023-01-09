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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_widget_NHP(object):
    def setupUi(self, widget_NHP):
        if not widget_NHP.objectName():
            widget_NHP.setObjectName(u"widget_NHP")
        widget_NHP.resize(640, 320)
        self.layoutWidget = QWidget(widget_NHP)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 10, 621, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_noordhoekpathfinder = QLabel(self.layoutWidget)
        self.label_noordhoekpathfinder.setObjectName(u"label_noordhoekpathfinder")
        self.label_noordhoekpathfinder.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(36)
        self.label_noordhoekpathfinder.setFont(font)
        self.label_noordhoekpathfinder.setLayoutDirection(Qt.LeftToRight)
        self.label_noordhoekpathfinder.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_noordhoekpathfinder)

        self.horizontalLayout_uk = QHBoxLayout()
        self.horizontalLayout_uk.setObjectName(u"horizontalLayout_uk")
        self.label_UKcrewlist = QLabel(self.layoutWidget)
        self.label_UKcrewlist.setObjectName(u"label_UKcrewlist")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_UKcrewlist.sizePolicy().hasHeightForWidth())
        self.label_UKcrewlist.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(20)
        self.label_UKcrewlist.setFont(font1)
        self.label_UKcrewlist.setMargin(10)

        self.horizontalLayout_uk.addWidget(self.label_UKcrewlist)

        self.pushButton_copyUKcrewlist = QPushButton(self.layoutWidget)
        self.pushButton_copyUKcrewlist.setObjectName(u"pushButton_copyUKcrewlist")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_copyUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_copyUKcrewlist.setSizePolicy(sizePolicy1)

        self.horizontalLayout_uk.addWidget(self.pushButton_copyUKcrewlist)

        self.pushButton_createUKcrewlist = QPushButton(self.layoutWidget)
        self.pushButton_createUKcrewlist.setObjectName(u"pushButton_createUKcrewlist")
        sizePolicy1.setHeightForWidth(self.pushButton_createUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_createUKcrewlist.setSizePolicy(sizePolicy1)

        self.horizontalLayout_uk.addWidget(self.pushButton_createUKcrewlist)

        self.pushButton_infoUKcrewlist = QPushButton(self.layoutWidget)
        self.pushButton_infoUKcrewlist.setObjectName(u"pushButton_infoUKcrewlist")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_infoUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_infoUKcrewlist.setSizePolicy(sizePolicy2)

        self.horizontalLayout_uk.addWidget(self.pushButton_infoUKcrewlist)


        self.verticalLayout.addLayout(self.horizontalLayout_uk)

        self.horizontalLayout_nl = QHBoxLayout()
        self.horizontalLayout_nl.setObjectName(u"horizontalLayout_nl")
        self.label_NLcrewlist = QLabel(self.layoutWidget)
        self.label_NLcrewlist.setObjectName(u"label_NLcrewlist")
        sizePolicy.setHeightForWidth(self.label_NLcrewlist.sizePolicy().hasHeightForWidth())
        self.label_NLcrewlist.setSizePolicy(sizePolicy)
        self.label_NLcrewlist.setFont(font1)

        self.horizontalLayout_nl.addWidget(self.label_NLcrewlist)

        self.pushButton_arrivalNL = QPushButton(self.layoutWidget)
        self.pushButton_arrivalNL.setObjectName(u"pushButton_arrivalNL")
        sizePolicy1.setHeightForWidth(self.pushButton_arrivalNL.sizePolicy().hasHeightForWidth())
        self.pushButton_arrivalNL.setSizePolicy(sizePolicy1)

        self.horizontalLayout_nl.addWidget(self.pushButton_arrivalNL)

        self.pushButton_departureNL = QPushButton(self.layoutWidget)
        self.pushButton_departureNL.setObjectName(u"pushButton_departureNL")
        sizePolicy1.setHeightForWidth(self.pushButton_departureNL.sizePolicy().hasHeightForWidth())
        self.pushButton_departureNL.setSizePolicy(sizePolicy1)

        self.horizontalLayout_nl.addWidget(self.pushButton_departureNL)

        self.pushButton_createNL = QPushButton(self.layoutWidget)
        self.pushButton_createNL.setObjectName(u"pushButton_createNL")
        sizePolicy1.setHeightForWidth(self.pushButton_createNL.sizePolicy().hasHeightForWidth())
        self.pushButton_createNL.setSizePolicy(sizePolicy1)

        self.horizontalLayout_nl.addWidget(self.pushButton_createNL)

        self.pushButton_infoNL = QPushButton(self.layoutWidget)
        self.pushButton_infoNL.setObjectName(u"pushButton_infoNL")
        sizePolicy2.setHeightForWidth(self.pushButton_infoNL.sizePolicy().hasHeightForWidth())
        self.pushButton_infoNL.setSizePolicy(sizePolicy2)

        self.horizontalLayout_nl.addWidget(self.pushButton_infoNL)


        self.verticalLayout.addLayout(self.horizontalLayout_nl)

        self.horizontalLayout_rhts = QHBoxLayout()
        self.horizontalLayout_rhts.setObjectName(u"horizontalLayout_rhts")
        self.label_resthours_and_timesheets = QLabel(self.layoutWidget)
        self.label_resthours_and_timesheets.setObjectName(u"label_resthours_and_timesheets")
        sizePolicy.setHeightForWidth(self.label_resthours_and_timesheets.sizePolicy().hasHeightForWidth())
        self.label_resthours_and_timesheets.setSizePolicy(sizePolicy)
        self.label_resthours_and_timesheets.setFont(font1)

        self.horizontalLayout_rhts.addWidget(self.label_resthours_and_timesheets)

        self.pushButton_generate_resthours = QPushButton(self.layoutWidget)
        self.pushButton_generate_resthours.setObjectName(u"pushButton_generate_resthours")
        sizePolicy1.setHeightForWidth(self.pushButton_generate_resthours.sizePolicy().hasHeightForWidth())
        self.pushButton_generate_resthours.setSizePolicy(sizePolicy1)

        self.horizontalLayout_rhts.addWidget(self.pushButton_generate_resthours)

        self.pushButton_info_resthours = QPushButton(self.layoutWidget)
        self.pushButton_info_resthours.setObjectName(u"pushButton_info_resthours")

        self.horizontalLayout_rhts.addWidget(self.pushButton_info_resthours)


        self.verticalLayout.addLayout(self.horizontalLayout_rhts)


        self.retranslateUi(widget_NHP)

        QMetaObject.connectSlotsByName(widget_NHP)
    # setupUi

    def retranslateUi(self, widget_NHP):
        widget_NHP.setWindowTitle(QCoreApplication.translate("widget_NHP", u"Form", None))
        self.label_noordhoekpathfinder.setText(QCoreApplication.translate("widget_NHP", u"Noorhoek Pathfinder", None))
        self.label_UKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"UK crew list:", None))
        self.pushButton_copyUKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"Select NHP format crewlist", None))
        self.pushButton_createUKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"Create an UK crewlist", None))
        self.pushButton_infoUKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
        self.label_NLcrewlist.setText(QCoreApplication.translate("widget_NHP", u"NL crew list:", None))
        self.pushButton_arrivalNL.setText(QCoreApplication.translate("widget_NHP", u"Arrival crew list", None))
        self.pushButton_departureNL.setText(QCoreApplication.translate("widget_NHP", u"Departure crew list", None))
        self.pushButton_createNL.setText(QCoreApplication.translate("widget_NHP", u"Create a NL crew list", None))
        self.pushButton_infoNL.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
        self.label_resthours_and_timesheets.setText(QCoreApplication.translate("widget_NHP", u"Resthours and timesheets:", None))
        self.pushButton_generate_resthours.setText(QCoreApplication.translate("widget_NHP", u"Generate sheets", None))
        self.pushButton_info_resthours.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
    # retranslateUi

