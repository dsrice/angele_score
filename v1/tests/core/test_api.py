from django.test import TestCase
from core.api import Api_method
from bowring.models.users import User

class APICoreCase(TestCase):

    def accesstest(self):
        user = User.objects.get(email="test@xxx.xx")
        api = Api_method()
        token = api.auth(user)
        print(token)


case = APICoreCase()
case.accesstest()
