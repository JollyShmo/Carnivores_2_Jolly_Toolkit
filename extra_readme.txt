/By Jolly Joe/
\_ Carnivores 2 Extracting Models__/
Hello and welcome to my journey into extracting files from Carnivores 2.
I found some tools and ended up making a few of my own tools as well.
This will give you the steps I take in extracting the models from the game.
_______________
\_/\ Issues /\_/
Some issues I am dealing with texture transparency for blacked out parts like
making in between the teeth transparent, the game uses 'flags' which
work on the face level of the mesh. It doesn't help that
the texture colors are a little wonky (black shades are all over,
it doesn't have an alpha channel). I made other tools that make the
color black an alpha channel that only gave holes throughout the texture of the model.
____________
\__ Models __/
All Dinosaurs
Hunter
Dropship
Weapons
______________
\__ Workflow __/
The tools I use are as followed to get the mesh objects from the `.car` files under `/carnivors2/HUNTDAT/`.
First thing is to use a beta tool C3Dit_v0-0-99-5 (*The updated version on github doesn't work).
 ___________
\__ Prep __/
Make a folder to work in (i.e. Project/model) in the folder `model`
and place the copy of the `.car` file you want to work on.
_____________
\___ C3Dit __/
File > Open (select the .car file)
Data > Export Model (save as .obj file)
Data > Export Texture (save as .tga file)
Exit
 ___________________
\___ OBJ VN FIXXER __/
Run `OBJ_VN_FIXXER.py`
Enter the .obj file path from C3D (don't include the .obj)
 ____________________
\___ Dino MTL Maker ___/
Run `dino_mtl_maker.py`
Select Generate MTL
Select the .obj file with ending in `_with_normals.obj`
Exit
 _________________
\___ TGA-2-PNG ___/
Run `tga_2_png.py`
Enter the project folder (will go through subfolders as well)
Now you can fix the rotation by importing it into blender.
 _____________________________
\__ Blender - Obj Import Settings __/
Add these changes to improve the orientation of the object. Keep the rest the same (save the settings to use again later)
Forward Axis: -X
Split by Object ☑
__________________
\_ **Finished** _/
Now you can export to other file types and mod it any way you like. 
The python tools I made myself message me if you want to collaborate or talk shop. 
I have another part that will be the tools I made to extract the animation data. 
\->To Be Continued.../
