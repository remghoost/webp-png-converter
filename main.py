import os
import subprocess
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Webp to PNG Converter")
        self.setAcceptDrops(True)
        self.setStyleSheet("QMainWindow { background-color: #333333; }")  # set the background color to dark gray

        # Create a label to display the dropped file names
        self.label = QtWidgets.QLabel("Drop webp files here")
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel { background-color: #444444; border: 1px solid gray; padding: 10px; color: white; }")  # set the label's background color to light gray and its text color to white

        # Create a checkbox to enable automatic confirmation of overwrites
        self.overwrite_checkbox = QtWidgets.QCheckBox("Automatically confirm overwrites")
        self.overwrite_checkbox.setChecked(True)
        self.overwrite_checkbox.setStyleSheet("QCheckBox { color: white; }")  # set the checkbox's text color to white

        # Create a layout to hold the label and checkbox
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.overwrite_checkbox)

        # Set the layout as the central widget of the main window
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def dragEnterEvent(self, event):
        # Accept the drag event if a file is being dragged
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Get the file paths of the dropped files
        file_paths = [url.toLocalFile() for url in event.mimeData().urls()]

        # Check if all the files are webp files
        if not all(path.endswith(".webp") for path in file_paths):
            self.label.setText("Error: Not all files are webp files")
            return

        # Convert the webp files to PNG using ffmpeg
        converted_files = []
        for file_path in file_paths:
            file_name, _ = os.path.splitext(os.path.basename(file_path))
            output_path = os.path.join(os.path.dirname(file_path), file_name + "_converted.png")
            command = ["ffmpeg", "-y", "-i", file_path, output_path]  # "-y" flag automatically confirms overwrites
            if not self.overwrite_checkbox.isChecked():
                command.remove("-y")  # remove the "-y
            subprocess.run(command)
            converted_files.append((file_path, output_path))

        # Update the label to show the conversion was successful
        self.label.setText("Successfully converted:\n" + "\n".join("{} to {}".format(input_path, output_path) for input_path, output_path in converted_files))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
