import os
import shutil
from PySide6.QtCore import Qt, QProcess, QUrl
from PySide6.QtWidgets import QWidget, QFileDialog
from ui_widget_NHP import Ui_widget_NHP


class Widget_NHP(QWidget, Ui_widget_NHP):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Noordhoek Pathfinder - unofficial app')

        # NL port docs associated buttons:
        self.pushButton_arrivalNL.clicked.connect(lambda: self.copy_crewlist(
            r"NHP_apps\nl_ports_crewlist_project\vessel-format-crewlist\arrival"))

        self.pushButton_departureNL.clicked.connect(lambda: self.copy_crewlist(
            r"NHP_apps\nl_ports_crewlist_project\vessel-format-crewlist\departure"))
        self.pushButton_createNL.clicked.connect(self.create_nl_crewlist)

        # UK port docs associated buttons:
        self.pushButton_copyUKcrewlist.clicked.connect(lambda: self.copy_crewlist(
            r"NHP_apps\uk_ports_crewlist_project\current-crewlist"))
        self.pushButton_createUKcrewlist.clicked.connect(self.create_uk_crewlist)
        self.process = QProcess()
        self.process.finished.connect(self.process_finished)

    def copy_crewlist(self, destination_folder):
        destination_directory = os.path.join(os.getcwd(), destination_folder)
        shutil.rmtree(destination_directory, ignore_errors=True)
        os.makedirs(destination_directory, exist_ok=True)
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_url, _ = QFileDialog.getOpenFileUrl(self, "Select file to copy", QUrl(),
                                                 "All Files (*);;Excel Files (*.xlsx)", options=options)
        if not file_url.isValid():
            # User cancelled the file selection dialog
            return
        file_path = file_url.toLocalFile()
        shutil.copy(file_path, destination_directory)

    def create_uk_crewlist(self):
        self.process.start("python",
                           [r"C:\Users\wojte\Desktop\python_projects\Noordhoek_Pathfinder\NHP_apps\uk_ports_crewlist_project\main.py"])

    def create_nl_crewlist(self):
        self.process.execute("python",
                             [r"C:\Users\wojte\Desktop\python_projects\Noordhoek_Pathfinder\NHP_apps\nl_ports_crewlist_project\main.py"])
        # if self.process.errorOccurred():
        #     print(self.process.errorString())
        self.process.waitForStarted()
        print('start nl crewlist')
        self.process.waitForFinished()
        print('finished nl crewlist')
        print(self.process.exitStatus())
    # def handle_error(self):
    #     error = self.process.error()
    #     error_string = self.process.errorString()
    #     print(f'An error occurred: {error} - {error_string}')

    def process_finished(self):
        if self.process.exitStatus() != QProcess.NormalExit:
            print(f'An error occurred while running the script. {self.process.exitStatus}')
        else:
            print('Job done. Time to relax...')
