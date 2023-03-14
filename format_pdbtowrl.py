print("pdbfile:",end="")
#PDBファイルを取得
pdb_file = input()
import sys
sys.path.append('/opt/homebrew/Cellar/pymol/2.5.0/libexec/lib/python3.11/site-packages')
#PyMOLをCUIで開く
import pymol
pymol.pymol_argv = ['pymol','-c'] 
pymol.finish_launching()
#PDBファイルを読み込む
pymol.cmd.load(pdb_file)
#tentative.wrlとしてエクスポート
pymol.cmd.save("tentative.wrl")
#tentative.wrlのtentativeをインポートしたPDBファイルと同名にする
name = pdb_file[:pdb_file.rfind(".")]
import os
os.rename("tentative.wrl",name+".wrl")