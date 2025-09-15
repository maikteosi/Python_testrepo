import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv('BASE_URL', 'https://ru.yougile.com/api-v2')
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    COMPANY_ID = os.getenv('COMPANY_ID')
    API_KEY = os.getenv('API_KEY')

    TEST_PROJECT_TITLE = "Test Project " + str(os.getpid())
    TEST_PROJECT_UPDATED_TITLE = "Updated Test Project " + str(os.getpid())
