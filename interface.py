# customized-python/interface.py
# Ian Kollipara
# 2020.03.04
# Rust-like Interface implementation in Python
#
# Usage
# from interface import Interface

# Imports
from typing import Iterable, Optional

class Interface:
    """ Implement a Rust-like Interface. 
    
    Use as a wrapper around a list of functions.
    """

    def __init__(self, methods:Iterable[function]=[]) -> None:
        """ __init__() create a new Interface object. 
        
        Parameters
        methods  Optional list of functions to apply to the object.

        Example
        i = Interface()
        i.add_method(f)
        """

        self.__init_methods(methods)
    
    def add_method(self, method:function) -> None:
        """ Add new method to Interface object. 
        
        Parameters
        method  Function to be added
        """

        setattr(self, method.__name__, method)
    
    def __init_methods(self, methods:Iterable[function]) -> None:
        """ Add list of methods to Interface object. 
        
        PRIVATE FUNCTION

        Parameters
        methods  List of methods to be added to Interface object
        """

        for method in methods:
            setattr(self, method.__name__, method)