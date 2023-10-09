import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog, QLabel, QDoubleSpinBox
from gen_noisy import generate_noisy

# def extern_function(dataset_file, dc_file, output_file, noisy_percentage):
#     # Esta função será chamada quando o botão for clicado
#     print(f"Dataset File: {dataset_file}")
#     print(f"DC File: {dc_file}")
#     print(f"Output File: {output_file}")
#     print(f"Noisy percentage: {noisy_percentage}")

class FileSelectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generate noisy")
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
        self.dc_button = QPushButton("Select DC (dc)", self)
        self.dc_button.clicked.connect(self.selecionar_dc)
        layout.addWidget(self.dc_button)

        # Create a text box to display the selected DC file path
        self.dc_path_text = QLineEdit(self)
        layout.addWidget(self.dc_path_text)

        # # Create a label for the filename output
        self.filepath_output = QLineEdit(self)
        # Create a button to open the folder selection dialog for saving
        self.save_button = QPushButton("Save as", self)
        self.save_button.clicked.connect(self.selecionar_pasta_e_nome_do_arquivo)
        layout.addWidget(self.save_button)
        
        # # Create a text box for specifying the file path including the filename
        layout.addWidget(self.filepath_output)
        
        # porcentagem_label = QLabel("Porcentagem de Tuplas em Violações:", self)
        # layout.addWidget(porcentagem_label)
        self.porcentagem_input = QDoubleSpinBox(self)
        self.porcentagem_input.setRange(0.0, 100.0)  # Define a faixa de valores permitidos
        layout.addWidget(self.porcentagem_input)

        # Create a button to call extern_function with the selected files
        self.call_function_button = QPushButton("Generate DC violations", self)
        self.call_function_button.clicked.connect(self.chamar_funcao_externa)
        layout.addWidget(self.call_function_button)

        central_widget.setLayout(layout)

    def selecionar_dataset(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Optionally, make the selected file read-only
        dataset_selecionado, _ = QFileDialog.getOpenFileName(self, "Selecionar dataset", "", "CSV Files (*.csv *.xcsv);;All Files (*)", options=options)
        if dataset_selecionado:
            self.dataset_path_text.setText(dataset_selecionado)

    def selecionar_dc(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Optionally, make the selected file read-only
        dc_selecionado, _ = QFileDialog.getOpenFileName(self, "Selecionar DC (.dc)", "", "Text Files (*.dc);;All Files (*)", options=options)
        if dc_selecionado:
            self.dc_path_text.setText(dc_selecionado)

    def selecionar_pasta_e_nome_do_arquivo(self):
        pasta_selecionada, _ = QFileDialog.getSaveFileName(self, "Salvar como", "")
        if pasta_selecionada:
            self.filepath_output.setText(pasta_selecionada)

    def chamar_funcao_externa(self):
        dataset_file = self.dataset_path_text.text()
        dc_file = self.dc_path_text.text()
        output_file = self.filepath_output.text()
        noisy_percentage = self.porcentagem_input.value()
        generate_noisy(dataset_file, dc_file, noisy_percentage, output_file)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_selection_app = FileSelectionApp()
    file_selection_app.show()
    sys.exit(app.exec_())
