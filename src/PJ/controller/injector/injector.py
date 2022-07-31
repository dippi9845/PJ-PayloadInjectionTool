from abc import ABC, abstractmethod
from __future__ import annotations

class Injector(ABC):
    
    @abstractmethod
    def _get_injection(self, index : int) -> str | Injector:
        pass
    
    @abstractmethod
    def _inject_by_index(self, index : int) -> None:
        pass
    
    @abstractmethod
    def inject_all(self) -> None:
        pass

class InjectorIterator:
    def __init__(self, injector : Injector, injection_num : int) -> None:
        self.__injector = injector
        self.__injection_num = injection_num
        self.__index = 0
    
    def _is_over(self) -> bool:
        self.__index < self.__injection_num

    def _get_injector_at_index(self) -> str | Injector:
        return self.__injector._get_injection(self.__index)

    def __next__(self) -> str | Injector:
        if self._is_over():
            self.__injector._inject_by_index(self.__index)
            self.__index += 1
            return self._get_injector_at_index()
        else:
            raise StopIteration


class InjectorList(Injector):
    def __init__(self, injectors : list[Injector]):
        self.__injectors = injectors

    def __iter__(self):
        return InjectorListIterator(self)
    
    def _inject_by_index(self, index : int) -> None:
        '''
        Cant inject an injector, so do nothing
        '''
        pass

    def _get_injection(self, index : int) -> Injector:
        return self.__injectors[index]

    def inject_all(self):
        for i in self.__injectors:
            i.inject_all()
    
    def split(self, num : int) -> list:
        rtr = [self.__injectors[x:x+num] for x in range(0, len(self.__injectors), num)]
        rtr = [InjectorList(x.copy()) for x in rtr]
        return rtr

class InjectorListIterator(InjectorIterator):
    def __init__(self, injector: InjectorList) -> None:
        super().__init__(injector, len(injector))