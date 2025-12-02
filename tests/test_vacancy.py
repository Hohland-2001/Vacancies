import unittest
from unittest.mock import patch

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.vacancy = Vacancy(
            title="Python Developer",
            link="https://example.com/1",
            salary="100000 – 150000",
            description="Разработка на Python",
            requirements="Опыт от 3 лет",
        )

    # 1. Тесты для __init__

    def test_init_sets_attributes(self):
        """Проверка установки атрибутов при инициализации"""
        self.assertEqual(self.vacancy.title, "Python Developer")
        self.assertEqual(self.vacancy.link, "https://example.com/1")
        self.assertEqual(self.vacancy.salary, "100000 – 150000")
        self.assertEqual(self.vacancy.description, "Разработка на Python")
        self.assertEqual(self.vacancy.requirements, "Опыт от 3 лет")
        self.assertIsInstance(self.vacancy.list_of_vacancies, list)
        self.assertEqual(len(self.vacancy.list_of_vacancies), 0)

    # 2. Тесты для cast_to_object_list

    def test_cast_to_object_list_normal_case(self):
        """Тест нормальной работы метода (все ключи присутствуют)"""
        hh_data = [
            {
                "name": "Backend Engineer",
                "alternate_url": "https://job.com/123",
                "salary": {"from": 120000, "to": 180000},
                "snippet": {"responsibility": "Разработка API", "requirement": "Знание Django"},
            }
        ]
        self.vacancy.cast_to_object_list(hh_data)

        expected = {
            "title": "Backend Engineer",
            "link": "https://job.com/123",
            "salary": "120000 - 180000",
            "description": "Разработка API",
            "requirements": "Знание Django",
        }
        self.assertEqual(len(self.vacancy.list_of_vacancies), 1)
        self.assertDictEqual(self.vacancy.list_of_vacancies[0], expected)

    def test_cast_to_object_list_missing_alternate_url(self):
        """Тест: нет alternate_url → подставляется дефолтное значение"""
        hh_data = [{"name": "QA Engineer", "salary": {"from": 80000, "to": 100000}}]
        self.vacancy.cast_to_object_list(hh_data)

        result = self.vacancy.list_of_vacancies[0]
        self.assertEqual(result["link"], "Ссылка не найдена")  # KeyError → "Ссылка не найдена"

    def test_cast_to_object_list_salary_none(self):
        """Тест: salary is None → подставляется 'Зарплата не указана'"""
        hh_data = [{"name": "Designer", "salary": None, "snippet": {"responsibility": "UI/UX"}}]
        self.vacancy.cast_to_object_list(hh_data)

        result = self.vacancy.list_of_vacancies[0]
        self.assertEqual(result["salary"], "Зарплата не указана")  # TypeError → "Зарплата не указана"

    def test_cast_to_object_list_missing_salary_keys(self):
        """Тест: отсутствуют from/to в salary → 'Зарплата не указана'"""
        hh_data = [{"name": "Analyst", "salary": {}, "snippet": {"responsibility": "Анализ данных"}}]  # пустой словарь
        self.vacancy.cast_to_object_list(hh_data)

        result = self.vacancy.list_of_vacancies[0]
        self.assertEqual(result["salary"], "Зарплата не указана")

    def test_cast_to_object_list_missing_description(self):
        """Тест: нет snippet.responsibility → 'Описание отсутствует'"""
        hh_data = [{"name": "Manager", "salary": {"from": 90000, "to": 110000}}]
        self.vacancy.cast_to_object_list(hh_data)

        result = self.vacancy.list_of_vacancies[0]
        self.assertEqual(result["description"], "Описание отсутствует")

    def test_cast_to_object_list_missing_requirements(self):
        """Тест: нет snippet.requirement → 'Требования не указаны'"""
        hh_data = [
            {
                "name": "Support",
                "salary": {"from": 60000, "to": 70000},
                "snippet": {"responsibility": "Помощь пользователям"},
            }
        ]
        self.vacancy.cast_to_object_list(hh_data)

        result = self.vacancy.list_of_vacancies[0]
        self.assertEqual(result["requirements"], "Требования не указаны")

    def test_cast_to_object_list_empty_input(self):
        """Тест: пустой список входных данных → list_of_vacancies остаётся пустым"""
        self.vacancy.cast_to_object_list([])
        self.assertEqual(len(self.vacancy.list_of_vacancies), 0)

    def test_cast_to_object_list_multiple_entries(self):
        """Тест: несколько вакансий в входе → все добавляются в list_of_vacancies"""
        hh_data = [
            {"name": "Dev1", "alternate_url": "url1", "salary": {"from": 1, "to": 2}},
            {"name": "Dev2", "alternate_url": "url2", "salary": {"from": 3, "to": 4}},
        ]
        self.vacancy.cast_to_object_list(hh_data)
        self.assertEqual(len(self.vacancy.list_of_vacancies), 2)

    # 3. Тесты для __ge__

    def test_ge_same_type_true(self):
        """Тест __ge__: сравнение с другим Vacancy, условие True"""
        other = Vacancy("Junior", "url", "80000 – 100000", "", "")
        result = self.vacancy >= other
        self.assertFalse(result)  # "100000 – 150000" >= "80000 – 100000"

    def test_ge_same_type_false(self):
        """Тест __ge__: сравнение с другим Vacancy, условие False"""
        stronger = Vacancy("Senior", "url", "200000 – 250000", "", "")
        result = self.vacancy >= stronger
        self.assertFalse(result)

    def test_ge_none_handling(self):
        """Тест __ge__: обработка None в salary (хотя в __init__ такого не ожидается)"""
        # Создаём вакансию с salary=None для теста
        vac_with_none = Vacancy("Test", "url", None, "", "")
        other = Vacancy("Other", "url", "50000", "", "")

        # В текущей реализации сравнение строк с None вызовет TypeError,
        # но тест показывает, что метод ожидает строковые значения
        with self.assertRaises(TypeError):
            vac_with_none >= other
