# タンパク質を対象としたMixed Reallityによる視覚・触覚体験アプリケーション
論文「タンパク質を対象としたMixed Reallityによる視覚・触覚体験アプリケーション」で使用したコードを記載する。

# 概要
PyMOLにおける自動化、Blenderにおける自動化のソースコードを掲載する。

# 使い方
## PyMOLにおけるファイルの変換
```
python format_pdbtowrl.py
```
引数：取得したPDBファイル名
## Blenderにおけるファイルの編集と変換
````
blender --background --python blender_operation.py
````
引数：インポートするファイルのパスとエクスポートした後のファイルのパス

# 環境
- Mac OS
- Python 3.11.1
- PyMOL 2.5.0
- Blender 3.3.0

# 文責
太田悠登