# customize-python/namespace.py
# Ian Kollipara
# 2020.03.03
# Namespace Implementation in Python
#
# Usage
# from namespace import create_namespace, namespace

# Imports
from functools import wraps


def create_namespace(scope):
    """ Create an empty namespace from given scope. 
    
    scope  String used to create namespace.
    """
    
    return type(scope, (object,), {})()

def namespace(scope):
    """ Add given the function to the given namespace. 
    
    Parameters
    scope  Object to add the function to. Used in conjunction
           with create_namespace()
    """

    def namespace_decorator(func):
        """ Inner decorator function. 
        
        func  Function passed as part of decorator syntax.
        """

        setattr(scope, func.__name__, func)

        @wraps(func)
        def wrapper():
            return func()

        return wrapper

    return namespace_decorator