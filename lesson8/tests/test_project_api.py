import pytest
from src.yougile_api import ProjectApi
from src.config import Config


class TestProjectApi:
    @pytest.fixture
    def project_api(self):
        if not Config.API_KEY:
            pytest.skip("API_KEY not configured")
        return ProjectApi(Config.BASE_URL, Config.API_KEY)

    @pytest.fixture
    def test_project_id(self, project_api):
        response = project_api.create_project(Config.TEST_PROJECT_TITLE)
        assert response.status_code in [200, 201]
        project_data = response.json()
        project_id = project_data['id']
        yield project_id
        try:
            project_api.delete_project(project_id)
        except Exception:
            pass

    def test_project_api_initialization(self):
        if not Config.API_KEY:
            pytest.skip("API_KEY not configured")
        project_api = ProjectApi(Config.BASE_URL, Config.API_KEY)
        assert project_api.base_url == Config.BASE_URL
        assert project_api.api_key == Config.API_KEY

    def test_create_project_success(self, project_api):
        response = project_api.create_project(Config.TEST_PROJECT_TITLE)
        assert response.status_code in [200, 201]
        data = response.json()
        assert 'id' in data
        if 'title' in data:
            assert data['title'] == Config.TEST_PROJECT_TITLE
        project_api.delete_project(data['id'])

    def test_create_project_unauthorized(self):
        project_api = ProjectApi(Config.BASE_URL, "invalid_api_key")
        response = project_api.create_project(Config.TEST_PROJECT_TITLE)
        assert response.status_code in [401, 403]

    def test_get_project_success(self, project_api, test_project_id):
        response = project_api.get_project(test_project_id)
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == test_project_id
        if 'title' in data:
            assert data['title'] == Config.TEST_PROJECT_TITLE

    def test_get_project_not_found(self, project_api):
        response = project_api.get_project("non_existent_project_id")
        assert response.status_code == 404

    def test_update_project_success(self, project_api, test_project_id):
        response = project_api.update_project(
            test_project_id,
            Config.TEST_PROJECT_UPDATED_TITLE
        )
        assert response.status_code == 200
        data = response.json()
        if 'title' in data:
            assert data['title'] == Config.TEST_PROJECT_UPDATED_TITLE
        get_response = project_api.get_project(test_project_id)
        get_data = get_response.json()
        if 'title' in get_data:
            assert get_data['title'] == Config.TEST_PROJECT_UPDATED_TITLE

    def test_get_all_projects_success(self, project_api, test_project_id):
        response = project_api.get_all_projects()
        assert response.status_code == 200
        data = response.json()
        assert 'content' in data
        assert isinstance(data['content'], list)
        get_response = project_api.get_project(test_project_id)
        assert get_response.status_code == 200
        project_data = get_response.json()
        assert project_data['id'] == test_project_id

    def test_update_project_not_found(self, project_api):
        response = project_api.update_project(
            "non_existent_project_id",
            "Новое название"
        )
        assert response.status_code == 404

    def test_update_project_unauthorized(self):
        project_api = ProjectApi(Config.BASE_URL, "invalid_api_key")
        response = project_api.update_project(
            "some_project_id",  # Любой ID
            "Новое название"
        )
        assert response.status_code in [401, 403]
