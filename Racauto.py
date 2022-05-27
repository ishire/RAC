import email
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/ikramshire/Downloads/chromedriver")
driver.maximize_window()
url = "https://skills.yourlearning.ibm.com/servicecenter/"
user="register@alberta.college"
password = "@Register2022!@"
driver.get(url)
login = driver.find_elements_by_xpath("/html/body/sb-root/div/sb-login/div/div[2]/div/div[1]/div/sb-account-btn/a/span")
#print(len(login))
if len(login) > 0:
    login[0].click()
email = driver.find_element_by_id("identifierId").send_keys(user)
sleep(3)
#pass1 = driver.find_element_by_id("password").send_keys(password)

login_button= driver.find_element_by_class_name("VfPpkd-vQzf8d")
login_button.click()
sleep(3)
pass1 = driver.find_element_by_name("password").send_keys(password)

send_button= driver.find_element_by_class_name("VfPpkd-vQzf8d")
send_button.click()

driver.get("https://skills.yourlearning.ibm.com/servicecenter/#home")


