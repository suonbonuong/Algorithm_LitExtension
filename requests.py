import requests
url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php?redirect_to=http%3A%2F%2F45.79.43.178%2Fsource_carts%2Fwordpress%2Fwp-admin%2F&reauth=1'
login_data = {'log': 'admin', 'pwd': '123456aA'}
with requests.Session() as s:
    resp = s.post(url, data = login_data)
    resp = s.get(url)
data = resp.request.headers.get("Cookie")
print(data[data.find('=') + 1:data.find('%')])
