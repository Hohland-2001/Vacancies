from unittest.mock import patch

from src.api import HH


@patch("requests.get")
def test_class_hh_load_vacancies(mock_get):
    mock_get.return_value.json.return_value = {"items": ["1234567889", "5675657"]}
    h = HH()
    h.load_vacancies("aaa")
    assert h.vacancies == [
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
        "1234567889",
        "5675657",
    ]
