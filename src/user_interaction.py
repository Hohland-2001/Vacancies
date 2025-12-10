from itertools import count

from src.api import HH
from src.files import JSONSaver
from src.vacancy import Vacancy


def user_interaction() -> None:
    """
    Функцию для взаимодействия с пользователем через консоль
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = input("Введите количество вакансий для вывода в топ N: ")  # Пример: 6
    filter_words = input("Введите ключевые слова для фильтрации вакансий через запятую: ").split(
        ", "
    )  # Москва, высшее образование
    salary_minimum = input("Введите нижний порог зарплаты: ")  # Пример: 100000
    response_user = input("Выберите как произвести сортировку по зарплате:\n1. По возрастанию\n2. По убыванию\n")

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HH()

    # Получение вакансий с hh.ru в формате JSON
    hh_api.load_vacancies(search_query)

    # Получаем список вакансий
    hh_vacancies = hh_api.vacancies

    # Создаём список экземпляров класса для работы с вакансиями
    list_of_vacancies = []
    for v in hh_vacancies:
        list_of_vacancies.append(Vacancy(v))

    # Фильтруем вакансии по ключевым словам
    filtered_vacancies = filter_vacancies(list_of_vacancies, filter_words)

    # Фильтруем список вакансий по зарплате
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_minimum)

    # Сортируем вакансии по зарплате (по умолчанию: по возрастанию)
    sorted_vacancies = sort_vacancies(ranged_vacancies, response_user)

    for v in sorted_vacancies:
        JSONSaver().add_vacancy(v)

    print(JSONSaver().get_vacancy()[: int(top_n)])
    return None


def filter_vacancies(vacancies_list: list, filter_words: list | None = None) -> list:
    """
    Функция фильтрует список вакансий по ключевым словам
    """
    if filter_words == "" or filter_words is None:
        no_filtered_vacancies = vacancies_list
        return no_filtered_vacancies
    else:
        filtered_vacancies = []
        for vacancy in vacancies_list:
            for word in filter_words:
                if (
                    word.lower()
                    in f"{vacancy.title.lower(), vacancy.link.lower(), vacancy.address.lower(), vacancy.salary.lower(),
                vacancy.description.lower(), vacancy.requirements.lower()}"
                ):
                    filtered_vacancies.append(vacancy)
                else:
                    continue
        return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list, salary_minimum: str) -> list:
    """
    Функция фильтрует список по диапазону зарплат
    """
    if bool(salary_minimum.strip()) is False:
        return filtered_vacancies
    else:
        ranged_vacancies = []
        minimum = int(salary_minimum)
        for vacancy in filtered_vacancies:
            if vacancy.salary == "Зарплата не указана":
                continue
            elif minimum <= int(vacancy.salary.split(" - ")[0]):
                ranged_vacancies.append(vacancy)
            else:
                continue
        return ranged_vacancies


def sort_vacancies(list_of_vacancies: list, response: str) -> list:
    """
    Функция сортирует вакансии по зарплате (по умолчанию: по возрастанию)
    """
    if bool(response) is False:
        response = "1"
    sorted_vacancies = sorted(
        list_of_vacancies,
        reverse=False if int(response) == 1 else True,
        key=lambda vacancy: int(vacancy.salary.split(" - ")[0]),
    )
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies: list, top_n: str) -> list:
    """
    Функция выводит количество вакансий, заданных пользователем
    """
    if top_n == "":
        return sorted_vacancies
    else:
        n = int(top_n)
        return sorted_vacancies[:n]
