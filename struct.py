# customized-python/struct.py
# Ian Kollipara
# 2020.03.03
# Rust-like Struct implementation in Python
# 
# Usage
# from struct import Struct

# Imports
from interface import Interface
from typing import Dict, Any

class Struct:
    """ Implement a Rust-like Struct implementation. 
    
    Use as a wrapper around a dictionary.
    """

    def __init__(self, fields:Dict[str, Any]={}) -> None:
        """ __init__() create a new Struct object. 
        
        Parameters
        fields  Optional Dictionary to initialize values with

        Example
        x = Struct()
        x.add_field({"a": 1})
        x.implement(Interface())
        """

        self.__dict__ = fields
    
    def add_field(self, field:Dict[str, Any]) -> None:
        """ Add new field to Struct. 
        
        Parameters
        field  Dictionary to update struct with.
        """

        self.__dict__.update(field)
    
    def implement(self, inteface:Interface) -> None:
        """ Add methods via an interface object. 
        
        Parameters
        interface  Interface object used to add methods with.
        """
        self.__dict__.update(inteface.__dict__)