
"""
Defines ui interactions

Dependency:
 - PyQt5
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtBoundSignal


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
