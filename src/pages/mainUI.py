# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QColumnView, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(948, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.columnView = QColumnView(self.frame)
        self.columnView.setObjectName(u"columnView")

        self.verticalLayout.addWidget(self.columnView)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.import_2 = QPushButton(self.frame_2)
        self.import_2.setObjectName(u"import_2")

        self.horizontalLayout_2.addWidget(self.import_2)

        self.export_2 = QPushButton(self.frame_2)
        self.export_2.setObjectName(u"export_2")

        self.horizontalLayout_2.addWidget(self.export_2)


        self.verticalLayout.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchUpdate = QPushButton(self.frame_5)
        self.searchUpdate.setObjectName(u"searchUpdate")

        self.horizontalLayout_3.addWidget(self.searchUpdate)

        self.upgrade = QPushButton(self.frame_5)
        self.upgrade.setObjectName(u"upgrade")

        self.horizontalLayout_3.addWidget(self.upgrade)


        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)

        self.updateList = QListView(self.frame_4)
        self.updateList.setObjectName(u"updateList")

        self.gridLayout_2.addWidget(self.updateList, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.joinDomain = QCheckBox(self.frame_7)
        self.joinDomain.setObjectName(u"joinDomain")

        self.verticalLayout_3.addWidget(self.joinDomain)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.domainEdit = QLineEdit(self.frame_7)
        self.domainEdit.setObjectName(u"domainEdit")

        self.horizontalLayout_4.addWidget(self.domainEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.hostnameEdit = QLineEdit(self.frame_7)
        self.hostnameEdit.setObjectName(u"hostnameEdit")

        self.horizontalLayout_5.addWidget(self.hostnameEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        self.rdpCheck = QCheckBox(self.frame_6)
        self.rdpCheck.setObjectName(u"rdpCheck")

        self.gridLayout_3.addWidget(self.rdpCheck, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.startScript = QPushButton(self.frame_3)
        self.startScript.setObjectName(u"startScript")

        self.verticalLayout_2.addWidget(self.startScript)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WinStaller", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.import_2.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.searchUpdate.setText(QCoreApplication.translate("MainWindow", u"Search Update", None))
        self.upgrade.setText(QCoreApplication.translate("MainWindow", u"Upgrade", None))
        self.joinDomain.setText(QCoreApplication.translate("MainWindow", u"Join domain", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Domain", None))
#if QT_CONFIG(tooltip)
        self.domainEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Domain to join", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.rdpCheck.setText(QCoreApplication.translate("MainWindow", u"Active Remote Desktop Protocol", None))
        self.startScript.setText(QCoreApplication.translate("MainWindow", u"START", None))
    # retranslateUi

