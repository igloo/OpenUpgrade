# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger('OpenUpgrade')

_short_name = __name__.split(".")[-1]
logger.warn(
    "Importing %(full_name)s is deprecated. "
    "Use from openupgradelib import %(short_name)s" % {
        'full_name': __name__,
        'short_name': _short_name,
    }
)

_new_name = "openupgradelib.%s" % _short_name

_modules = __import__(_new_name, globals(), locals(), ['*'])
for _i in dir(_modules):
    locals()[_i] = getattr(_modules, _i)
