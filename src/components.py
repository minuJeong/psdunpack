
"""
Defines ui interactions

Dependency:
 - PyQt5
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import pyqtBoundSignal

from . import psd_handle


class CMN_EVENTKEY(object):
    CLICKED = "clicked"


class EventDispatcher(object):

    _eventmapping = {}

    def add_event_listener(self, eventkey, callback):
        if eventkey not in self._eventmapping:
            self._eventmapping[eventkey] = []

        self._eventmapping[eventkey].append(callback)

    def remove_event_listener(self, eventkey, callback):
        if eventkey not in self._eventmapping:
            return

        if callback not in self._eventmapping[eventkey]:
            return

        self._eventmapping[eventkey].remove(callback)

    def dispatch_event(self, eventkey, param):
        if eventkey not in self._eventmapping:
            return

        for callback in self._eventmapping[eventkey]:
            callback(param)


class BaseComponent(EventDispatcher):
    """ Connect signals using reflection """

    _component_reference_mapping = {}

    widget = None
    triggers = None

    def start(self):
        """ override this and define initialization """
        pass

    def __init__(self, widget, widget_name):
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

        BaseComponent._component_reference_mapping[widget_name] = self

    def get_component(self, target_name):
        return BaseComponent._component_reference_mapping[target_name]


class Input_DropFile(BaseComponent):

    EVENTKEY_UPDATE_OPENFILES = "eventkey update openfiles"

    psd_handlers = []

    def start(self):
        # let drag-droppable
        self.widget.dragEnterEvent = self.drag_enter
        self.widget.dragMoveEvent = self.drag_move
        self.widget.dropEvent = self.drop_file

        self.get_component("UnpackButton").add_event_listener(
            CMN_EVENTKEY.CLICKED,
            lambda x: self.unpack()
        )

    def drag_enter(self, e):
        e.acceptProposedAction()

    def drag_move(self, e):
        e.acceptProposedAction()

    def drop_file(self, e):
        if not e.mimeData().hasUrls():
            return

        self.psd_handlers = []

        for url in e.mimeData().urls():
            path = url.path()
            if path.startswith("/"):
                path = path[1:]
            self.psd_handlers.append(
                psd_handle.PSDHandler(path)
            )

        layers = []
        for psd_handler in self.psd_handlers:
            layers += psd_handler.leaf_layers

        print(len(self.psd_handlers))
        print(len(layers))
        print("DISPATCH", layers)
        self.dispatch_event(
            Input_DropFile.EVENTKEY_UPDATE_OPENFILES,
            layers
        )

    def unpack(self):
        for psd_handler in self.psd_handlers:
            psd_handler.unpack()


class Preview_Layers(BaseComponent):

    def start(self):
        self.refresh_list([])
        self.get_component("Input_DropFile")\
            .add_event_listener(
                Input_DropFile.EVENTKEY_UPDATE_OPENFILES,
                self.refresh_list
            )

    def refresh_list(self, layers):
        self.widget.clear()
        for layer in layers:
            item = QTreeWidgetItem(self.widget)
            item.setText(0, layer.name)


class UnpackButton(BaseComponent):

    def clicked(self, is_checked=False):
        self.dispatch_event(CMN_EVENTKEY.CLICKED, None)
