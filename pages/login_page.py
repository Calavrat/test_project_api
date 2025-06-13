from config import settings 
from playwright.sync_api import Playwright, sync_playwright, expect,Page
import logging

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message=page.get_by_text("Invalid credentials. Please")
        

    def navigate(self):
         ###Открываем страницу логина
         self.page.goto(settings.LOGIN_URL) 

    def login(self, username: str, password: str):
        ###Вход на страницу
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        ###Возвращает текст сообщения об
        return self.error_message.inner_text()
    
    def get_url(self):
        self.url = self.page.url
        return self.url

