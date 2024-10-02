import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog

class MtlGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MTL File Generator')
        self.setGeometry(100, 100, 400, 200)

        self.file_label = QLabel('No OBJ file selected.')
        self.generate_button = QPushButton('Generate MTL')
        self.generate_button.clicked.connect(self.generate_mtl)

        vbox = QVBoxLayout()
        vbox.addWidget(self.file_label)
        vbox.addWidget(self.generate_button)

        self.setLayout(vbox)

    def generate_mtl(self):
        obj_filename, _ = QFileDialog.getOpenFileName(self, 'Select OBJ File', '.', 'OBJ Files (*.obj)')
        
        if obj_filename:
            base_name = os.path.splitext(os.path.basename(obj_filename))[0]
            mtl_filename = f"{base_name}.mtl"

            material_name = "Dino_Skin"
            ambient_color = "0.2 0.2 0.2"
            diffuse_color = "1.0 1.0 1.0"
            specular_color = "0.0 0.0 0.0"
            shininess = "0.0"
            texture_filename = "Skin.png"

            mtl_content = f"# MTL file generated for {base_name}\n\n"
            mtl_content += f"newmtl {material_name}\n"
            mtl_content += f"Ka {ambient_color}  # Ambient color\n"
            mtl_content += f"Kd {diffuse_color}  # Diffuse color\n"
            mtl_content += f"Ks {specular_color}  # Specular color\n"
            mtl_content += f"d 1.0\n"  # Dissolve (fully opaque)
            mtl_content += f"Ns {shininess}  # Shininess\n"
            mtl_content += f"illum 2\n\n"
            mtl_content += f"map_Kd {texture_filename}\n"
            mtl_content += "# Thank you for using =)\n"

            with open(mtl_filename, 'w') as mtl_file:
                mtl_file.write(mtl_content)

            self.file_label.setText(f'MTL file "{mtl_filename}" generated.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MtlGenerator()
    window.show()
    sys.exit(app.exec_())
