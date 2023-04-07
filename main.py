from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from datetime import datetime
import time
import os

mail = ""
password = ""
saat = ""
trying = 1

def func(password, mail, saat):
    ser = Service("chromedriver.exe")
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options = webdriver.ChromeOptions()
    options.add_argument(
        r"user-data-dir={}".format(profile))

    driver = webdriver.Chrome(options=options, service=ser)
    driver.get('https://online.yildiz.edu.tr/?transaction=LMS.CORE.Cockpit.ViewCockpit')
    time.sleep(3)

    def joiner():
        isrighttime = 1
        while(isrighttime):
            now = datetime.now()
            current_time = now.strftime("%H")
            print(str(current_time))
            if(str(current_time) == saat):
                trying = 0
                driver.find_element(By.XPATH, '//*[@id="flow-tab"]/div/div[2]/div[3]').click()
                time.sleep(2)
                tryuntil = 1
                while (tryuntil):
                    time.sleep(1)
                    driver.refresh()
                    time.sleep(4)
                    try:
                        driver.find_element(By.XPATH, '//*[text()="Derse Katıl"]').click()
                        time.sleep(5)
                        try:
                            x = 0
                            while(x < 5):
                                import pyautogui
                                pyautogui.press("tab", presses=2)
                                pyautogui.press("enter")
                                time.sleep(4)
                                x += 1
                        except:
                            pass
                        tryuntil = 0
                        break
                    except:
                        pass
            time.sleep(60)


    try:
        driver.find_element(By.XPATH, '//*[@id="Data_Mail"]').send_keys(mail)
        driver.find_element(By.XPATH, '//*[@id="Data_Password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="Information"]/div[3]/div[2]/button').click()

        while (trying):
            time.sleep(5)
            try:
                joiner()
            except:
                pass
    except:
        while (trying):
            time.sleep(5)
            try:
                joiner()
            except:
                pass

def starter():
    z = open('mailpass.txt', "r").readlines()
    print(z)
    mail = z[0].split(" ")[1].split("\n")[0]
    password = z[1].split(" ")[1]
    saat = z[2].split(" ")[1]
    func(password, mail, saat)

time.sleep(1)
starter()