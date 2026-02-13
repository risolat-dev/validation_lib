import re
from datetime import datetime

class Validator:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Email formatini va tipini tekshirish."""
        if not isinstance(email, str):
            raise ValueError("Email satr (string) bo'lishi kerak")
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_password(password: str) -> bool:
        """Kamida 8 belgi, 1 raqam va 1 katta harf."""
        if not isinstance(password, str) or len(password) < 8:
            return False
        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        return has_digit and has_upper

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """O'zbekiston formati: +998XXXXXXXXX"""
        if not isinstance(phone, str): return False
        return bool(re.match(r"^\+998\d{9}$", phone))

    @staticmethod
    def validate_username(username: str) -> bool:
        r"""3-15 belgi, harf bilan boshlanishi kerak, faqat \w (harf, son, _)."""
        if not isinstance(username, str) or not (3 <= len(username) <= 15):
            return False
        return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", username))

    @staticmethod
    def validate_birth_year(year: int) -> bool:
        """1900 dan hozirgi yilgacha bo'lgan diapazon."""
        current_year = datetime.now().year
        if not isinstance(year, int):
            return False
        return 1900 <= year <= current_year