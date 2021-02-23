import requests
from requests import Session

from settings import IP_SIT, USERNAME, PASSWORD


class Base:
    def __init__(self):
        self.s = Session()
        self.ip = IP_SIT
        self.username = USERNAME
        self.password = PASSWORD
        self.s.headers["Token"] = self.get_token()

    def get_token(self, username=None, password=None):
        """
        获取用户登录 token
        :param username: 用户名
        :param password: 密码
        :return: token
        """
        if username is None:
            username = self.username
        if password is None:
            password = self.password

        login_url = self.ip + "/api/user/mis/login.do"

        login_params = {"username": username, "password": password}

        r = requests.get(url=login_url, params=login_params)

        return r.json()["data"]["loginUser"]["token"]


if __name__ == '__main__':
    test = Base()
    test.get_token()
