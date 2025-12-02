class Vacancy:
    __slots__ = ["title", "link", "salary", "description", "requirements", "list_of_vacancies"]
    """
    Класс для работы с вакансиями
    """
    title: str
    link: str
    salary: str
    description: str
    requirements: str
    list_of_vacancies: list[dict]

    def __init__(self, title, link, salary, description, requirements) -> None:
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self.requirements = requirements
        self.list_of_vacancies = []

    def cast_to_object_list(self, hh_vacancies: list) -> None:
        """
        Добавляет словарь вакансий в список c ключами title, link, salary, description, requirements
        """
        vacancy_list = []
        for i in hh_vacancies:
            dictionary = {}
            dictionary["title"] = i["name"]
            try:
                dictionary["link"] = i["alternate_url"]
            except ValueError:
                dictionary["link"] = "Ссылка не указана"
            except KeyError:
                dictionary["link"] = "Ссылка не найдена"
            try:
                dictionary["salary"] = f"{i['salary']['from']} - {i['salary']['to']}"
            except ValueError:
                dictionary["salary"] = "Зарплата не указана"
            except KeyError:
                dictionary["salary"] = "Зарплата не указана"
            except TypeError:
                dictionary["salary"] = "Зарплата не указана"
            try:
                dictionary["description"] = i["snippet"]["responsibility"]
            except ValueError:
                dictionary["description"] = "Описание отсутствует"
            except KeyError:
                dictionary["description"] = "Описание отсутствует"
            try:
                dictionary["requirements"] = i["snippet"]["requirement"]
            except ValueError:
                dictionary["requirements"] = "Требования не указаны"
            except KeyError:
                dictionary["requirements"] = "Требования не указаны"
            vacancy_list.append(dictionary)
        self.list_of_vacancies.extend(vacancy_list)
        return None

    def __validation(self):
        """
        Приватный метод валидации данных
        """
        pass

    def __ge__(self, other: object) -> bool:
        """
        Магический метод, который сравнивает зарплату >= (больше или равно)
        """
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        else:
            return NotImplemented
