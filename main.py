#!/usr/bin/env python

from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from manage_fun.add_fun import wrc
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import pickle, time, datetime, os


PATH_enter_faucet = "//*[@id='app-mount']/div[2]/div/div[2]/div/div[1]/div/div[@class='content-1SgpWY']/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/span/span"
PATH_entrence_menu  = "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div[1]/div/div[@class='content-1SgpWY']/div[1]/section/div[2]/div[3]/button[3]"
PATH_press_exit = "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[@aria-label='Выйти']/div"
PATH_click_exit = "//*[@id=\"app-mount\"]/div[4]/div[2]/div/div/div[3]/button[1]"
PATH_click_check = "//*[@id=\"checkbox\"]"


useragent = UserAgent()

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(f"user-agent={useragent.random}")
options.add_argument("user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'")

one_day = 24 * 60 * 60 
while True:
    driver = webdriver.Chrome(executable_path="/home/illya/Documents/My_test_work/work_withBrouser/Discord_token/chromedriver", options=options)
    data = wrc.get_all()
    print("Цикл розпочатий!")
    for dt in data["data"]:
        driver.get("https://discord.com/login")
        assert "Discord" in driver.title
        time.sleep(5)
        driver.save_screenshot("discord.png")
        os.system("rm /var/www/html/img/discord.png")
        os.system("mv discord.png /var/www/html/img")
        time.sleep(30)

        # enter_e = driver.find_element_by_name("email")
        # enter_p = driver.find_element_by_name("password")
        # enter_e.clear()
        # enter_p.clear()
        # enter_e.send_keys(dt[0])
        # time.sleep(3)
        # enter_p.send_keys(dt[1])
        # time.sleep(3)
        # enter_p.send_keys(Keys.RETURN)
        # time.sleep(5)
    
        driver.get(data["url"][wrc.find_index((data, dt[2], "url"))][1])
        time.sleep(10)
        try:
            # send_message = driver.exit = driver.find_element(by=By.XPATH, value=PATH_enter_faucet)
            # send_message.clear()
            # send_message.send_keys("$faucet " + data["address"][wrc.find_index((data, dt[3], "address"))][1] + "\n")
            # time.sleep(5)
            exit = driver.find_element(by=By.XPATH, value=PATH_entrence_menu).click()
            time.sleep(10)
            exit = driver.find_element(by=By.XPATH, value=PATH_press_exit).click()
            time.sleep(5)
            exit = driver.find_element(by=By.XPATH, value=PATH_click_exit).click()
            time.sleep(5)
        except Exception as ex:
            with open("error.log", "+a") as file:
                file.write(f"email: {dt[0]}; password: {dt[1]}")
                file.write(str(ex))
                print(f"Error email: {dt[0]} time: {datetime.datetime.now()}")
            driver.close()
            driver.quit()
            driver = webdriver.Chrome(executable_path="/home/illya/Documents/My_test_work/work_withBrouser/Discord_token/chromedriver", options=options)
    print("Цикл завершений")
    driver.close()
    driver.quit()
    time.sleep(10)
        