import json

from src.abstract_class import API, AddGetDel
import requests


# class Parser(Abstract):
#     """
#     Родительский класс для сохранения информации о вакансиях в json-файл
#     """
#     file_worker: str
#
#     def __init__(self, file_worker):
#         self.file_worker = file_worker
#
#     def save_to_file(self, information):
#         """
#         Метод сохраняет данные в json-файл
#         """
#         with open(f'../data/{self.file_worker}', 'w', encoding='utf-8') as file:
#             json.loads(information)


class HH(API):
    """
    Дочерний класс для работы с API HeadHunter
    """
    url: str
    headers: dict
    params: dict
    vacancies: list

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self):
        self.vacancies = []

    def cast_to_object_list(self, hh_vacancies):
        """
        Добавляет словарь вакансий в список c ключами title, link, salary, description, requirements
        """
        vacancy_list = []
        for i in hh_vacancies:
            dictionary = {}
            dictionary['title'] = i['name']
            try:
                dictionary['link'] = i['alternate_url']
            except ValueError:
                dictionary['link'] = 'Ссылка не указана'
            except KeyError:
                dictionary['link'] = 'Ссылка не найдена'
            try:
                dictionary['salary'] = f"{i['salary']['from']} - {i['salary']['to']}"
            except ValueError:
                dictionary['salary'] = 'Зарплата не указана'
            except KeyError:
                dictionary['salary'] = 'Зарплата не указана'
            except TypeError:
                dictionary['salary'] = 'Зарплата не указана'
            try:
                dictionary['description'] = i['snippet']['responsibility']
            except ValueError:
                dictionary['description'] = 'Описание отсутствует'
            except KeyError:
                dictionary['description'] = 'Описание отсутствует'
            try:
                dictionary['requirements'] = i['snippet']['requirement']
            except ValueError:
                dictionary['requirements'] = 'Требования не указаны'
            except KeyError:
                dictionary['requirements'] = 'Требования не указаны'
            vacancy_list.append(dictionary)
        self.vacancies.extend(vacancy_list)

    def salary_comparison(self, other):
        """
        Метод сравнивает зарплаты разных вакансий
        """
        pass


class JSONSaver(AddGetDel, HH):
    """
    Класс для сохранения, удаления, добавления и получения информации о вакансиях в JSON-файле
    """

    def add_vacancy(self, vacancy):
        """
        Метод добавляет вакансию в список
        """
        self.vacancies.append(vacancy)

    def get_vacancy(self, vacancy):
        """
        Метод получает информацию о вакансии
        """
        pass

    def delete_vacancy(self, vacancy):
        """
        Метод удаляют вакансию из списка
        """
        pass

    def save_vacancy_in_json_file(self, list_of_vacancies, path_to_file='../data/vacancies.json'):
        """
        Метод сохраняет информацию в Json-файл
        """
        with open(path_to_file, 'w', encoding='utf-8') as file:
            json.dump(list_of_vacancies, file, ensure_ascii=False, indent=4)
