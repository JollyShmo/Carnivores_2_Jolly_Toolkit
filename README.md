[-> Download Jolly Toolkit](https://github.com/JollyShmo/Carnivores_2_Jolly_Toolkit/archive/refs/heads/main.zip)

The OBJ VN FIXXER script is for enhancing `.obj` files with vertex normals, the MTL generator script is for creating `.mtl` files, and the TGA to PNG converter script is for converting texture files. Here’s how you can use them in a workflow:

**-> Visit the vg-resource thread: [Visit Here](https://www.vg-resource.com/thread-43064.html) for more info. <-**
## Workflow: Using OBJ VN FIXXER, MTL Generator, and TGA to PNG Converter Scripts

#### Prerequisites:
- **Python Environment:** Ensure Python 3.x is installed on your system.
- **Required Libraries:**
   -> pip install numpy pyfiglet PyQt5 Pillow 

- Download C3Dit -> [Moddb Page](https://www.moddb.com/mods/carnivores-custom-edition/downloads/carnivores-3d-editor-v0099)
#### Scripts Overview:
1. **OBJ VN FIXXER:** Enhances `.obj` files with vertex normals.
2. **MTL Generator:** Creates `.mtl` files with predefined material properties.
3. **TGA to PNG Converter:** Converts TGA texture files to PNG format.

#### Workflow Steps:
1. **Make New Folder `project`**

(Since every skin should be named `Skin.png` this will keep things from breaking.)

2. **Convert `.car` to `.obj` Using C3Dit:**
   - Use C3Dit or any other tool to convert `.car` files to `.obj`.
     
   - Ensure associated `.tga` texture files are exported as well (for MTL generation).

3. **MTL Generation (Using MTL Generator Script):**
   - Run the MTL Generator script to create `.mtl` files with specified material properties.

   - Follow the prompts to select the `.obj` file. The script will generate a corresponding `.mtl` file in the same directory.

4. **TGA to PNG Conversion (Using TGA to PNG Converter Script):**
   - Run the TGA to PNG Converter script to convert a folder and sub folders with TGA texture files to PNG format.

   - Enter the path to the directory containing TGA files. The script will recursively convert all TGA files found to PNG format.

5. **Enhance `.obj` Files with Vertex Normals (Using OBJ VN FIXXER Script):**
   - After generating the `.mtl` files and converting TGA textures to PNG, run the OBJ VN FIXXER script to add vertex normals to your `.obj` file.

   - Enter the path to the `.obj` file when prompted (just file path with no .obj). The script will create a new `.obj` file with `_with_normals` appended to the filename, containing vertex normals.

## **Steps:**
### 1. MTL Generator Script

#### Tree Map:
```
project/
├── models/
│   └── example_model.obj          (Input: .obj file)
│
└── mtl_generator.py               (Script: MTL Generator)
```

#### Example:
- **Start with:** `example_model.obj` (Wavefront OBJ file)
- **End up with:** `example_model.mtl` (Material Template Library file)

#### Workflow:
- **Input:** `example_model.obj`
- **Action:** Run `mtl_generator.py`
- **Output:** `example_model.mtl` (Generated MTL file with predefined material properties)

### 2. TGA to PNG Converter Script

#### Tree Map:
```
project/
├── models/
│   ├── example_model.obj          (Input: .obj file)
│   ├── example_model.mtl          (Generated: .mtl file)
│   ├── texture1.tga               (Input: TGA texture file)
│   └── texture2.tga               (Input: TGA texture file)
│
└── convert_tga_to_png.py          (Script: TGA to PNG Converter)
```

#### Example:
- **Start with:** `texture1.tga`, `texture2.tga` (TGA texture files)
- **End up with:** `texture1.png`, `texture2.png` (Converted PNG texture files)

#### Workflow:
- **Input:** `/path/to/your/project/models/` (Contains TGA texture files)
- **Action:** Run `convert_tga_to_png.py`
- **Output:** `texture1.png`, `texture2.png` (Converted PNG files in the same directory)

### 3. OBJ VN FIXXER Script

#### Tree Map:
```
project/
├── models/
│   ├── example_model.obj          (Input: .obj file)
│   ├── example_model.mtl          (Generated: .mtl file)
│   ├── texture1.tga               (Converted: PNG texture file)
│   ├── texture2.tga               (Converted: PNG texture file)
│   └── example_model_with_normals.obj  (Output: .obj file with vertex normals)
│
└── obj_vn_fixer.py                (Script: OBJ VN FIXXER)
```

#### Example:
- **Start with:** `example_model.obj` (Wavefront OBJ file)
- **End up with:** `example_model_with_normals.obj` (OBJ file with vertex normals)

#### Workflow:
- **Input:** `/path/to/your/project/models/example_model.obj` (Original .obj file)
- **Action:** Run `obj_vn_fixer.py`
- **Output:** `example_model_with_normals.obj` (Enhanced .obj file with vertex normals)

### Summary:
- **MTL Generator:** Generates `.mtl` files from `.obj` files with predefined material properties.
- **TGA to PNG Converter:** Converts TGA texture files to PNG format.
- **OBJ VN FIXXER:** Enhances `.obj` files with vertex normals.

This tree map and example illustrate the workflow and outputs of each script, providing clarity on what you start with and what you achieve after running each script in your project directory. Adjust paths and script inputs based on your specific file structure and project needs.
#### Notes:
- Ensure scripts are executed in the correct order: MTL generation, TGA to PNG conversion, and OBJ enhancement.
- Customize scripts as needed for specific material properties, file paths, or additional features.
- Monitor script outputs for errors or prompts during execution to ensure each step completes successfully.
- ! The model needs to be flipped this can be done through Blender or another 3d editor. 

By following this workflow, you can effectively prepare your `.obj` models with vertex normals and associated `.mtl` and texture files in PNG format, ready for use in 3D rendering applications or games that support Wavefront OBJ format with material definitions. Adjust values in the `mtl` file if needed or import into blender.
