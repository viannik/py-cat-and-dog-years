import pytest

from app import main


def convert_to_human(cat_age, first_year, second_year, each_year):
    if cat_age < first_year:
        return 0
    if cat_age < first_year + second_year:
        return 1
    return 2 + (cat_age - first_year - second_year) // each_year


def test_zero_ages(monkeypatch):

    def mock_zero_ages(cat_age, dog_age):
        cat_to_human = convert_to_human(cat_age, 15.00001, 9, 4)
        dog_to_human = convert_to_human(dog_age, 15.00001, 9, 5)
        return [cat_to_human, dog_to_human]

    monkeypatch.setattr(main, "get_human_age", mock_zero_ages)

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1


def test_first_ages(monkeypatch):

    def mock_first_ages(cat_age, dog_age):
        cat_to_human = convert_to_human(cat_age, 15, 9.00001, 4)
        dog_to_human = convert_to_human(dog_age, 15, 9.00001, 5)
        return [cat_to_human, dog_to_human]

    monkeypatch.setattr(main, "get_human_age", mock_first_ages)

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1


def test_second_ages(monkeypatch):

    def mock_second_ages(cat_age, dog_age):
        cat_to_human = convert_to_human(cat_age, 15, 9, 4.00001)
        dog_to_human = convert_to_human(dog_age, 15, 9, 5.00001)
        return [cat_to_human, dog_to_human]

    monkeypatch.setattr(main, "get_human_age", mock_second_ages)

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1
