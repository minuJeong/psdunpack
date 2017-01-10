
import os

from psd_tools import PSDImage


class PSDHandler(object):

    leaf_layers = []

    def __init__(self, psd_filepath):

        if not psd_filepath.endswith(".psd"):
            return

        if not os.path.exists(psd_filepath):
            return

        print(f"LOADING..{psd_filepath}")

        psdimage = PSDImage.load(psd_filepath)
        self.recurse(psdimage)

    def recurse(self, parent_layer):
        for layer in parent_layer.layers:
            if layer.hasattr("layers"):
                self.recurse(layer)
            else:
                leaf_layers.append(layer)
