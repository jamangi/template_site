# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

from pathlib import Path
import webbrowser

filename = Path("index.html")

webbrowser.open(filename.absolute().as_uri())
