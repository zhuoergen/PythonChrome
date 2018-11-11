# add some explaination

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.weibo.com/login.php')
elem = browser.find_element_by_id(id_='loginname')
elem.send_keys('your_username')
elem_psw = browser.find_element_by_name('your_password')
