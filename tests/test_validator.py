import pytest
from src.validator import Validator

class TestValidator:

    @pytest.mark.parametrize("email, expected", [
        ("dev@test.com", True),
        ("wrong-format", False),
        (None, "error"),
    ])
    def test_email(self, email, expected):
        if expected == "error":
            with pytest.raises(ValueError): Validator.validate_email(email)
        else:
            assert Validator.validate_email(email) == expected

    @pytest.mark.parametrize("pwd, expected", [
        ("Python2026", True),
        ("short", False),
        ("nouppercas1", False),
        ("NoDigitsHere", False),
    ])
    def test_password(self, pwd, expected):
        assert Validator.validate_password(pwd) == expected

    @pytest.mark.parametrize("phone, expected", [
        ("+998901234567", True),
        ("998901234567", False),
        ("+998123", False),
    ])
    def test_phone(self, phone, expected):
        assert Validator.validate_phone(phone) == expected

    @pytest.mark.parametrize("user, expected", [
        ("risolat_dev", True),
        ("1user", False),    # Raqam bilan boshlangan
        ("ab", False),       # Juda qisqa
        ("very_long_username_test", False), # Juda uzun
    ])
    def test_username(self, user, expected):
        assert Validator.validate_username(user) == expected

    @pytest.mark.parametrize("year, expected", [
        (1998, True),
        (2026, True),        # Hozirgi yil (valid)
        (1899, False),       # Chegara osti
        (2030, False),       # Kelajak
        ("2000", False),     # Noto'g'ri tip
    ])
    def test_birth_year(self, year, expected):
        assert Validator.validate_birth_year(year) == expected