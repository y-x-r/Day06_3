def assert_common(self,response,status_code=200,msg="操作成功！"):
    self.assertEqual(status_code,response.status_code)

    self.assertTrue(response.json().get("success"))

    self.assertEqual(10000,response.json().get("code"))

    self.assertEqual(msg,response.json().get("message"))
