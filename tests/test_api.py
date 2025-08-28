import allure

@allure.story('Тестирование api')
@allure.title('Получение списка ресурсов')
@allure.description('По ендпоинтУ получить список ресурсов')
@allure.severity(allure.severity_level.MINOR)
def test_list_posts(dummy_page):
    with allure.step('Получение списка ресурсов'):
        dummy_page.getPosts()

@allure.story('Тестирование api')
@allure.title('Создание вбфывюбфывюбфы нового ресурса')
@allure.description('По ендпоинту создать ресурс ')
def test_create_post(dummy_page):
    with allure.step('Создание нового ресурса и проверка то что он создан'):
        dummy_page.createPost()

@allure.story('Тестирование api')
@allure.title('Получить ресурс по id')
@allure.description('По ендпоинту получить ресурс по id')
def test_get_post(dummy_page):
    with allure.step('Получение ресурса по id'):
        dummy_page.getPost('21')

@allure.story('Тестирование api')
@allure.title('Удаление ресурса по id')
@allure.description('По ендпоинту удалить ресурс')
def test_delete_post(dummy_page):
    with allure.step('Удаление ресурса по id'):
        dummy_page.deletePost('21')