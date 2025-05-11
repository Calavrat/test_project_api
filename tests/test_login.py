import logging
import pytest
import allure
from config import settings 
@allure.epic('Эпик задачи')
@allure.story('Авторизация')
@allure.title('Авторизация с невалидными данными')
@allure.description('Тест входа с невалидными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Вход с невалидными данными'):
        logging.info('Проверка логирования с невалидными данными')
        login_page.login('user', 'password')
    with allure.step('URL не изменился'):
        assert login_page.get_url() == settings.LOGIN_URL
    with allure.step('Проверка отображения ошибки - Invalid credentials. Please try again.'):
        logging.info('Проверка сообщения об ошибке')
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'

@allure.epic('Эпик задачи')
@allure.story('Авторизация')
@allure.title('Авторизация с валидными данными')
@allure.description('Тест входа с валидными данными')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('username, password',[
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Вход с валидными данными'):
        logging.info('Проверка логирования с валидными данными')
        login_page.login(username, password)
    with allure.step('Проверка отображения приветсвенного сообщения с именем профиля'):
        dashboard_page.assert_welcome_message(f'Welcome {username}')
