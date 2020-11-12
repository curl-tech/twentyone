import sys
import types

from ..tasks.tasks import TaskType
from ..data.data import DataType

def str_to_class(field):
    try:
        identifier = getattr(sys.modules[__name__], field)
    except AttributeError:
        raise NameError("%s doesn't exist." % field)
    if isinstance(identifier, types.ClassType):
        return identifier
    raise TypeError("%s is not a class." % field)



