from rest_framework.test import APIClient
import environ

env = environ.Env()
env.read_env('.env')

class Api_method:
    traffic = env('API_TRAFFIC')
    host = env('API_HOST')
    base_url = traffic + "://" + host + "/"

    def auth(self, user):
        """
        認証処理をおこない、JWTを取得する
        """
        client = APIClient()
        url = self.base_url + "v1/token/"
        data = {
            "email": user.email,
            "password": user.password
        }
        print(url)
        response = client.post(url, data)
        print(response)



    def get(self, url, token, params):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)
        client.get(url, params, format="json")