from abc import ABC, abstractmethod

import requests


class API(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def load_vacancies(self, *args: str) -> None:
        pass


class HH(API):
    """
    Дочерний класс для работы с API HeadHunter
    """

    url: str
    headers: dict
    params: dict
    vacancies: list[dict]

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def load_vacancies(self, keyword: str) -> None:
        """
        Метод получения данных о вакансиях через API
        """
        self.__params["text"] = keyword
        while self.__params.get("page") != 2:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    @property
    def headers(self) -> dict:
        """
        Геттер возвращает словарь
        """
        return self.__headers

    @property
    def params(self) -> dict:
        """
        Геттер возвращает словарь параметров
        """
        return self.__params

    @property
    def vacancies(self) -> list[dict]:
        """
        Геттер возвращает список вакансий
        """
        return self.__vacancies

    @property
    def url(self) -> str:
        """
        Геттер возвращает ссылку
        """
        return self.__url
