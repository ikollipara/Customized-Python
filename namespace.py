# customize-python/namespace.py
# Ian Kollipara
# 2020.03.03
# Namespace Implementation in Python
#
# Usage
# from namespace import create_namespace, namespace

# Imports
from functools import wraps
from typing import Callable

def create_namespace(scope:str) -> object:
    """ Create an empty namespace from given scope. 
    
    scope  String used to create namespace.
    """

    return type(scope, (object,), {})()

def namespace(scope:object) -> Callable:
    """ Add given the function to the given namespace. 
    
    Parameters
    scope  Object to add the function to. Used in conjunction
           with create_namespace()
    """

    def namespace_decorator(func:Callable) -> Callable:
        """ Inner decorator function. 
        
        func  Function passed as part of decorator syntax.
        """

        setattr(scope, func.__name__, func)

        @wraps(func)
        def wrapper() -> None:
            return func()

        return wrapper

    return namespace_decorator