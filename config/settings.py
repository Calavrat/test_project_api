import os
from dotenv import load_dotenv

load_dotenv()
LISTEN_NETWORK_URL =os.getenv('LISTEN_NETWORK_URL', 'https://osinit.com/#home') 
NETWORK_URL=os.getenv('NETWORK_URL', 'https://reqres.in/')
LOGIN_URL=os.getenv('LOGIN_URL', 'https://zimaev.github.io/pom/') 
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

