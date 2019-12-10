import unittest
import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from parameterized import parameterized
from tools.read_txt import read_txt

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api=ApiEmployee()

    @parameterized.expand(read_txt("employee_post.txt"))
    def test001_post(self, username, mobile, workNumber):
    # def test01_post(self,username="bj1211",mobile="13812345678",workNumber="123456"):
        r=self.api.api_post_employee(username,mobile,workNumber)
        print(r.json())
        api.user_id=r.json().get("data").get("id")
        print(api.user_id)
        assert_common(self, r)

    def test002_put(self,username="bj11122"):
        r=self.api.api_put_employee(username)
        print(r.json())
        assert_common(self, r)

    def test003_get(self):
        r=self.api.api_get_employee()
        assert_common(self, r)

    def test004_delete(self):
        r=self.api.api_delete_employee(api.user_id)
        print(r.json())
        assert_common(self,r)