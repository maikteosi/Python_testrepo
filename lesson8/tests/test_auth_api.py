import pytest
import requests
from src.yougile_api import AuthApi
from src.config import Config


class TestAuthApi:
    @pytest.fixture
    def auth_api(self):
        return AuthApi(Config.BASE_URL, Config.LOGIN, Config.PASSWORD)

    def test_auth_api_initialization(self):
        auth_api = AuthApi(Config.BASE_URL, Config.LOGIN, Config.PASSWORD)
        assert auth_api.base_url == Config.BASE_URL
        assert auth_api.login == Config.LOGIN
        assert auth_api.password == Config.PASSWORD

    def test_auth_api_initialization_without_password(self):
        auth_api = AuthApi(Config.BASE_URL, Config.LOGIN)
        assert auth_api.base_url == Config.BASE_URL
        assert auth_api.login == Config.LOGIN
        assert auth_api.password is None

    # def test_create_api_key_success(self, auth_api):
        if not all([Config.COMPANY_ID, Config.LOGIN, Config.PASSWORD]):
            pytest.skip("Auth credentials not configured")
        response = auth_api.create_api_key(Config.COMPANY_ID)
        assert response.status_code == 201
        data = response.json()
        assert 'key' in data
        assert len(data['key']) > 20

    def test_get_api_keys_success(self, auth_api):
        if not all([Config.COMPANY_ID, Config.LOGIN, Config.PASSWORD]):
            pytest.skip("Auth credentials not fully configured")
        keys = auth_api.get_api_keys(Config.COMPANY_ID)
        assert isinstance(keys, list)
        if keys:
            key = keys[0]
            assert 'companyId' in key
            assert 'key' in key
            assert 'timestamp' in key
            assert key['companyId'] == Config.COMPANY_ID
            assert len(key['key']) > 20

    def test_create_api_key_invalid_credentials(self):
        auth_api = AuthApi(
            Config.BASE_URL, "invalid_login", "invalid_password")
        response = auth_api.create_api_key(Config.COMPANY_ID)
        assert response.status_code in [400, 401]

    def test_get_api_keys_invalid_credentials(self):
        auth_api = AuthApi(
            Config.BASE_URL, "invalid_login", "invalid_password")
        with pytest.raises(requests.exceptions.HTTPError):
            auth_api.get_api_keys(Config.COMPANY_ID)
