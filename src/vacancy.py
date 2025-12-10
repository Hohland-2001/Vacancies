class Vacancy:
    __slots__ = ["title", "link", "address", "salary", "description", "requirements"]
    """
    Класс для работы с вакансиями
    """
    title: str
    link: str
    address: str
    salary: str
    description: str
    requirements: str

    # Дефолтные значения для полей
    TITLE = "Вакансия без названия"
    LINK = "Ссылка отсутствует"
    ADDRESS = "Адрес не указан"
    SALARY = "Зарплата не указана"
    DESCRIPTION = "Описание отсутствует"
    REQUIREMENTS = "Требования не указаны"

    def __init__(self, hh_vacancy: dict) -> None:
        self.title = self.__validate_title(hh_vacancy["name"])
        self.link = self.__validate_link(hh_vacancy["alternate_url"])
        self.address = self.__validate_address(self.__get_safe(self.__get_safe(hh_vacancy, "address"), "raw"))
        self.salary = self.__validate_salary(self.__get_safe(hh_vacancy, "salary"))
        self.description = self.__validate_description(
            self.__get_safe(self.__get_safe(hh_vacancy, "snippet"), "responsibility")
        )
        self.requirements = self.__validate_requirements(
            self.__get_safe(self.__get_safe(hh_vacancy, "snippet"), "requirement")
        )

    @staticmethod
    def __get_safe(data: dict, key: str) -> dict | None:
        """
        Безопасное получение значения из словаря.
        Возвращает None, если ключ отсутствует или data.
        """
        if isinstance(data, dict) and key in data:
            return data[key]
        else:
            return None

    def __validate_title(self, value: str | None) -> str:
        """
        Проверяет поле title
        """
        if isinstance(value, str):
            return value
        else:
            return self.TITLE

    def __validate_link(self, value: str | None) -> str:
        """
        Проверяет поле link
        """
        if isinstance(value, str):
            return value
        else:
            return self.LINK

    def __validate_address(self, value: dict | None) -> str:
        """
        Проверяет поле link
        """
        if isinstance(value, str):
            return value
        else:
            return self.ADDRESS

    def __validate_salary(self, value: dict | None) -> str:
        """
        Проверяет поле salary
        """
        if value is not None:
            if value["from"] is not None and value["to"] is not None:
                return f"{value['from']} - {value['to']}"
            elif value["from"] is not None:
                return f"{value['from']}"
            elif value["to"] is not None:
                return f"{value['to']}"
            else:
                pass
        else:
            return self.SALARY

    def __validate_description(self, value: dict | None) -> str:
        """
        Проверяет поле description
        """
        if isinstance(value, str):
            return value
        else:
            return self.DESCRIPTION

    def __validate_requirements(self, value: dict | None) -> str:
        """
        Проверяет поле requirements
        """
        if isinstance(value, str):
            return value
        else:
            return self.REQUIREMENTS

    def __ge__(self, other: object) -> bool:
        """
        Магический метод, который сравнивает зарплату >= (больше или равно)
        """
        if isinstance(other, Vacancy):
            if int(self.salary.split()[0]) >= int(other.salary.split()[0]):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __str__(self) -> str:
        """
        Магический метод для строкового отображения объекта
        """
        return f"{self.title}, {self.link}, {self.address}, {self.salary}, {self.description}, {self.requirements}"
