
"""
Defines ui interactions
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtBoundSignal

from . import psd_handle


class EventDispatcher(object):

    _eventmapping = {}

    def add_event_listener(self, eventkey, callback):
        if eventkey not in self._eventmapping:
            self._eventmapping[eventkey] = []
        self._eventmapping[eventkey].append(self._eventmapping[eventkey])

    def remove_event_listener(self, eventkey, callback):
        if eventkey not in self._eventmapping:
            return

        if callback not in self._eventmapping[eventkey]:
            return

        self._eventmapping[eventkey].remove(callback)

    def dispatch_event(self, eventkey):
        if eventkey not in self._eventmapping:
            return

        for callback in self._eventmapping[eventkey]:
            callback()


class BaseComponent(EventDispatcher):
    """ Connect signals using reflection """

    widget = None
    triggers = None

    def start(self):
        """ override this and define initialization """
        pass

    def __init__(self, widget):
        assert isinstance(widget, QWidget)

        self.widget = widget
        self.triggers = []

        for signal_name in dir(widget):
            signal = getattr(widget, signal_name)

            if not isinstance(signal, pyqtBoundSignal):
                continue

            if hasattr(self, signal_name):

                # Don't shorten getattr(~) into lambda.
                # Should cause error, because getattr being evaluated lazily
                slot = getattr(self, signal_name)
                signal.connect(lambda x: slot(x))

        self.start()


class Input_DropFile(BaseComponent):

    psd_hanlders = []

    def start(self):
        # let drag-droppable
        self.widget.dragEnterEvent = self.dragEnterEvent
        self.widget.dragMoveEvent = self.dragMoveEvent
        self.widget.dropEvent = self.dropEvent

    def dragEnterEvent(self, e):
        e.acceptProposedAction()

    def dragMoveEvent(self, e):
        e.acceptProposedAction()

    def dropEvent(self, e):
        if not e.mimeData().hasUrls():
            return

        for url in e.mimeData().urls():
            path = url.path()
            if path.startswith("/"):
                path = path[1:]
            self.psd_hanlders.append(
                psd_handle.PSDHandler(path)
            )
