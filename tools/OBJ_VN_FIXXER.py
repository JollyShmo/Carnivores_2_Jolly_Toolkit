# OBJ_VN_FIXXER.py
#
# This script fixes vertex normal data in an OBJ file exported from C3Dit.
# It ensures correct shading by recalculating vertex normals based on face normals.
#
# Usage:
#   1. Run this script.
#   2. When prompted, enter the path to the .obj file exported from C3Dit (without the .obj extension).
#
# Requirements:
#   - Python 3.x
#   - Dependencies: numpy, pyfiglet
#     Install dependencies using: pip install numpy pyfiglet
#
# Author: Jolly Joe
# Date: 10/03/2024
# Version: 1.0

import numpy as np
import re
from pathlib import Path
import pyfiglet as fig

def read_mtl_file(filename):
    mtl_lines = []
    with open(filename, 'r') as mtl_f:
        for line in mtl_f:
            mtl_lines.append(line.strip())
    return mtl_lines

def read_obj_file(filename):
    polygon_name = []
    vertices = []
    texture_vertices = []
    faces = []
    groups = []
    print("->" * 2 + f"Loaded {filename}" + "<-" * 2)
    with open(filename, 'r') as file:
        obj_name_pattern = r'# Name:\s*(.+)|^g\s+(\w+)'
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            
            match = re.search(obj_name_pattern, line, re.IGNORECASE)
            if match:
                name = match.group(2) if match.group(2) else match.group(1)
                polygon_name.append(name.strip())
                print("Name:", name.strip())
            else:
                polygon_name.append('# Name_Goes_Here')
            
            if parts[0] == 'g':
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
                    else:
                        face['texture_vertices'].append(None)  # Handle missing texture indices
                faces.append(face)

    return vertices, texture_vertices, faces, groups, polygon_name

def calculate_vertex_normals(vertices, faces):
    # Initialize vertex normals to zero
    vertex_normals = {i: np.array([0.0, 0.0, 0.0]) for i in range(1, len(vertices) + 1)}

    for face in faces:
        v_indices = face['vertices']
        if len(v_indices) < 3:
            print(f"Skipping degenerate face with vertices: {v_indices}")
            continue  # Skip degenerate faces
        
        # Get the vertices of the face
        v0 = vertices[v_indices[0] - 1]
        v1 = vertices[v_indices[1] - 1]
        v2 = vertices[v_indices[2] - 1]

        # Calculate the face normal using cross product
        edge1 = v1 - v0
        edge2 = v2 - v0
        face_normal = np.cross(edge1, edge2)
        
        # Check for a zero-length face normal
        if np.linalg.norm(face_normal) == 0:
            print(f"Degenerate face found with vertices: {v_indices}, edges: {edge1}, {edge2}")
            continue
        
        face_normal /= np.linalg.norm(face_normal)  # Normalize the face normal

        # Add the face normal to each vertex normal
        for v_idx in v_indices:
            vertex_normals[v_idx] += face_normal

    # Normalize the vertex normals
    for v_idx in vertex_normals:
        if np.linalg.norm(vertex_normals[v_idx]) > 0:
            vertex_normals[v_idx] /= np.linalg.norm(vertex_normals[v_idx])
        else:
            print(f"Warning: Vertex {v_idx} has zero normal after averaging.")

    return vertex_normals

def write_obj_file_with_normals(filename, polygon_names, vertices, texture_vertices, vertex_normals, faces, groups):
    # Extract just the filename and change extension
    future_mtl_file = Path(filename).name.replace('.obj', '.mtl')
    with open(filename, 'w') as file:
        file.write("#  OBJ VN FIXXER\n#  Created by Jolly Joe\n")
        file.write(f"mtllib {future_mtl_file}\n")
        
        # Use the first non-default polygon name
        valid_polygon_name = next((name for name in polygon_names if name != "# Name_Goes_Here"), "Unnamed")
        file.write(f"o {valid_polygon_name}\n")
        
        # Write vertices (v)
        for vertex in vertices:
            file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
        
        # Write texture vertices (vt)
        for texture_vertex in texture_vertices:
            file.write(f"vt {texture_vertex[0]} {texture_vertex[1]}\n")
        
        # Write vertex normals (vn)
        for v_idx, vn in vertex_normals.items():
            file.write(f"vn {vn[0]} {vn[1]} {vn[2]}\n")
        
        # Handle groups and materials
        if groups:
            file.write(f"g {groups[0]}\n")  # Using the first group for now
        file.write("usemtl Dino_Skin\n")
        
        # Write faces (f)
        file.write("s 1\n")
        for face in faces:
            v_indices = face['vertices']
            vt_indices = face['texture_vertices']
            file.write("f")
            for i in range(len(v_indices)):
                if vt_indices[i] is not None:
                    file.write(f" {v_indices[i]}/{vt_indices[i]}/{v_indices[i]}")
                else:
                    file.write(f" {v_indices[i]}//{v_indices[i]}")  # No texture coordinates
            file.write("\n")

def main():
    title_prog = fig.figlet_format("VN FIXXER", font='coinstak')
    print(title_prog, "by Jolly Joe\n\n","This is to aid in fixing UV data if None are present.\n Enter the location of the Obj file\n to calculate the vn data\n(DON'T include the .obj)")
    bad_vn_obj_file = input("->")
    input_obj_file = f'{bad_vn_obj_file}.obj'
    output_obj_file = f'{bad_vn_obj_file}_with_normals.obj'

    try:
        # Step 1: Read and parse the OBJ file
        vertices, texture_vertices, faces, groups, polygon_names = read_obj_file(input_obj_file)

        # Step 2: Calculate vertex normals
        vertex_normals = calculate_vertex_normals(vertices, faces)

        # Step 3: Write OBJ file with vertex normals
        write_obj_file_with_normals(output_obj_file, polygon_names, vertices, texture_vertices, vertex_normals, faces, groups)
        print(f"OBJ file with vertex normals saved as {output_obj_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_obj_file} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
