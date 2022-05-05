import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def get_btn_action(bot,reply):

    time.sleep(2)
    reply_btn = bot.find_elements_by_xpath('//div[@class="css-1dbjc4n r-xoduu5"]/*[name()="svg"][@class="r-4qtqp9 r-yyyyoo r-50lct3 r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1srniue"]')[0]
    retw_btn = bot.find_elements_by_xpath('//div[@class="css-1dbjc4n r-xoduu5"]/*[name()="svg"][@class="r-4qtqp9 r-yyyyoo r-50lct3 r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1srniue"]')[1]
    like_btn = bot.find_elements_by_xpath('//div[@class="css-1dbjc4n r-xoduu5"]/*[name()="svg"][@class="r-4qtqp9 r-yyyyoo r-50lct3 r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1srniue"]')[2]

    time.sleep(1)
    like_btn.click()
    
    
    
    retw_btn.click()

    retw_btn2 = bot.find_elements_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div[2]/div/span')[0]
    retw_btn2.click()
    
    
    time.sleep(2)
    reply_btn.click()
    sleep(2)
    reply_input = bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
)
    
    reply_input.send_keys(reply)
    reply_btn_final = bot.find_element_by_xpath(
    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span'
    )
    time.sleep(2)
    reply_btn_final.click()
    time.sleep(3)
    print("整个流程结束")

def init(url,tg_url,cookie,reply):
    chromeOptions = webdriver.ChromeOptions()
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {"performance": "ALL"}  # newer: goog:loggingPrefs
    driver = webdriver.Chrome(
        executable_path = "./chromedriver",
        options=chromeOptions, desired_capabilities=capabilities)
    while 1:
        try:
            driver.get(url)
            break
        except:
            sleep(TIMEOUT // 10)
    for i in range(len(cookie)):
        if 'sameSite' in cookie[i]:
            if cookie[i]['sameSite'] not in ['Strict', 'Lax', 'None']:
                cookie[i]['sameSite'] = 'None'
                
        driver.add_cookie(cookie[i])
    driver.get(tg_url)
    print('Initialize Success!')
    sleep(5)
    get_btn_action(driver,reply)
    return driver



root_path = "./cookies/"
TIMEOUT = 40   
ALLPARENTSNUMBER = 10000
USERINFOLIST = []
TRUSTLIST = []
print("读取设置数据")
with open('set.json', 'r') as obj:
    set_json = json.load(obj)
baseUrl = set_json['baseUrl']
tg_url = set_json['tg_url']
print("读取用户数据")
fo = open("user.txt", "r")
for index,line in enumerate(fo.readlines()):
    if index != 0:
        print("line",line)
        user = line.split("	")   
        username = user[0]
        reply = user[1]
        print("读取用户cookies")
        with open('./cookies/%s.json'%(username), 'r') as f:
            cookie = json.load(f)
        init(baseUrl,tg_url,cookie,reply)
        
