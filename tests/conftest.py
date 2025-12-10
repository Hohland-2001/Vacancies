import pytest


@pytest.fixture
def v_correct1():
    v = {
        "name": "aaa",
        "alternate_url": "bbb",
        "address": {"raw": "ccc"},
        "salary": {"from": "10000", "to": "15000"},
        "snippet": {"responsibility": "ddd", "requirement": "eee"}
    }
    return v


@pytest.fixture
def v_correct2():
    v = {
        "name": "xxx",
        "alternate_url": "ppp",
        "address": {"raw": "vvv"},
        "salary": {"from": "5000", "to": "11000"},
        "snippet": {"responsibility": "nnn", "requirement": "mmm"}
    }
    return v


@pytest.fixture
def v_no_info():
    v = {
        "name": None,
        "alternate_url": None,
        "address": {"raw": None},
        "salary": None,
        "snippet": {"responsibility": None, "requirement": None}
    }
    return v


@pytest.fixture
def v_no_salary_from():
    v = {
        "name": "aaa",
        "alternate_url": "bbb",
        "address": {"raw": "ccc"},
        "salary": {"from": None, "to": "15000"},
        "snippet": {"responsibility": "ddd", "requirement": "eee"}
    }
    return v


@pytest.fixture
def v_no_salary_to():
    v = {
        "name": "aaa",
        "alternate_url": "bbb",
        "address": {"raw": "ccc"},
        "salary": {"from": "10000", "to": None},
        "snippet": {"responsibility": "ddd", "requirement": "eee"}
    }
    return v
