import requests
from typing import Optional, List, Dict


class AuthApi:
    def __init__(
              self, base_url: str, login: str, password: Optional[str] = None):
        self.base_url = base_url
        self.login = login
        self.password = password
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

    def create_api_key(self, company_id: str) -> requests.Response:
        """Создание нового ключа API - POST /auth/keys"""
        url = f"{self.base_url}/auth/keys"
        payload = {
            "companyId": company_id,
            "login": self.login
        }

        if self.password:
            payload["password"] = self.password

        response = self.session.post(url, json=payload)
        return response

    def get_api_keys(self, company_id: str) -> List[Dict]:
        """Получение списка ключей API - POST /auth/keys/get"""
        url = f"{self.base_url}/auth/keys/get"
        payload = {
            "companyId": company_id,
            "login": self.login
        }

        if self.password:
            payload["password"] = self.password

        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()


class ProjectApi:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })

    def create_project(self, title: str) -> requests.Response:
        """Создание проекта - POST /projects"""
        url = f"{self.base_url}/projects"
        payload = {"title": title}
        response = self.session.post(url, json=payload)
        return response

    def update_project(self, project_id: str, title: str) -> requests.Response:
        """Изменение проекта - PUT /projects/{id}"""
        url = f"{self.base_url}/projects/{project_id}"
        payload = {"title": title}
        response = self.session.put(url, json=payload)
        return response

    def get_project(self, project_id: str) -> requests.Response:
        """Получение проекта по ID - GET /projects/{id}"""
        url = f"{self.base_url}/projects/{project_id}"
        response = self.session.get(url)
        return response

    def get_all_projects(self) -> requests.Response:
        """Получение всех проектов - GET /projects"""
        url = f"{self.base_url}/projects"
        response = self.session.get(url)
        return response

    def delete_project(self, project_id: str) -> requests.Response:
        """Удаление проекта - DELETE /projects/{id}"""
        url = f"{self.base_url}/projects/{project_id}"
        response = self.session.delete(url)
        return response
