import os
import pickle
import pandas as pd
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# TRuy cập vào fb
driver.get("https://www.facebook.com/")

# Tạo hàm
# Hàm chuyển chế độ xem bình luận
def change_comment_filter_to_all(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # Bước 1: Click mở menu dropdown lọc bình luận
        filter_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[2]/div/div')
        driver.execute_script("arguments[0].scrollIntoView();",
                              filter_button)
        filter_button.click()

        # Bước 2: Chờ menu popup hiện ra, click chọn "Tất cả bình luận"
        all_comments_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]')
        ))
        all_comments_option.click()

        # print("Đã chuyển sang chế độ Tất cả bình luận.")
    except Exception as e:
        print("Lỗi khi chuyển chế độ lọc bình luận:", e)

 # Hiển thị full bình luận
def click_all_view_more(driver):
    while True:
        try:
            btns = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[3]/div[41]/div[1]')
            driver.execute_script("arguments[0].scrollIntoView(true);", btns)
            btns.click()
        except:
            break


def show_all_comments(driver):
    while True:
        buttons = driver.find_elements(By.XPATH, '//div[@role="button" and .//span[starts-with(text(),"Xem thêm") and contains(text(),"bình luận")]]')
        if not buttons:
            # print("Đã hết nút 'Xem thêm bình luận'.")
            break
        for btn in buttons:
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
            sleep(2)
            try:
                btn.click()
                sleep(2)
            except:
                continue

# Hàm lấy bình luận
def get_comments(driver):
    comments_data = []
    comment_blocks = driver.find_elements(By.XPATH, "//div[@role='article']")

    for block in comment_blocks:
        try:
            # click xem thêm
            try:
                see_more_buttons = block.find_elements(
                    By.XPATH, './/div[@role="button" and (text()="Xem thêm")]'
                )
                if see_more_buttons:
                    for btn in see_more_buttons:
                        driver.execute_script("arguments[0].click();", btn)
                        sleep(1)
            except Exception as e:
                print(f"Không bấm được 'Xem thêm' {e}")

            # Lấy tên người bình luận
            try:
                author_elem = block.find_elements(By.XPATH, './/span[@dir="auto" and not(ancestor::form)]')
                author = author_elem[0].text if author_elem else ""
            except:
                author = ""

            # Lấy nội dung comment (ghép các dòng lại)
            try:
                content_elements = block.find_elements(By.XPATH, './/div[@dir="auto" and not(ancestor::form)]')
                content = "\n".join([elem.text for elem in content_elements if elem.text.strip()])
            except:
                content = ""

            # Lấy thời gian đăng (ngày giờ chi tiết nếu có)
            # try:
            #     time_element = block.find_element(By.XPATH, './/a[contains(@href, "comment_id=")]')
            #     print("[+] Tìm thấy thẻ thời gian:", time_element.text)
            #
            #     # Di chuột để hiển thị tooltip
            #     ActionChains(driver).move_to_element(time_element).perform()
            #     sleep(0.5)  # chờ tooltip hiển thị
            #
            #     aria_describedby = time_element.get_attribute("aria-describedby")
            #     print("aria-describedby:", aria_describedby)
            #
            #     if aria_describedby:
            #         tooltip_elem = WebDriverWait(driver, 3).until(
            #             EC.presence_of_element_located((By.ID, aria_describedby))
            #         )
            #         posted_time = tooltip_elem.text.strip()
            #         print(f"Lấy được tooltip DOM: {posted_time}")
            #     else:
            #         # Thử lấy bằng các thuộc tính khác nếu aria-describedby không tồn tại
            #         posted_time = (
            #                 time_element.get_attribute("aria-label") or
            #                 time_element.get_attribute("title") or
            #                 time_element.get_attribute("data-tooltip-content") or
            #                 ""
            #         ).strip()
            #         print(f"[•] Không có aria-describedby, thử lấy từ thuộc tính khác: {posted_time}")
            #
            # except Exception as e:
            #     print(f"[!] Không lấy được posted_time: {repr(e)}")
            #     posted_time = ""
            posted_time = ""

            # Lấy link của bình luận
            try:
                comment_link_elem = block.find_element(By.XPATH, './/a[contains(@href, "comment_id=")]') # dùng thẻ comment_id
                comment_link = comment_link_elem.get_attribute("href")
            except:
                comment_link = ''

            crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if content:  # Chỉ lấy comment có nội dung
                comments_data.append({
                    'link': comment_link,
                    'author': author,
                    'content': content,
                    'posted_time': posted_time,
                    'crawl_time': crawl_time
                })
                # print(f"author: {author}\ncontent: {content}\nposted_time: {posted_time}\ncrawl_time: {crawl_time}\n")

        except Exception as e:
            print(f"[Lỗi khi xử lý 1 comment block] ")

    return comments_data

sleep(5)


#-----------------------------------------------
# Tải lại cookies
with open("fb_cookies.pkl", "rb") as f:
    cookies = pickle.load(f)
for cookie in cookies:
    if 'sameSite' in cookie:
        del cookie['sameSite']
    driver.add_cookie(cookie)

driver.refresh()
# sleep(5)

# Lưu kết quả
def save_output(data, output):
    df_result = pd.DataFrame(data, columns=['link', 'author', 'content', 'posted_time', 'crawl_time'])
    if os.path.exists(output):
        old_df = pd.read_excel(output)
        new_df = pd.concat([old_df, df_result], ignore_index=True)
    else:
        new_df = df_result

    new_df.to_excel(output, index=False)
    return output

# Mở bài viết và crawl
input = 'tuyen_dung.xlsx'
output = 'output.xlsx'
df = pd.read_excel(input, header = None, sheet_name = 'ung_tuyen')
data = []
for index, row in df.iterrows():
    if int(index) >= 58:
        print(int(index)+1)
        path = row[0]
        try:
            driver.get(path)
            sleep(1)
            change_comment_filter_to_all(driver)
            sleep(1)
            show_all_comments(driver)
            sleep(1)
            data = get_comments(driver)
            save_output(data, output)
        except Exception as e:
            print('Lỗi khi xử lý bài viết', e)
driver.close()
print('Đã lưu vào file excel')

