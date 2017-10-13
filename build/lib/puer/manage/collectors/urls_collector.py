from importlib import import_module, util
from core.core import AbstractCollector

__all__ = ["UrlsCollector"]


class UrlsCollector(AbstractCollector):
    def load_from_module(self, module):
        package_name = "%s.urls" % module
        if util.find_spec(package_name) is not None:
            import_module(package_name, module)
