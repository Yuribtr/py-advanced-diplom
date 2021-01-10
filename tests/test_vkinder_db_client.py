import unittest
from unittest import mock
from tests.mock_server import get_free_port, start_mock_server
from сlasses.vk_api_classes import VKinderClient
from сlasses.vk_api_client import VkApiClient
from сlasses.vkinder_db_client import VKinderDb


class TestVKinderDb(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = VKinderDb('test', 'test', 'test', debug_mode=True)
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

    def test_client_save_load(self):
        assert self.db.is_initialized
        mock_users_url = 'http://localhost:{port}/'.format(port=self.mock_server_port)
        with mock.patch('сlasses.vk_api_client.VkApiClient.API_BASE_URL', new_callable=mock.PropertyMock) as mock_f:
            mock_f.return_value = mock_users_url
            self.api = VkApiClient(token='', app_id='', user_id='1', debug_mode=True)
            assert self.api.is_initialized
            users = self.api.get_users('1')
            assert len(users) == 1
            user = self.api.get_users('1')[0]
            client = VKinderClient(user)
            self.db.save_client(client)
            client_db = self.db.load_client_from_db('1')
            assert client_db
            client = VKinderClient(client_db)
            assert client.vk_id == '1'
            assert client.fname == 'Павел'
            assert client.lname == 'Дуров'
