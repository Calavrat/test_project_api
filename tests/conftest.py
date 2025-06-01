import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import logging
from playwright.sync_api import sync_playwright
from config import settings
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.dummy_page import DummyPage
@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def dummy_page(page):
    return DummyPage(page)

# Настройка логирования
if settings.DEBUG:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()]
    )
else:
    logging.basicConfig(level=logging.INFO)

@pytest.fixture(autouse=True)
def log_test_start(request):
    browser_name = request.node.funcargs.get("browser_name", "unknown")
    test_name = request.node.name
    file_path = request.node.fspath  # Полный путь к файлу
    file_name = os.path.basename(file_path)  # Только имя файла
    logging.info(f"Запуск теста: {test_name} | Браузер: {browser_name} | Файл: {file_name}")

@pytest.fixture(scope="session")  
def browser_context_args(browser_context_args):
    return {
      
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

# Хук для логирования ошибок после выполнения каждого теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

# Фикстура, чтобы логировать ошибку после теста
@pytest.fixture(autouse=True)
def log_failure_on_error(request):
    yield
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        # Попробуем получить подробности ошибки
        longrepr = getattr(rep_call, "longrepr", None)

        if hasattr(longrepr, "reprcrash"):
            message = longrepr.reprcrash.message
        else:
            message = str(longrepr)

        logging.error(f"Тест '{request.node.nodeid}' завершился с ошибкой:\n{message}")

