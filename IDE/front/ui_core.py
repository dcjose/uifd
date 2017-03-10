from ui_view import IdeWindow

import io, sys

# Para simular clases parciales.
def extends(klass):
    def _(func):
      setattr(klass, func.__name__, func)
      return func
    return _

@extends(IdeWindow)
def on_new_comp():
    print("Manzana")
