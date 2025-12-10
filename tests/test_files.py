import json
import os

from src.files import JSONSaver
from src.vacancy import Vacancy


def test_class_json_saver_add_vacancy(v_correct2: dict, v_no_info: dict) -> None:
    test_file = "test_vacancies"
    test_data_path = f"../data/{test_file}"

    # Удаляем файл перед тестом, если существует
    if os.path.exists(f'{test_data_path}.json'):
        os.remove(f'{test_data_path}.json')

    v = Vacancy(v_correct2)
    JSONSaver(test_data_path).add_vacancy(v)

    JSONSaver(test_data_path).add_vacancy(v)

    assert JSONSaver(test_data_path).get_vacancy() == [
        {
            "title": "xxx",
            "link": "ppp",
            "address": "vvv",
            "salary": "5000 - 11000",
            "description": "nnn",
            "requirements": "mmm"
        }
    ]


def test_class_json_saver_get_vacancy(v_correct2: dict) -> None:
    test_file = "test_vacancies"
    test_data_path = f"../data/{test_file}"

    # Удаляем файл перед тестом, если существует
    if os.path.exists(f'{test_data_path}.json'):
        os.remove(f'{test_data_path}.json')

    v = Vacancy(v_correct2)
    JSONSaver(test_data_path).add_vacancy(v)
    assert JSONSaver(test_data_path).get_vacancy() == [
        {
            "title": "xxx",
            "link": "ppp",
            "address": "vvv",
            "salary": "5000 - 11000",
            "description": "nnn",
            "requirements": "mmm"
        }
    ]


def tests_class_json_saver_del_vacancy(v_correct1: dict, v_correct2: dict) -> None:
    test_file = "test_vacancies"
    test_data_path = f"../data/{test_file}"

    # Удаляем файл перед тестом, если существует
    if os.path.exists(f'{test_data_path}.json'):
        os.remove(f'{test_data_path}.json')

    v1 = Vacancy(v_correct1)
    v2 = Vacancy(v_correct2)
    JSONSaver(test_data_path).add_vacancy(v1)
    JSONSaver(test_data_path).add_vacancy(v2)
    JSONSaver(test_data_path).delete_vacancy(v1)

    assert JSONSaver(test_data_path).get_vacancy() == [
        {
            "title": "xxx",
            "link": "ppp",
            "address": "vvv",
            "salary": "5000 - 11000",
            "description": "nnn",
            "requirements": "mmm"
        }
    ]
