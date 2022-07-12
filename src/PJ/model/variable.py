from injectable import Injectable

'''
This class model a varaible in the url
'''
class Variable:

    def __init__(self, var_name : str, protocol : str, content="") -> None:
        self.__var_name =  var_name
        self.__protocol = protocol
        self.__content = content
    
    def _set_content(self, content : str) -> None:
        self.__content = content

    def get_protocol(self) -> str:
        return self.__protocol
    
    def get_variable_name(self) -> str:
        return self.__var_name

    def get_content(self) -> str:
        return self.__content
    
    def to_dict(self):
        return {self.__var_name : self.__content}

''' 
This is a variable that can't be injected anything
'''
class FixedVariable(Injectable, Variable):

    def __init__(self, var_name : str, protocol : str, content="") -> None:
        super().__init__(var_name, protocol, content)


class InjectableVariable(Injectable, Variable):
    def __init__(self, var_name : str, protocol : str, content="") -> None:
        super().__init__(var_name, protocol, content)

    def _clear(self) -> None:
        self._set_content("")

    def inject(self, payload : str) -> None:
        self._set_content(payload)