import os
import shutil
from PySide6.QtCore import Qt, QProcess
from PySide6.QtWidgets import QWidget
from ui_widget_NHP import Ui_Widget_NHP


class Widget_NHP(QWidget, Ui_Widget_NHP):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Noordhoek Pathfinder - unofficial app')
        self.pushButton_copyUKcrewlist.clicked.connect(self.copy_crewlist)
        self.pushButton_createUKcrewlist.clicked.connect(self.create_uk_crewlist)
        self.process = QProcess()
        self.process.finished.connect(self.uk_crewlist_finished)

    def copy_crewlist(self):
        current_location = os.getcwd()
        destination_subfolder = r'Noordhoek-Pathfinder\UK ports crewlist project\current crewlist'
        destination_directory = os.path.join(current_location, destination_subfolder)
        for root, dirs, files in os.walk(destination_directory):
            for f in files:
                os.unlink(os.path.join(root, f))
        crewlist_to_convert = self.lineEdit_UKcrewlist.text()
        shutil.copy(crewlist_to_convert, destination_directory)

    def create_uk_crewlist(self):
        self.process.start("python", [r"C:\Users\wojte\Desktop\python_projects\Noordhoek_Pathfinder\Noordhoek-Pathfinder\UK ports crewlist project/main.py"])

    def uk_crewlist_finished(self):
        print('Creation of UK crewlist successful!')
