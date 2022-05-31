import email
import os.path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

from selenium.webdriver.common.by import By

import pickle

url = "https://skills.yourlearning.ibm.com/servicecenter/"
user="register@alberta.college"
password = "@Register2022!@"
opt = webdriver.ChromeOptions()
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.maximize_window()

"""
Automatically logs into skillsbuild.org by inputting user info and dumps cookies to a text file.
"""
def firstlogin():
    
    driver.get(url)

    login = driver.find_elements(By.XPATH, "/html/body/sb-root/div/sb-login/div/div[2]/div/div[1]/div/sb-account-btn/a/span")
    if len(login) > 0:
        login[0].click()

    sleep(2)
    email = driver.find_element(By.ID, "identifierId").send_keys(user)

    login_button= driver.find_elements(By.XPATH, "//span[@jsname='V67aGc']")[1]
    login_button.click()

    sleep(1)

    pass1 = driver.find_element(By.NAME, "password").send_keys(password)
    send_button= driver.find_elements(By.XPATH, "//span[@jsname='V67aGc']")[1]
    send_button.click()

    driver.get("https://skills.yourlearning.ibm.com/servicecenter/#home")
    pickle.dump(driver.get_cookies(), open("cookies.txt", "wb"))

"""
Inserts saved cookies into browser and visits skillsbuild site with saved login.
"""
def cookieLogin():
    cookies = pickle.load(open("cookies.txt", "rb"))
    driver.delete_all_cookies()
    ibm = []
    sb = []
    for cookie in cookies:
        if cookie["domain"].find("yourlearning.ibm") > 0:
            sb.append(cookie)
        elif cookie["domain"].find("ibm.com"):
            ibm.append(cookie)
    driver.get("https://ibm.com")
    for cookie in ibm:
        driver.add_cookie(cookie)
    # driver.get("https://skills.yourlearning.ibm.com//")
    for cookie in sb:
        # to avoid domain mismatch, because skills.yourlearning.ibm.com is only available after login
        cookie["domain"] = '.ibm.com'
        driver.add_cookie(cookie)
    
    driver.implicitly_wait(1)
    driver.get("https://skills.yourlearning.ibm.com/servicecenter/#home")

if os.path.exists("cookies.txt"):
    cookieLogin()
else:
    firstlogin()
