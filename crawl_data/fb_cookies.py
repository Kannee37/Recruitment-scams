from selenium import webdriver
import pickle
import time

# Mở trình duyệt
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login.php?next=/login")

# Dừng lại để bạn đăng nhập thủ công
input("Vui lòng đăng nhập Facebook, sau đó nhấn Enter để tiếp tục...")

#Lưu cookies sau khi đăng nhập thành công
with open('fb_cookies.pkl', 'wb') as f:
    pickle.dump(driver.get_cookies(), f)

print("Đã lưu cookies vào fb_cookies.pkl.")
driver.quit()
