
"""
dependency:
 - psd_tools
 - Pillow

author: minu jeong
"""

import os
import time

try:
    from psd_tools import PSDImage
except ModuleNotFoundError:
    import pip

    pip.main(["install", "psd_tools"])
    from psd_tools import PSDImage

try:
    from PIL import Image
except ModuleNotFoundError:
    import pip

    pip.main(["install", "Pillow"])
    from PIL import Image

from . import SETTINGS


class PSDHandler(object):

    _psd_path = None
    _psd_filename = None

    leaf_layers = None

    def __init__(self, psd_filepath):

        if not psd_filepath.endswith(".psd"):
            return

        if not os.path.exists(psd_filepath):
            return

        print(f"LOADING..{psd_filepath}")

        self.leaf_layers = []

        self._psd_path = os.path.dirname(psd_filepath)
        self._psd_filename = os.path.basename(psd_filepath)

        starttime = time.time()
        psdimage = PSDImage.load(psd_filepath)
        self.recurse_catch_leaves(psdimage)

        print("LOADED IN {} SECONDS".format(time.time() - starttime))

    def recurse_catch_leaves(self, parent_layer):
        for layer in parent_layer.layers:
            if hasattr(layer, "layers"):
                self.recurse_catch_leaves(layer)
            else:
                self.leaf_layers.append(layer)

    def unpack(self):
        dirname = f"{self._psd_path}/{SETTINGS.OUTPUT_DIRECTORY}/{self._psd_filename}"
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        for layer in self.leaf_layers:
            filename = f"{layer.name}.png"
            layer.as_PIL().save(f"{dirname}/{filename}")
