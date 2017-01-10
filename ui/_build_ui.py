
"""
Utility class for build ui files.
This script will just compile all ui files into python class

author: Minu
"""

import os
import sys
import glob

from PyQt5 import uic


def run():

    sys.path.append(os.path.dirname(__file__))

    dirname = os.path.dirname(__file__)
    for root, dirs, files in os.walk(dirname):
        for ui_filename in files:
            if not ui_filename.endswith(".ui"):
                continue

            src_filename = ui_filename.replace(".ui", "")
            src_path = f"{root}/{src_filename}.qrc"
            
            if os.path.exists(src_path):
                os.system(f"pyrcc5 -o {root}/{src_filename}_rc.py {src_path}")

    uic.compileUiDir(
        os.path.dirname(__file__),
        recurse=True
    )

if __name__ == "__main__":
    run()
