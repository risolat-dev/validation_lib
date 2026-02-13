from src.validator import Validator

def run_demo():
    print("=" * 50)
    print("🚀 CUSTOM VALIDATION LIBRARY - FULL DEMO")
    print("=" * 50)

    # Barcha turdagi test ma'lumotlari
    test_cases = {
        "USERNAMES": [
            "risolat_dev",      # To'g'ri
            "1user",            # Xato (Raqam bilan boshlangan)
            "ab"                # Xato (Juda qisqa)
        ],
        "EMAILS": [
            "risolat@mail.uz",  # To'g'ri
            "not-an-email.com", # Xato (Format noto'g'ri)
            "user@.com"         # Xato (Domen noto'g'ri)
        ],
        "PASSWORDS": [
            "StrongPass123",    # To'g'ri
            "weak123",          # Xato (Katta harf yo'q)
            "NoDigitsHere"      # Xato (Raqam yo'q)
        ],
        "PHONE NUMBERS": [
            "+998901234567",    # To'g'ri
            "998901112233",     # Xato (+ yo'q)
            "+99890123"         # Xato (Raqam kam)
        ],
        "BIRTH YEARS": [
            2000,               # To'g'ri
            1850,               # Xato (Juda eski)
            2030                # Xato (Kelajak yili)
        ]
    }

    # 1. Username tekshiruvi
    print("\n👤 [USERNAME VALIDATION]:")
    for user in test_cases["USERNAMES"]:
        is_valid = Validator.validate_username(user)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"   {str(user):<25} -> {status}")

    # 2. Email tekshiruvi
    print("\n📧 [EMAIL VALIDATION]:")
    for email in test_cases["EMAILS"]:
        is_valid = Validator.validate_email(email)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"   {str(email):<25} -> {status}")

    # 3. Parol tekshiruvi
    print("\n🔑 [PASSWORD VALIDATION]:")
    for pwd in test_cases["PASSWORDS"]:
        is_valid = Validator.validate_password(pwd)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"   {str(pwd):<25} -> {status}")

    # 4. Telefon raqami tekshiruvi
    print("\n📞 [PHONE VALIDATION]:")
    for phone in test_cases["PHONE NUMBERS"]:
        is_valid = Validator.validate_phone(phone)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"   {str(phone):<25} -> {status}")

    # 5. Tug'ilgan yil tekshiruvi
    print("\n📅 [BIRTH YEAR VALIDATION]:")
    for year in test_cases["BIRTH YEARS"]:
        is_valid = Validator.validate_birth_year(year)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"   {str(year):<25} -> {status}")

    print("\n" + "=" * 50)
    print("🎯 Barcha Production-ready tekshiruvlar yakunlandi.")
    print("=" * 50)


if __name__ == "__main__":
    run_demo()