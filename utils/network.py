import json
import logging
from pathlib import Path

### Блокировка для нескольких типов 
def block_resources(page, types: list[str] = None):
    """
    Блокирует загрузку ресурсов по типу (image, font, stylesheet, и т.д.)

    Пример типов:
    - "image" — изображения (png, jpg и т.д.)
    - "font" — шрифты
    - "stylesheet" — CSS
    - "media" — видео и аудио
    - "script" — JavaScript

    Полный список: https://playwright.dev/python/docs/api/class-request#request-resource-type
    """
    #types = types or ["image", "font", "stylesheet"]  # значения по умолчанию

    def handle_route(route, request):
        if request.resource_type in types:
            logging.debug(f"Заблокирован ресурс: {request.url} ({request.resource_type})")
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle_route)
### блокировка для конкретного типа
def handle_block(route, request):
    logging.debug(f"Заблокирован ресурс: {request.url} ({request.resource_type})")
    route.abort()


### Подмена тела запроса из json файла
def override_request(json_path: str):
    
    project_root = Path(__file__).resolve().parent.parent  # предполагаем, что скрипт в /project/utils/ или /project/
    json_file = project_root / json_path
    if not json_file.exists():
        raise FileNotFoundError(f"JSON-файл не найден: {json_path}")

    with open(json_file, "r", encoding="utf-8") as f:
        new_data_dict = json.load(f)
        new_data = json.dumps(new_data_dict)

    def handler(route, request):
        original_post_data = request.post_data
        # method=request.method
        # url=request.url

        logging.debug(f"Переопределение тела запроса: {request.method} {request.url}")
        logging.debug(f"Оригинальные POST-данные: {original_post_data}")
        logging.debug(f"Используется JSON: {json_path}")
        logging.debug(f"Новые данные: {new_data}")
        route.continue_(post_data=new_data)
        

    return handler

##Подмена тела запроса из json-файла
def mock_reponce_from_file(json_path: str, status: int = 200, content_type: str = "application/json"):
    project_root = Path(__file__).resolve().parent.parent  # предполагаем, что скрипт в /project/utils/ или /project/
    json_file = project_root / json_path
    if not json_file.exists():
        raise FileNotFoundError(f"JSON-файл не найден: {json_path}")
    
    with open(json_file, "r", encoding="utf-8") as f:
        new_data_dict = json.load(f)
        new_data = json.dumps(new_data_dict)

    def handler(route, request):
        logging.info(f"Перехват запроса: {request.method} {request.url}")
        logging.info(f"Используется JSON: {json_path}")
        logging.debug(f"Подменённый ответ: {new_data}")

        route.fulfill(
            status=status,
            content_type=content_type,
            body=new_data
        )
    return handler    
