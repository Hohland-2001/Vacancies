from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def load_vacancies(self, *args):
        pass


class AddGetDel(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления
    вакансий в файл, получения данных из файла по указанным критериям и
    удаления информации о вакансиях
    """

    @abstractmethod
    def add_vacancy(self, *args):
        pass

    @abstractmethod
    def get_vacancy(self, *args):
        pass

    @abstractmethod
    def delete_vacancy(self, *args):
        pass
