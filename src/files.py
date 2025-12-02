import json
import os
from abc import ABC, abstractmethod
from typing import Any

from src.vacancy import Vacancy


class AddGetDel(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления
    вакансий в файл, получения данных из файла по указанным критериям и
    удаления информации о вакансиях
    """

    @abstractmethod
    def add_vacancy(self, *args: Any) -> None:
        pass

    @abstractmethod
    def get_vacancy(self, *args: Any) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, *args: Any) -> None:
        pass


class JSONSaver(AddGetDel):
    """
    Класс для сохранения, удаления, добавления и получения информации о вакансиях в JSON-файле
    """

    __name_file: str

    def __init__(self, name_file: str | None = None) -> None:
        self.__name_file = name_file if name_file else "vacancies"

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Метод добавляет данных в файл
        """
        try:
            with open(f"../data/{self.__name_file}.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            if any(str(vacancy.link) in v.values() for v in data) is False:
                dictionary = {}
                dictionary["title"] = vacancy.title
                dictionary["link"] = vacancy.link
                dictionary["salary"] = vacancy.salary
                dictionary["description"] = vacancy.description
                dictionary["requirements"] = vacancy.requirements
                data.append(dictionary)

            with open(f"../data/{self.__name_file}.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except json.JSONDecodeError:
            with open(f"../data/{self.__name_file}.json", "w", encoding="utf-8") as file:
                dictionary = {}
                dictionary["title"] = vacancy.title
                dictionary["link"] = vacancy.link
                dictionary["salary"] = vacancy.salary
                dictionary["description"] = vacancy.description
                dictionary["requirements"] = vacancy.requirements
                json.dump([dictionary], file, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            with open(f"../data/{self.__name_file}.json", "w", encoding="utf-8") as file:
                dictionary = {}
                dictionary["title"] = vacancy.title
                dictionary["link"] = vacancy.link
                dictionary["salary"] = vacancy.salary
                dictionary["description"] = vacancy.description
                dictionary["requirements"] = vacancy.requirements
                json.dump([dictionary], file, ensure_ascii=False, indent=4)

        return None

    def get_vacancy(self) -> list[dict]:
        """
        Метод получения данных из файла
        """
        with open(f"../data/{self.__name_file}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Метод удаляют вакансию из списка
        """
        with open(f"../data/{self.__name_file}.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        count = 0
        for v in data:
            if vacancy.link in v.values():
                del data[count]
            else:
                count += 1

        with open(f"../data/{self.__name_file}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return None
