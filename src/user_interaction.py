from src.vacancy import HH, Vacancy, JSONSaver


def user_interaction() -> None:
    """
    Функцию для взаимодействия с пользователем через консоль
    """
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = input("Введите количество вакансий для вывода в топ N: ")  # Пример: 6
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split(', ')  # Москва, высшее образование
    salary_minimum = input("Введите нижний порог зарплаты: ")  # Пример: 100000

    # Делается запрос вакансий от сайта hh.ru по ключевому слову
    hh_api = HH()
    hh_api.load_vacancies(search_query)

    # Формируем список вакансий по нужным ключам словаря
    vacancies_list = Vacancy()
    vacancies_list.cast_to_object_list(hh_api.vacancies)

    # Сохраняем отформатированный список в json-файл
    JSONSaver().save_vacancy_in_json_file(vacancies_list.vacancies)

    # Фильтруем список по ключевым словам
    filtered_vacancies = filter_vacancies(vacancies_list.vacancies, filter_words)
    print(f'Фильтр по ключевым словам {filtered_vacancies}\n\n')

    # Фильтруем список по диапазону зарплат
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_minimum)
    print(f'Фильтруем список по диапазону зарплат {ranged_vacancies}\n\n')

    # Сортируем вакансии по зарплате
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    print(f'Сортируем вакансии по зарплате {sorted_vacancies}\n\n')

    # Выводим топ N вакансий (N - задаётся пользователем)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(f'Выводим топ N вакансий {top_vacancies}')

    return None


def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
    """
    Функция фильтрует список вакансий по ключевым словам
    """
    if filter_words == '':
        no_filtered_vacancies = vacancies_list
        return no_filtered_vacancies
    else:
        filtered_vacancies = []
        for vacancy in vacancies_list:
            for word in filter_words:
                if word in str(vacancy):
                    filtered_vacancies.append(vacancy)
                else:
                    continue
        return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list, salary_minimum: str) -> list:
    """
    Функция фильтрует список по диапазону зарплат
    """
    if salary_minimum == '' or salary_minimum is str:
        return filtered_vacancies
    else:
        ranged_vacancies = []
        minimum = int(salary_minimum)
        for vacancy in filtered_vacancies:
            if vacancy['salary'] == 'Зарплата не указана':
                ranged_vacancies.append(vacancy)
            elif minimum <= int(vacancy['salary'].split(' - ')[0]):
                ranged_vacancies.append(vacancy)
            else:
                continue
    return ranged_vacancies


def sort_vacancies(list_of_vacancies: list) -> list:
    """
    Функция сортирует вакансии по зарплате (по возрастанию)
    """
    sorted_vacancies = sorted(list_of_vacancies, reverse=False, key=lambda vacancy: vacancy['salary'].split(' - ')[0])
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies: list, top_n: str) -> list:
    """
    Функция выводит количество вакансий, заданных пользователем
    """
    if top_n == '':
        return sorted_vacancies
    else:
        n = int(top_n)
        return sorted_vacancies[:n]
