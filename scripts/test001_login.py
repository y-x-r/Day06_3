import unittest

import api
from api.api_login import ApiLogin

from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login=ApiLogin()

    def test01_login(self,mobile="13800000002",password="123456"):
        r=self.login.api_login(mobile,password)
        print(r.json())

        token=r.json().get("data")
        api.headers["Authorization"]="Bearer " + token
        print("登录成功后的headers的值为:",api.headers)

        assert_common(self,r)

