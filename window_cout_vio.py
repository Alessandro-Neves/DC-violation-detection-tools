import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog, QLabel, QDoubleSpinBox
from count_violations import count_violations

class FileSelectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Detect violations")
        self.setGeometry(100, 100, 800, 400)  # Defina a largura e altura da janela aqui
        self.init_ui()

    def init_ui(self):
        # Create a central widget to contain the widgets
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout to organize the widgets
        layout = QVBoxLayout()

        # Create a button to open the dataset file selection dialog
        self.dataset_button = QPushButton("Select dataset (csv)", self)
        self.dataset_button.clicked.connect(self.selecionar_dataset)
        layout.addWidget(self.dataset_button)

        # Create a text box to display the selected dataset file path
        self.dataset_path_text = QLineEdit(self)
        layout.addWidget(self.dataset_path_text)

        # Create a button to open the DC file selection dialog
        self.dc_button = QPushButton("Select DC (txt)", self)
        self.dc_button.clicked.connect(self.selecionar_dc)
        layout.addWidget(self.dc_button)

        # Create a text box to display the selected DC file path
        self.dc_path_text = QLineEdit(self)
        layout.addWidget(self.dc_path_text)

        # Create a button to call extern_function with the selected files
        self.call_function_button = QPushButton("Detect violations", self)
        self.call_function_button.clicked.connect(self.chamar_funcao_externa)
        layout.addWidget(self.call_function_button)

        central_widget.setLayout(layout)

    def selecionar_dataset(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Optionally, make the selected file read-only
        dataset_selecionado, _ = QFileDialog.getOpenFileName(self, "Select dataset", "", "CSV Files (*.csv *.xcsv);;All Files (*)", options=options)
        if dataset_selecionado:
            self.dataset_path_text.setText(dataset_selecionado)

    def selecionar_dc(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Optionally, make the selected file read-only
        dc_selecionado, _ = QFileDialog.getOpenFileName(self, "Select DC", "", "Text Files (*.txt);;All Files (*)", options=options)
        if dc_selecionado:
            self.dc_path_text.setText(dc_selecionado)

    def chamar_funcao_externa(self):
        dataset_file = self.dataset_path_text.text()
        dc_file = self.dc_path_text.text()
        self.close()
        count_violations(dataset_file, dc_file)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_selection_app = FileSelectionApp()
    file_selection_app.show()
    sys.exit(app.exec_())
