class _NullContextmanager(object):

  def __enter__(self):
    pass

  def __exit__(self, type_arg, value_arg, traceback_arg):
    return False  # False values do not suppress exceptions
    
#text wrappered by 'with' will call __enter__ before start and execute __exit__ after finish.
