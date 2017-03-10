## exampe usage
class C:
    def __init__(self, data):
        self.data = data
## exampe usage
class D:
    def __init__(self, data):
        self.data = data

def inclass(kls):
    """
    Decorator that adds the decorated function
    as a method in specified class
    """
    def _(func):
        setattr(kls,func.__name__, func)
        return func
    return _

# this would be in a separate file.
@inclass(C)
def meth(self, a):
    print("C:", a, self.data)
@inclass(D)
def meth(self, a):
    print("D:", a, self.data)

a = C(5)
b = D(5)

a.meth(10)
b.meth(20)
