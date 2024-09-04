# foam2su2
This Python script takes a simple computational mesh in OpenFoam to a SU2 mesh. 
I assume that you have had all the needed tools to execute Python 3, and the config file in SU2 is already written with respect to the original case in OpenFoam.

Steps:
1. Place the foam2su2.py into the constant/polyMesh folder (which should has the mesh description files right now, if not, run blockMesh first)
2. In command prompt, cd to the said polyMesh folder and run "python foam2su2.py"
3. Copy the mesh.su2 file to the SU2 project folder and check again with SU2_DEF [config_file.cfg]

   Tip: The program supports tetra, prism and hexa mesh.
   Tip 2: You can first check the quality of your mesh in OpenFoam by "checkMesh", also to compare it to your program.
