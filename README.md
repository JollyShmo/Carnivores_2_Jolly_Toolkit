The OBJ VN FIXXER script is for enhancing `.obj` files with vertex normals, the MTL generator script is for creating `.mtl` files, and the TGA to PNG converter script is for converting texture files. Here’s how you can use them in a workflow:

### Workflow: Using OBJ VN FIXXER, MTL Generator, and TGA to PNG Converter Scripts
Locate the `.car` file you want -> 

Export `.obj` (using C3Dit) + `.tga` -> 

`mtl` (MTL Genterator) -> 

convert `.tga` to `.png` (TGA to PNG Converter) ->

`.obj` (OBJ VN FIXXER) -> Finished!


#### Prerequisites:
- **Python Environment:** Ensure Python 3.x is installed on your system.
- **Required Libraries:** Install necessary libraries such as NumPy (for OBJ VN FIXXER) and Pillow (for TGA to PNG converter).

#### Scripts Overview:
1. **OBJ VN FIXXER:** Enhances `.obj` files with vertex normals.
2. **MTL Generator:** Creates `.mtl` files with predefined material properties.
3. **TGA to PNG Converter:** Converts TGA texture files to PNG format.

#### Workflow Steps:
1. **Make New Folder `project`**

(Since every skin should be named `Skin.png` this will keep things from breaking.)

2. **Convert `.car` to `.obj` Using C3Dit:**
   - Use C3Dit or any other tool to convert `.car` files to `.obj`.
   - Ensure associated `.tga` texture files are exported or created separately (for MTL generation).

3. **MTL Generation (Using MTL Generator Script):**
   - Run the MTL Generator script to create `.mtl` files with specified material properties.
     ```bash
     python mtl_generator.py
     ```
   - Follow the prompts to select the `.obj` file. The script will generate a corresponding `.mtl` file in the same directory.

4. **TGA to PNG Conversion (Using TGA to PNG Converter Script):**
   - Run the TGA to PNG Converter script to convert a folder and sub folders with TGA texture files to PNG format.
     ```bash
     python convert_tga_to_png.py
     ```
   - Enter the path to the directory containing TGA files. The script will recursively convert all TGA files found to PNG format.

5. **Enhance `.obj` Files with Vertex Normals (Using OBJ VN FIXXER Script):**
   - After generating the `.mtl` files and converting TGA textures to PNG, run the OBJ VN FIXXER script to add vertex normals to your `.obj` file.
     ```bash
     python obj_vn_fixer.py
     ```
   - Enter the path to the `.obj` file when prompted (just file path with no .obj). The script will create a new `.obj` file with `_with_normals` appended to the filename, containing vertex normals.

#### Example Workflow:

Suppose you have the following directory structure and files:

```
project/
│
├── models/
│   ├── example_model.obj
│   ├── example_model.mtl
│   ├── texture1.tga
│   └── texture2.tga
│
├── mtl_generator.py
├── convert_tga_to_png.py
└── obj_vn_fixer.py
```

- **Steps:**
   1. **Run MTL Generator:**
      - Execute `python mtl_generator.py`.
      - Select `example_model.obj` when prompted. This creates `example_model.mtl` with specified material properties (`Dino_Skin`).

   2. **Convert TGA to PNG:**
      - Execute `python convert_tga_to_png.py`.
      - Enter `/path/to/your/project/models` when prompted. This converts `texture1.tga` and `texture2.tga` to `texture1.png` and `texture2.png`.

   3. **Enhance OBJ with Vertex Normals:**
      - Execute `python obj_vn_fixer.py`.
      - Enter `/path/to/your/project/models/example_model.obj` when prompted. This generates `example_model_with_normals.obj` with vertex normals.

#### Notes:
- Ensure scripts are executed in the correct order: MTL generation, TGA to PNG conversion, and OBJ enhancement.
- Customize scripts as needed for specific material properties, file paths, or additional features.
- Monitor script outputs for errors or prompts during execution to ensure each step completes successfully.
- ! The model needs to be flipped this can be done through Blender or another 3d editor. 

By following this workflow, you can effectively prepare your `.obj` models with vertex normals and associated `.mtl` and texture files in PNG format, ready for use in 3D rendering applications or games that support Wavefront OBJ format with material definitions. Adjust values in the `mtl` file if needed or import into blender.
