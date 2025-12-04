# SolarAutomation / Автоматизация тестирования сайта Solar PV Energy

![Python](https://img.shields.io/badge/python-3.10-blue)
![Pytest](https://img.shields.io/badge/pytest-tests-brightgreen)
![Selenium](https://img.shields.io/badge/selenium-webdriver-yellow)
![Allure](https://img.shields.io/badge/allure-report-orange)
![Status](https://img.shields.io/badge/status-in--progress-lightgrey)

---

## 📝 Project Description / Описание проекта

This is a **learning project** for automating the website [Solar PV Energy](http://saveenergyeo.atwebpages.com).  
It uses **Python**, **Selenium**, **Pytest**, and **Allure** for UI testing.

Это **учебный проект** по автоматизации сайта [Solar PV Energy](http://saveenergyeo.atwebpages.com).  
Используются **Python**, **Selenium**, **Pytest** и **Allure** для тестирования интерфейса.

---

## ⚙️ Features / Возможности

- UI testing of Home and Contact pages / UI-тестирование страниц Home и Contact  
- Verification of form fields, placeholders, and input data / Проверка полей формы, плейсхолдеров и введённых данных  
- Video presence and playback check on the homepage / Проверка наличия и воспроизведения видео на главной странице  
- Navigation between pages / Переход между страницами  
- Logging with Python logger and integration with Allure reports / Логирование с помощью Python logger и интеграция с отчётами Allure

---

## 📂 Project Structure / Структура проекта
```
📂 project/
│
├─ pages/            # Page Objects / Страницы для Page Object Model
├─ tests/            # Test cases / Тесты
├─ utils/            # Utility functions and logger / Вспомогательные функции и логгер
├─ config/           # Constants and configurations / Константы и конфигурации
├─ website/          # Static website files / Файлы веб-сайта для локального тестирования
├─ .gitignore
└─ README.md
```


---

## 🚀 Getting Started / Начало работы

1. **Clone the repository / Клонировать репозиторий**

```bash
git clone https://github.com/AzNavyr/PROJECT.git
cd PROJECT
```

2. **Create and activate virtual environment / Создать и активировать виртуальное окружение**
```
python -m venv .venv
```
#Windows
```
.venv\Scripts\activate
```


#Mac/Linux
```
source .venv/bin/activate
pip install -r requirements.txt
```
3. **Install dependencies / Установить зависимости**

```
pytest tests/ --alluredir=allure-results
```

4. **Run tests with Pytest / Запуск тестов с Pytest**
```
pytest tests/ --alluredir=allure-results
```

5. **Generate Allure report / Генерация отчета Allure**
```
allure serve allure-results
```


---

## 🔮 Planned Features / Планируемые функции

### API Testing / API-тестирование
In the future, we plan to create a **simple API** for the Solar PV Energy project.  
В будущем планируется создать **простой API** для проекта Solar PV Energy.

The API will include **4 basic methods** / API будет включать 4 базовых метода:

1. **GET /contacts** – retrieve all contact requests / получить все запросы на обратный звонок  
2. **POST /contacts** – create a new contact request / создать новый запрос на обратный звонок  
3. **PUT /contacts/{id}** – update an existing contact request / обновить существующий запрос  
4. **DELETE /contacts/{id}** – delete a contact request / удалить запрос на обратный звонок

---

### Database Integration / Интеграция с базой данных
We plan to implement a **small local database** to store form submissions.  
Планируется создание **небольшой локальной базы данных** для хранения данных форм.

- Store contact requests / Хранение запросов обратного звонка  
- Track form submissions / Отслеживание отправки форм  
- Provide data for API endpoints / Предоставление данных для API эндпоинтов
