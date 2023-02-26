print("pdbfile:",end="")
pdb_file = input()
import sys
sys.path.append('/opt/homebrew/Cellar/pymol/2.5.0/libexec/lib/python3.11/site-packages')
import pymol
pymol.pymol_argv = ['pymol','-c'] 
pymol.finish_launching()
pymol.cmd.load(pdb_file)
pymol.cmd.save("tentative.wrl")
pdb_id = pdb_file[0:4]
import os
os.rename("tentative.wrl",pdb_id+".wrl")