import os
from dotenv import load_dotenv

load_dotenv()
LISTEN_NETWORK_URL =os.getenv('LISTEN_NETWORK_URL', 'https://osinit.com/#home') 
NETWORK_URL=os.getenv('NETWORK_URL', 'https://reqres.in/')
LOGIN_URL=os.getenv('LOGIN_URL', 'https://zimaev.github.io/pom/') 
GET_POSTS = os.getenv('GET_POSTS', 'https://jsonplaceholder.typicode.com/posts')
GET_POST = os.getenv('GET_POST', 'https://jsonplaceholder.typicode.com/posts/&')
CREATE_POST = os.getenv('CREATE_POST', 'https://jsonplaceholder.typicode.com/posts')
DELETE_POST = os.getenv('DELETE_POST','https://jsonplaceholder.typicode.com/posts/&')
ORANGE_URL = os.getenv('ORANGE_URL','http://2.59.41.2:4300/api/login')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN','')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN', '')
TODOS = os.getenv('TODOS','http://2.59.41.2:4300/api/todos/1011')
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

