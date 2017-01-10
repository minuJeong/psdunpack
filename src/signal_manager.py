
import sys

from PyQt5.QtWidgets import QWidget

from . import components

if not sys.version < '3':
    from imp import reload

reload(components)


class SignalManager(object):

    @staticmethod
    def init(window):
        valid_handlers = []

        def setup_handler(widget_name):
            """ replace of lambda """

            widget = getattr(window, widget_name)

            if not isinstance(widget, QWidget):
                return

            if not hasattr(components, widget_name):
                return

            valid_handlers.append(
                getattr(components, widget_name)(widget, widget_name)
            )

        for widget_name in dir(window):
            setup_handler(widget_name)

        for widget_handler in valid_handlers:
            widget_handler.start()
