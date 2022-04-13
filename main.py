#!/usr/bin/env python

from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from manage_fun.add_fun import wrc
from fake_useragent import UserAgent
# from selenium.webdriver.common.options import Options
from selenium.webdriver.common.by import By
import time

PATH_enter_faucet = "//*[@id='app-mount']/div[2]/div/div[2]/div/div[1]/div/div[@class='content-1SgpWY']/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/span/span"
PATH_entrence_menu  = "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div[1]/div/div[@class='content-1SgpWY']/div[1]/section/div[2]/div[3]/button[3]"
PATH_press_exit = "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[@aria-label='Выйти']/div"
PATH_click_exit = "//*[@id=\"app-mount\"]/div[4]/div[2]/div/div/div[3]/button[1]"



useragent = UserAgent()

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"user-agent={useragent.random}")
one_day = 24 * 60 * 60 
while True:
    driver = webdriver.Chrome(executable_path="/home/illya/Documents/My_test_work/work_withBrouser/Discord_token/chromedriver", options=options)
    date = wrc.get_all()
    for dt in date["date"]:
        driver.get("https://discord.com/login")
        assert "Discord" in driver.title
        time.sleep(2)
        enter = driver.find_element_by_name("email")
        enter.clear()
        enter.send_keys(dt[0])
        time.sleep(5)
        enter = driver.find_element_by_name("password")
        enter.clear()
        enter.send_keys(dt[1])
        time.sleep(5)
        enter.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.get("https://discord.com/channels/781005936260939818/953652276508119060")
        print("Enter uptick")
        time.sleep(10)
        try:
            # send_message = driver.exit = driver.find_element(by=By.XPATH, value=PATH_enter_faucet)
            # send_message.clear()
            # send_message.send_keys("$faucet " + date["address"][0][1] + "\n")
            # time.sleep(5)
            exit = driver.find_element(by=By.XPATH, value=PATH_entrence_menu).click()
            time.sleep(10)
            exit = driver.find_element(by=By.XPATH, value=PATH_press_exit).click()
            time.sleep(5)
            exit = driver.find_element(by=By.XPATH, value=PATH_click_exit).click()
            time.sleep(5)
            print("Програма пройшла цикл")
        except Exception as ex:
            with open("error.log", "+a") as file:
                file.write(f"email: {dt[0]}; password: {dt[1]}")
                file.write(str(ex))
            driver.close()
            driver.quit()
            driver = webdriver.Chrome(executable_path="/home/illya/Documents/My_test_work/work_withBrouser/Discord_token/chromedriver", options=options)
        print("Продовжуємо!!!")
    driver.close()
    driver.quit()
    time.sleep(10)
        