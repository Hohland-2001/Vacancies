from abc import ABC, abstractmethod


class Abstract(ABC):
    '''Абстрактный класс'''

    @abstractmethod
    def __init__(self, *args, **kwargs):
        '''Абстрактный метод инициализации'''
        pass

    @abstractmethod
    def job_comparison(self):
        '''Метод сравнения вакансий по разным характеристикам'''
        pass
