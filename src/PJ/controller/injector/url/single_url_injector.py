from PJ.model.url import Url
from ....utils.urls import url_request

class SingleUrlInjector:

    def __init__(self, url : Url, payloads : list[str], request: function=url_request) -> None:
        self.__url = url
        self.__payloads = payloads
        self.__request = request
    
    def __iter__(self):
        return SingleUrlInjectorIterator(self)

    def _get_payload(self, index : int) -> str:
        '''
        Returns the payload at the given position
        '''
        return self.__payloads[index]

    def _get_payload_num(self) -> int:
        '''
        Return the number of payloads stored
        '''
        return len(self.__payloads)

    def _inject_payload(self, payload : str):
        '''
        Inject to url the given, the specified payload
        '''
        self.__url.inject(payload)
    
    def _inject_by_index(self, payload_inedex : int):
        '''
        Inject the payload, in the position given by the parameter
        '''
        self.__url.inject(self._get_payload(payload_inedex))

    def inject_all(self):
        '''
        Inject all payloads, to a given url
        '''
        for payload in self.__payloads:
            self.__url.inject(payload)
            self.__request(self.__url.get_url(), self.__url.get_params())

class SingleUrlInjectorIterator:

    def __init__(self, url_injector : SingleUrlInjector) -> None:
        self.__index = 0
        self.__url_injector = url_injector
    
    def __next__(self) -> str:
        if self.__index < self.__url_injector._get_payload_num():
            payload = self.__url_injector._get_payload(self.__index)
            self.__url_injector._inject_payload(payload)
            self.__index += 1
            return payload
        else:
            raise StopIteration