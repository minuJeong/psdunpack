
import sys

from PyQt5.QtWidgets import QWidget

from . import components

if not sys.version < '3':
    from imp import reload

reload(components)


class SignalManager(object):

    @staticmethod
    def init(window):

        def setup_handler(widget_name):
            widget = getattr(window, widget_name)
            try:
                assert isinstance(widget, QWidget)
                getattr(components, widget_name)(widget)
            except:
                return

        # casting list invokes setup_handler
        list(map(setup_handler, dir(window)))
