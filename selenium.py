from selenium import webdriver
from bs4 import BeautifulSoup
import time
url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php?redirect_to=http%3A%2F%2F45.79.43.178%2Fsource_carts%2Fwordpress%2Fwp-admin%2F&reauth=1'
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
user = 'admin'
password = '123456aA'
driver.get(url)
text_user = driver.find_element_by_id("user_login").send_keys(user)
text_password = driver.find_element_by_id("user_pass").send_keys(password)
text_user = driver.find_element_by_id("wp-submit").submit()
time.sleep(5)
html = driver.page_source
tree = BeautifulSoup(markup=html)
result = tree.find('span', attrs={"class": "display-name"})
print(result.text)
driver.close()
