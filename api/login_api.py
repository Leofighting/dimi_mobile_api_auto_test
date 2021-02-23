import requests

from api.base import Base


class Login(Base):
    def login_with_password(self):
        """
        使用 用户名、密码 登录
        :return:
        """
        login_url = self.ip + "/api/user/mis/login.do"
        login_params = {"username": self.username, "password": self.password}
        r = requests.post(url=login_url, params=login_params)
        return r.json()