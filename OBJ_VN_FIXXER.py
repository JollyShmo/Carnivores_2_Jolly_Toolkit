import numpy as np
import re
def read_mtl_file(filename):
    mtl_name = []
    with open(filename, 'r') as mtl_f:
        for line in mtl_f:
            mtl_line = line.split()
            print(mtl_line)
    return mtl_line

def read_obj_file(filename):
    polygon_name = []
    vertices = []
    texture_vertices = []
    faces = []
    groups = []
    print("->" * 2 + f"Loaded {filename}" + "<-" * 2)
    with open(filename, 'r') as file:
        obj_name_pattern = r'# Name:\s*(.+)'
        for line in file:
            parts = line.strip().split()
            
            if not parts:
                continue
            match = re.search(obj_name_pattern, line, re.IGNORECASE)  # Case insensitive search
            if match:
                name = match.group(1)  # Capture the name
                poly_name = name.strip()
                polygon_name.append(str(poly_name))
            elif parts[0] == 'g':
                groups.append(str(parts[1]))
            elif parts[0] == 'v':
                vertices.append(np.array([float(parts[1]), float(parts[2]), float(parts[3])]))
            elif parts[0] == 'vt':
                texture_vertices.append(np.array([float(parts[1]), float(parts[2])]))
            elif parts[0] == 'f':
                face = {'vertices': [], 'texture_vertices': []}
                for part in parts[1:]:
                    indices = part.split('/')
                    v_idx = int(indices[0])
                    face['vertices'].append(v_idx)
                    if len(indices) > 1 and indices[1]:
                        vt_idx = int(indices[1])
                        face['texture_vertices'].append(vt_idx)
                faces.append(face)
            else:
                print("None - Check the Files")
                return
    return vertices, texture_vertices, faces, groups, polygon_name

def calculate_vertex_normals(vertices, faces):
    vertex_normals = {i: np.array([0.0, 0.0, 0.0]) for i in range(1, len(vertices) + 1)}

    for face in faces:
        v_indices = face['vertices']
        if len(v_indices) < 3:
            continue

        v0 = vertices[v_indices[0] - 1]
        v1 = vertices[v_indices[1] - 1]
        v2 = vertices[v_indices[2] - 1]
        face_normal = np.cross(v1 - v0, v2 - v0)
        face_normal /= np.linalg.norm(face_normal)

        for v_idx in v_indices:
            vertex_normals[v_idx] += face_normal

    for v_idx in vertex_normals:
        if np.linalg.norm(vertex_normals[v_idx]) > 0:
            vertex_normals[v_idx] /= np.linalg.norm(vertex_normals[v_idx])

    return vertex_normals

def write_obj_file_with_normals(filename, polygon_name, vertices, texture_vertices, vertex_normals, faces, groups):
    future_mtl_file = filename.replace('obj','mtl').split('/')
    print(future_mtl_file[1])
    with open(filename, 'w') as file:
        file.write("#  OBJ VN FIXXER\n#  Created by Jolly Joe\n")
        file.write("\n")
        
        file.write(F"mtllib {future_mtl_file[1]}\n")
       
        file.write(f"o {polygon_name[0]}\n")
        # Write vertices (v)
        for vertex in vertices:
            file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
        
        # Write texture vertices (vt)
        for texture_vertex in texture_vertices:
            file.write(f"vt {texture_vertex[0]} {texture_vertex[1]}\n")
        
        # Write vertex normals (vn)
        for v_idx, vn in vertex_normals.items():
            file.write(f"vn {vn[0]} {vn[1]} {vn[2]}\n")
        #FIXME only works with the first group!!
        file.write(f"g {groups[0]}\n")
        file.write("usemtl Dino_Skin\n")
        # Write faces (f)
        file.write("s 1\n")
        for face in faces:
            v_indices = face['vertices']
            vt_indices = face['texture_vertices']
            file.write("f")
            for i in range(len(v_indices)):
                file.write(f" {v_indices[i]}/{vt_indices[i]}/{v_indices[i]}")
            file.write("\n")

def main():
    bad_vn_obj_file = input("Enter the location of the Obj file\nto calculate the vn data\n(do not include the .obj):\n|->")
    input_obj_file = f'{bad_vn_obj_file}.obj'
    output_obj_file = f'{bad_vn_obj_file}_with_normals.obj'

    # Step 1: Read and parse the OBJ file
    vertices, texture_vertices, faces, groups, polygon_name = read_obj_file(input_obj_file)

    # Step 2: Calculate vertex normals
    vertex_normals = calculate_vertex_normals(vertices, faces)

    # Step 3: Write OBJ file with vertex normals
    write_obj_file_with_normals(output_obj_file, polygon_name, vertices, texture_vertices, vertex_normals, faces, groups)
    print(f"OBJ file with vertex normals saved as {output_obj_file}")

if __name__ == '__main__':
    main()
