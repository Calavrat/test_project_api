from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect
from config import settings 
import logging
from utils import network

##Мониторинг сетевых запросов
# def test_listen_network(page: Page):
#     page.on('request', lambda request: print('>>', request.method, request.url))
#     page.on('response', lambda response: print('<<', response.status, response.url))
#     page.goto(settings.LISTEN_NETWORK_URL)

## Фильтрация и прерывания запроса к маршруту
# def test_filter_listen_network(page: Page):
#     #Если нужно заблокировать несколько ресурсов  utils/network.py
#     #network.block_resources(page, types=["script"])
#     #Если нужно заблокировать конкретный один ресурс
#     page.route("**/*.svg", network.handle_block)
#     page.goto(settings.LISTEN_NETWORK_URL)   

##Подмена тела запроса
#def  test_replace_body(page: Page):
#Без логирования
#   page.route('**/register', lambda route: route.continue_(post_data='{"email: "user", "password":"password"}'))
#С логированием
    # page.route('**/register', network.override_request('data/new_data_request.json'))
    # page.goto(settings.NETWORK_URL)
    # page.get_by_text('Register - successful').click()

def test_mock(page: Page): 
#С логированием
    page.route("**/register", network.mock_reponce_from_file('data/new_data_response.json'))
    page.goto(settings.NETWORK_URL)
    page.get_by_text('Register - successful').click()
