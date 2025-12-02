import json
import os
import unittest
from unittest.mock import patch

from src.files import JSONSaver
from src.vacancy import Vacancy


class TestJSONSaver(unittest.TestCase):

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.test_file = "test_vacancies"
        self.saver = JSONSaver(self.test_file)
        self.test_data_path = f"../data/{self.test_file}.json"

        # Удаляем файл перед тестом, если существует
        if os.path.exists(self.test_data_path):
            os.remove(self.test_data_path)

    def tearDown(self):
        """Очистка после каждого теста"""
        if os.path.exists(self.test_data_path):
            os.remove(self.test_data_path)

    @patch("json.load")
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_add_vacancy_existing_file(self, mock_open, mock_load):
        """Тест добавления вакансии в существующий файл"""
        # Подготавливаем существующие данные
        existing_data = [{"title": "JS Dev", "link": "https://example.com/2", "salary": "90000", "description": "aaa",
                          "requirements": "bbb"}]
        mock_load.return_value = existing_data

        vacancy = Vacancy("Python Dev", "https://example.com/1", "100000", "hjhj", "bubu")
        self.saver.add_vacancy(vacancy)

        # Проверяем, что вакансия добавлена
        with open(self.test_data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)
            self.assertIn("Python Dev", [item["title"] for item in data])

    @patch("json.load")
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_add_vacancy_duplicate_link(self, mock_open, mock_load):
        """Тест попытки добавления дублирующей вакансии (по ссылке)"""
        existing_data = [
            {"title": "Python Dev", "link": "https://example.com/1", "salary": "100000", "description": "aaa",
             "requirements": "bbb"}]
        mock_load.return_value = existing_data

        vacancy = Vacancy("Another Python Dev", "https://example.com/1", "120000", "utytu", "uyyu")
        self.saver.add_vacancy(vacancy)  # Не должна добавиться

        with open(self.test_data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)  # Количество не изменилось
