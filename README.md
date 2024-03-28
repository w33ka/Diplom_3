## Дипломный проект. Задание 3: UI-тесты

### UI тесты для Stellar Burgers

### Структура проекта

- `allure-report` 
- `allure-results`
- `locators`
- `pages`
- `tests` - пакет, содержащий тесты:
  - `test_main_functionality.py`
  - `test_order_feed.py`
  - `test_profile.py`
  - `test_restore_password.py` 
- `conftest.py`
- `data.py`
- `helpers.py`
- `requirements.txt`
- `README.md`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

>  `$pytest -v ./tests`