from src.abstract_class import Abstract


class Vacancy(Abstract):
    '''Класс для работы с данными вакансий с сайта hh.ru'''
    name: str
    link: str
    salary: int
    description: str

    def __init__(self, name, link, salary, description):
        '''Инициализатор'''
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description
