from src.vacancy import Vacancy


def test_class_vacancy_init(v_correct1: dict, v_no_info: dict, v_no_salary_to: dict, v_no_salary_from: dict) -> None:
    v1 = Vacancy(v_correct1)
    assert v1.title == 'aaa'
    assert v1.link == 'bbb'
    assert v1.address == 'ccc'
    assert v1.salary == '10000 - 15000'
    assert v1.description == 'ddd'
    assert v1.requirements == 'eee'

    v2 = Vacancy(v_no_info)
    assert v2.title == 'Вакансия без названия'
    assert v2.link == 'Ссылка отсутствует'
    assert v2.address == 'Адрес не указан'
    assert v2.salary == 'Зарплата не указана'
    assert v2.description == 'Описание отсутствует'
    assert v2.requirements == 'Требования не указаны'

    v3 = Vacancy(v_no_salary_from)
    assert v3.title == 'aaa'
    assert v3.link == 'bbb'
    assert v3.address == 'ccc'
    assert v3.salary == '15000'
    assert v3.description == 'ddd'
    assert v3.requirements == 'eee'

    v4 = Vacancy(v_no_salary_to)
    assert v4.title == 'aaa'
    assert v4.link == 'bbb'
    assert v4.address == 'ccc'
    assert v4.salary == '10000'
    assert v4.description == 'ddd'
    assert v4.requirements == 'eee'


def test_class_vacancy_comparison(v_correct1: dict, v_correct2: dict) -> None:
    v1 = Vacancy(v_correct1)
    v2 = Vacancy(v_correct2)
    assert (v2 >= v1) == False
    assert (v2 == v1) == False


def test_class_vacancy_str(v_correct1: dict) -> None:
    v = Vacancy(v_correct1)
    assert str(v) == 'aaa, bbb, ccc, 10000 - 15000, ddd, eee'
