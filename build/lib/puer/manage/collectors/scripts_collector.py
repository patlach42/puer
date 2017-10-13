from sys import modules
from importlib import import_module, util
from core.core import AbstractCollector

from core.scripts import __scripts__

__all__ = ["ScriptsCollector"]


class ScriptsCollector(AbstractCollector):
    def __init__(self):
        self.scripts = __scripts__

    def load_from_module(self, module):
        package_name = "%s.scripts" % module
        if util.find_spec(package_name) is not None:
            import_module(package_name)
            self.scripts.update(modules[package_name].__scripts__)