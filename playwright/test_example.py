# ФИО: Щетинин Сергей Витальевич 
# Дата: 2026-11-09
# Время: 20:02
# Описание: Тест запускает браузер Chrome в фоновом режиме, открывает страницу и проверяет правильность её работы
# Я скопировал пример из раздела "Writing tests" и запустил его локально.

import pytest
from playwright.sync_api import Page, expect

# Фикстура автоматически готовит браузер перед стартом каждого теста
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # 
    page.goto("https://playwright.dev/")
    yield

    # Код, который сработает сразу после окончания теста
    print("after the test runs")

# Тест проверяет что переход был по нужному адресу
def test_main_navigation(page: Page):
    # 
    expect(page).to_have_url("https://playwright.dev/")