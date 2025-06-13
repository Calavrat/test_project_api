from config import settings 
from playwright.sync_api import Playwright, sync_playwright, expect,Page, BrowserContext
import requests
import pages.model.orange_model as model
import logging
from dotenv import set_key, load_dotenv

def getToken():
    response  = requests.post(settings.ORANGE_URL, json=model.payload)
    assert response.status_code==201, f'Login failed {response.text}' 
    # logging.info(response.json())
    dotenv_path = '/home/hama/Документы/PythonTests/playwright_project_2/config/.env'
    set_key(dotenv_path, 'ACCESS_TOKEN', response.json()['accessToken'])
    set_key(dotenv_path, 'REFRESH_TOKEN', response.json()['refreshToken'])

class OrangePage():

    def __init__(self, page: Page):
        self.page = page
        self._setup_auth_headers()

    def _setup_auth_headers(self):
        getToken()
        # Устанавливаем заголовки для всех запросов через context
        self.page.context.set_extra_http_headers({
            "Authorization": f"Bearer {settings.ACCESS_TOKEN}"
         })

    def login(self):
        response = self.page.request.get(settings.TODOS)
        logging.info(response.status)
        logging.info(response.json())
        # expect(self.page.get_by_role("heading", name="Dashboard")).to_have_text("Dashboard")