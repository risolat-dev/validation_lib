# Custom Validation Library (TDD Approach)

Ushbu kutubxona foydalanuvchi ma'lumotlarini (Username, Email, Password, Phone, Birth Year) qat'iy mantiqiy qoidalar asosida tekshirish uchun mo'ljallangan. Loyiha **Test-Driven Development (TDD)** metodologiyasi asosida ishlab chiqilgan va 100% test qamroviga ega.

## 🚀 Xususiyatlari
* **Username Validation:** 3-15 belgi, harf bilan boshlanishi va xavfsiz belgilarni tekshirish.
* **Email Validation:** Format va ma'lumot turlarini qat'iy tekshirish.
* **Password Complexity:** Kamida 8 belgi, kamida bitta raqam va bitta katta harf mavjudligini nazorat qilish.
* **Phone Validation:** O'zbekiston telefon raqamlari formati (+998).
* **Birth Year Validation:** Tug'ilgan yilning mantiqiy diapazonda ekanligini (1900 dan joriy yilgacha) tekshirish.

## 🛠 Texnologiyalar
* **Python 3.13+**
* **Pytest**: Unit testlarni tashkil qilish uchun.
* **Pytest-Cov**: Test qamrovini (Coverage) o'lchash va hisobot yaratish uchun.

## 📊 Test Natijalari
Loyiha har bir mantiqiy qatorni qamrab olgan unit testlar bilan ta'minlangan. Pytest orqali olingan yakuniy natijalar:

```text
Name                Stmts   Miss  Cover
--------------------------------------
src/validator.py       31      0   100%
--------------------------------------
TOTAL                  31      0   100%

================== 19 passed in 0.03s ==================