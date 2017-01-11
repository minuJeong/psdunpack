
"""
Unpack psd format file to png files

dependency:
 - python 3.6 or above
 - PyQt5
 - psd_tools
 - Pillow

read requirements.txt for detailed dependency description

author: minu jeong
"""

import os
import sys

try:
    from PyQt5 import QtWidgets
except:
    print("PyQt5 not found.. installing..")

    from ui import _install_pyqt5
    _install_pyqt5.run()

    from PyQt5 import QtWidgets

    print("PyQt5 installed!")

from src.signal_manager import SignalManager
try:
    from ui import mainwin
except:
    print("ui files not found.. building..")

    from ui import _build_ui
    _build_ui.run()

    from ui import mainwin

    print("ui build done!")

ui_modules = [mainwin]

if not sys.version < '3':
    from imp import reload


def version_check():
    """ make sure ui files are up to date """

    modified_timestamp = os.path.getmtime("ui")
    timestamp_filename = "_timestamp"

    def build():
        print("REBUILDING UI ASSETS..")

        # build
        from ui import _build_ui
        _build_ui.run()

        for module in ui_modules:
            reload(module)

        # write time
        with open(timestamp_filename, "w") as ff:
            ff.write(str(modified_timestamp))

    # compare timestamp
    if os.path.exists(timestamp_filename):
        with open(timestamp_filename, "r") as ff:
            recent_buildtime = ff.read()

        try:
            if float(modified_timestamp) > float(recent_buildtime):
                build()

        except ValueError:
            # handles broken timestamp
            build()
    else:
        build()

version_check()


class Window(mainwin.Ui_MainWindow):
    """ call setupUi """

    def __init__(self, parent):
        self.setupUi(parent)
        SignalManager.init(self)


if __name__ == "__main__":

    application = QtWidgets.QApplication(sys.argv)

    container = QtWidgets.QMainWindow()
    Window(container)
    container.show()

    sys.exit(application.exec())
