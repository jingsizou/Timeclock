# -*- coding:utf-8 -*-

import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# python3.8 -m pip install urllib3==1.26.6

def is_element_present(browser, xpath):
    from selenium.common.exceptions import NoSuchElementException

    try:
    # //*[@id="wrapper"]/aside/section/form/div/div[2]/div[1]/div[1]
        element = browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[1]")
    except NoSuchElementException as e:
        # print(e)
        print("Don't find element")
    else:
        print("Find element")

print("Hello World")
print("Hello Yina! **^_^**")

# set to no-window
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")

time.sleep(random.randint(10, 20))

# simulate a browser to open the website
# browser = webdriver.Chrome(options=chrome_options)
browser = webdriver.Chrome()
# browser = webdriver.Chrome()
browser.get("https://www.eton88.com/time")
# browser.find_element_by_xpath("//*[@id='mt_5']/div[1]/div[3]/input").send_keys(uid)
is_element_present(browser, "/html/body/div/aside/section/form/div/div[2]/div[1]/input")
is_element_present(browser, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[1]/input")
uid = "eric"
pwd = "01242023Etonict9483"
browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/input").send_keys(uid)
browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[1]/input").send_keys(pwd)


time.sleep(3)

# Click in button
print("Click to Check in")
is_element_present(browser, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[4]/button[2]")
browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[4]/button[2]").click()

time.sleep(random.randint(10, 20))

# Click out button
browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/input").send_keys(uid)
browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[1]/input").send_keys(pwd)
print("Click to Check out")
is_element_present(browser, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[4]/button[4]")
browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[4]/button[4]").click()


# Click Lunch Button
# print("Click to Lunch")
# is_element_present(browser, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[4]/button[3]")
# browser.find_element(By.XPATH, "/html/body/div/aside/section/form/div/div[2]/div[1]/div[4]/button[3]").click()


print("Chrome Open! **^_^**")
