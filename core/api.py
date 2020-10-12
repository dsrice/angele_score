from rest_framework.test import APIClient
from rest_framework import status
import environ

env = environ.Env()
env.read_env('.env')


class Api_method:
    traffic = env('API_TRAFFIC')
    host = env('API_HOST')
    base_url = traffic + "://" + host + "/"

    def auth(self, email, password):
        """
        認証処理をおこない、JWTを取得する
        """
        client = APIClient()
        url = self.base_url + "v1/token/"
        print(url)
        data = {
            "email": email,
            "password": password
        }
        response = client.post(url, data)
        if response.status_code == status.HTTP_200_OK:
            return "JWT " + response.data["token"]
        else:
            return None

    def get(self, url, token, params):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)
        client.get(url, params, format="json")
