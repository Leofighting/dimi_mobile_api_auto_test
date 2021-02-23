import requests

login_url = "https://scm-dev.newpearl.com/api/user/mis/login.do"
login_param = {
    "username": "18819151992",
    "password": "123456"
}

r = requests.post(url=login_url, params=login_param)
print(r.json())