from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 1. Khai báo browser (trình duyệt)
browser = webdriver.Chrome()

# 2. URL của post
path = 'https://www.facebook.com/share/p/16uCpJj3Qi/'

# # 2a. Đăng nhập
# browser.get('https://www.facebook.com/')
#
# txtUser = browser.find_element(By.ID, 'email')
# txtUser.send_keys('nguyenthuytrang372004@gmail.com')
#
# txtPassword = browser.find_element(By.ID, 'pass')
# txtPassword.send_keys('Trang.3724')
#
# txtPassword.send_keys(Keys.ENTER) # nhấn enter sau khi điền username và password

# Truy cập vào bài viết
browser.get(path)
x_off = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/i')
x_off.click()

all_comment = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[2]/div/div')
browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_comment)  #cuộn đến chỗ hiển thị thẻ
sleep(5)
all_comment.click()
all_comment = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]')
all_comment.click()

# Lấy comment


sleep(5)
browser.close()
# browser.get('path')
