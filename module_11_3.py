import inspect
from pprint import pprint


def introspection_info(obj):
    about = {'type': type(obj), 'attributes': [method for method in dir(obj) if
                                               hasattr(obj, method) and not callable(getattr(obj, method))],
             'methods': [method for method in dir(obj) if hasattr(obj, method) and callable(getattr(obj, method))],
             'module': inspect.getmodule(obj).__name__ if hasattr(inspect.getmodule(obj), "__name__") else "None"}

    return about


class SomeClass:
    attr1 = 0

    def __init__(self, a):
        self.a = a

    def func(self):
        self.a *= 5
        return self.a


if __name__ == '__main__':
    testClass = SomeClass(5)
    number_info = introspection_info(testClass)
    pprint(number_info)
