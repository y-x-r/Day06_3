import requests

import api


class ApiEmployee:
    def __init__(self):
        self.url_add=api.BASE_URL+"/api/sys/user"
        self.url_employee=api.BASE_URL+"/api/sys/user/{}"

    def api_post_employee(self,username,mobile,workNumber):
        data={
            "username":username,"mobile":mobile,"workNumber":workNumber
        }
        return requests.post(url=self.url_add,json=data,headers=api.headers)

    def api_put_employee(self,username):
        data={"username":username}
        return requests.put(url=self.url_employee.format(api.user_id),json=data,headers=api.headers)

    def api_get_employee(self):
        return requests.get(url=self.url_employee.format(api.user_id),headers=api.headers)

    def api_delete_employee(self,user_id):
        return requests.delete(url=self.url_employee.format(user_id),headers=api.headers)
