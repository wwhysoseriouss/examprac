import pytest
from main import get_days_in_month

def test_valid_months():
    assert get_days_in_month("january") == 31
    assert get_days_in_month("april") == 30
    assert get_days_in_month("february") == 28

def test_case_insensitivity():
    assert get_days_in_month("May") == 31
    assert get_days_in_month("DECEMBER") == 31
    assert get_days_in_month("juLY") == 31

def test_strip_whitespace():
    assert get_days_in_month(" june ") == 30

def test_invalid_month():
    with pytest.raises(ValueError):
        get_days_in_month("Mars")
    with pytest.raises(ValueError):
        get_days_in_month("123")
    with pytest.raises(ValueError):
        get_days_in_month("")