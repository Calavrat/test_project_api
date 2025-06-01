from config import settings 
from playwright.sync_api import Playwright, sync_playwright, Page
import logging
import time
import pages.model.dummy_model as model
import json

def send_api_request(context, method, url, data=None, headers=None, max_retries=3):
    """
    Отправляет API-запрос и автоматически обрабатывает 429 ошибку.
    """
    for attempt in range(1, max_retries + 1):
        logging.info(f"Попытка {attempt} — Запрос: {method} {url}")
        
        if method.upper() == 'POST':
            response = context.request.post(url, data=data, headers=headers)
        elif method.upper() == 'GET':
            response = context.request.get(url)
        else:
            raise ValueError(f"Метод '{method}' не поддерживается")

        if response.status == 429:
            logging.warning("Получен 429 Too Many Requests. Жду 30 секунд...")
            time.sleep(5)
        else:
            return response

    raise Exception(f"Не удалось выполнить запрос после {max_retries} попыток")

class DummyPage:
    def __init__(self, page: Page):
        self.page = page

#API список всех ресурсов
    def getPosts(self):
        response = self.page.request.get(settings.GET_POSTS)
        if response.status == 429:
             time.sleep(5)
             response = self.page.request.get(settings.GET_POSTS)

        logging.info(f'Статус код: {response.status}')
        logging.info(response.json())
#API создание ресурса
    def createPost(self):
        response=self.page.request.post(settings.CREATE_POST, data = json.dumps(model.dataCreate), headers=model.headers) 
        logging.info(f'Статус код: {response.status}')
        if response.status == 429:
             time.sleep(20)
             response=self.page.request.post(settings.CREATE_POST, data = json.dumps(model.dataCreate), headers=model.headers) 

        content_type = response.headers.get('content-type', '')
        # logging.info(f'Content-Type:" {content_type}')
        if 'application/json' in content_type:
            try:
                data = response.json()
                logging.info(f'JSON Response: {data}')
                post_id = data.get("data", {}).get("id")
                if post_id:
                    logging.info(f'Созданный ID ресурса: {post_id}')
                    # get_url = settings.GET_EMPLOYEE_DUMMY_URL.replace('&',str(21))
                    # print(get_url)
                    # get_response = send_api_request(self.page, method='GET', url=get_url)

                    # logging.info(f'Статус код: {get_response.status}')
                    # logging.info(f'Cотрудник c id 21: {get_response.json()}')
            except json.JSONDecodeError:
                logging.info(f"Ошибка: Не удалось распарсить JSON")
        else:
            logging.info(f"Ошибка: Получен не JSON-ответ")
            logging.info(f'Текст ответа: {response.text()}')

#API Получение ресурса по id  
    def getPost(self, get_id: str):
        get_url = settings.GET_POST.replace('&',get_id)
        response = send_api_request(self.page, method='GET', url=get_url)
        logging.info(f'Статус код: {response.status}')
        logging.info(f'Ресурс c id {get_id}: {response.json()}')

#API Удаление сотрудника
    def deletePost(self, delete_id: str):
        get_url = settings.DELETE_POST.replace('&', delete_id)
        response = self.page.request.delete(get_url)
        logging.info(f'Статус код: {response.status}')
        logging.info(f'Ответ об удалении {response.json()}')