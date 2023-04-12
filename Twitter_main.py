import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class InternetSpeedTwitterBot:

    def __init__(self):
        Chrome_Dev_path = "E:\Python Udemy\Day 48\Chrome Dev Tools\chromedriver.exe"
        driver = Service(Chrome_Dev_path)
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=driver, options=option)

        self.down=100
        self.up=500




    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.browser.get(url)
        sleep(5)
        go_btn=self.browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()
        sleep(30)
        temp=self.browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down=float((temp.text).strip())
        sleep(30)
        temp=self.browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float((temp.text).strip())
        print(self.down)
        print(self.up)


    def tweet_at_provider(self):
        email = "mamun.kfz@gmail.com"
        passd = "testing@464"
        url = "https://twitter.com/"
        msg=f"Hey Internet Provider @amberit_se, why is my internet speed {self.down}down/{self.up}up when I pay for 150down/10up?"
        self.browser.get(url)
        sleep(10)
        login=self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span')
        login.click()
        sleep(10)
        userName_set=self.browser.find_element(By.XPATH,'//input[@autocomplete="username"]')
        userName_set.send_keys(email)
        userName_set.send_keys(Keys.ENTER)
        time.sleep(3)
        userPass_set = self.browser.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
        userPass_set.send_keys(passd)
        userPass_set.send_keys(Keys.ENTER)
        sleep(6)
        twt_txt=self.browser.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")
        twt_txt.send_keys(msg)
        sleep(3)
        twt=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        twt.click()
classObj=InternetSpeedTwitterBot()
classObj.get_internet_speed()
classObj.tweet_at_provider()
