# customized-python/JSON_dict.py
# Ian Kollipara
# 2020.03.02
# JSON notation in python
# 
# Usage
# from JSON_dict import JSON


class JSON(dict):
    """ Implement a python dictionary with dot notation. 
    
    Use as wrapper around base dictionary construction.
    """

    def __getattr__(self, key):
        """ Get value at key. """

        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        """ Set value at key. """

        self[key] = value
    
    def __delattr__(self, key):
        """ Delete value at key. """

        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)
    
    def __repr__(self):
        
        return f"<JSON {dict.__repr__(self)}>"