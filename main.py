#!/usr/bin/env python

from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from manage_fun.add_fun import wrc
import time


driver = webdriver.Chrome(executable_path="/home/illya/Documents/My_test_work/work_withBrouser/Discord_token/chromedriver")
one_day = 24 * 60 * 60 
while True:
    date = wrc.get_all()
    for dt in date["date"]:
        driver.get("https://discord.com/login")
        assert "Discord" in driver.title
        enter = driver.find_element_by_name("email")
        enter.send_keys(dt[0])
        time.sleep(2)
        enter = driver.find_element_by_name("password")
        enter.send_keys(dt[1])
        time.sleep(2)
        enter.send_keys(Keys.RETURN)
        time.sleep(4)
        driver.get("https://discord.com/channels/781005936260939818/953652276508119060")
        time.sleep(5)
        chat_url ="//*[@id='app-mount']/div[2]/div/div[2]/div/div[1]/div"
        chat_url_full = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div/span/span/span"
        send_message = driver.find_element_by_xpath(chat_url_full)
        send_message.clear()
        send_message.send_keys("faucet uptick18mcmka5np287fnv9803f8hly29s2yuygjhgq62\n")
        time.sleep(3)
        exit = driver.find_element_by_xpath("//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/section/div[2]/div[3]/button[3]/div").click()
        time.sleep(3)
        exit = driver.find_element_by_xpath("//*[@id=\"app-mount\"]/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[32]/div").click()
        time.sleep(3)
        exit = driver.find_element_by_xpath("//*[@id=\"app-mount\"]/div[4]/div[2]/div/div/div[3]/button[1]").click()
    time.sleep(one_day + 60)