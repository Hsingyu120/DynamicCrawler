# 載入需要的套件
from tkinter import W
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

import time

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
#driver = webdriver.Chrome()
# 方法二：或是直接指定exe檔案路徑
driver = webdriver.Chrome("/Users/hsingyu/Documents/Projects/DynamicCrawler/chromedriver")

driver.get("https://rate.bot.com.tw/xrt/history/USD?Lang=zh-TW") # 更改網址以前往不同網頁

# 定位搜尋框
#element = driver.find_element_by_xpath('/html/body/div[1]/main/div[4]/div/table/tbody/tr[1]/td[7]/a')
# 傳入字串

#element.click()
#time.sleep(5)

#driver.find_element_by_id('search').send_keys('hi')
#Select(driver.find_element(By.ID,'lang_ddl')).select_by_index(2)

time.sleep(5)
select = Select(driver.find_element_by_css_selector('#ie11andabove > div > div > form:nth-child(2) > div.control-group > div > div > select:nth-child(2)'))
select.select_by_value("2021")
select = Select(driver.find_element_by_xpath('//*[@id="ie11andabove"]/div/div/form[2]/div[1]/div/div/select[2]'))
select.select_by_value("08")
select = Select(driver.find_element_by_xpath('//*[@id="ie11andabove"]/div/div/form[2]/div[1]/div/div/select[3]'))
select.select_by_value("09")


element = driver.find_elements_by_xpath('/html/body/div[1]/main/div[4]/div/div/form[2]/div[3]/a')[0]
element.click()
time.sleep(10)
driver.close() # 關閉瀏覽器視窗

