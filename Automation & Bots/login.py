from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


def login(user,passwd):
    # fixing some options to make our bot indetectabel 
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'user-agent={user_agent}')

    # enter the path of chrome driver
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe",options=options)

    # get our page whos we want to work with it
    driver.get("https://fr-fr.facebook.com/")

    # get the elements from the html
    Email  = driver.find_element_by_id("email")
    passwd = driver.find_element_by_id("pass")
    btn    = driver.find_element_by_name("login")

    # emplement the elements with some information 
    Email.send_keys(f"{user}")
    passwd.send_keys(f"{passwd}")
    time.sleep(2)
    btn.click()


user = input("=> Enter Your Email : ")
passwd = input("=> Enter Your Password : ")
login(user,passwd)